"""Run the AI sprint report demo.

Example:
    python report_demo.py sample_sprint_data.md sample_user_data.md \
        sprint_report_prompt.md --provider=litellm
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from app_data_supplier import DemoAppDataSupplier, load_markdown_json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Draft a sprint report from app data and user report notes."
    )
    parser.add_argument("sprint_data", help="Markdown file with app data JSON")
    parser.add_argument("user_data", help="Markdown file with user note JSON")
    parser.add_argument("prompt", help="Markdown file with the base prompt")
    parser.add_argument(
        "--provider",
        choices=["openai", "litellm"],
        default="litellm",
        help="Model provider to use. Defaults to litellm.",
    )
    parser.add_argument(
        "--sprint-id",
        default=None,
        help="Sprint id to report on. Defaults to project.active_sprint_id.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the assembled prompt without calling the model.",
    )
    return parser.parse_args()


def selected_model(provider: str) -> str:
    if provider == "openai":
        return os.environ.get("OPENAI_MODEL", "gpt-5.6-luna")
    return os.environ.get("LITELLM_MODEL", os.environ.get("MODEL", "classroom-chat"))


def create_ai_client(provider: str):
    """Create the selected OpenAI-compatible client and model name."""
    from openai import OpenAI

    if provider == "openai":
        ai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        model = selected_model(provider)
        return ai_client, model

    ai_client = OpenAI(
        base_url=os.environ.get(
            "LITELLM_URL",
            os.environ.get("LITELLM_BASE_URL", "http://ml-capstone.cs.byu.edu:4000/v1"),
        ),
        api_key=os.environ.get("LITELLM_API_KEY", "sk-noauth"),
    )
    model = selected_model(provider)
    return ai_client, model


def build_full_prompt(base_prompt: str, sprint_context: dict) -> str:
    return (
        f"{base_prompt.rstrip()}\n\n"
        "## Sprint context\n\n"
        "Use the following JSON as the only source of project facts.\n\n"
        "```json\n"
        f"{json.dumps(sprint_context, indent=2)}\n"
        "```"
    )


def main() -> None:
    args = parse_args()

    app_data = DemoAppDataSupplier(args.sprint_data)
    raw_data = app_data.data
    sprint_id = args.sprint_id or raw_data["project"]["active_sprint_id"]
    user_report_notes = load_markdown_json(args.user_data)
    base_prompt = Path(args.prompt).read_text(encoding="utf-8")

    sprint_context = app_data.build_sprint_report_context(
        sprint_id=sprint_id,
        user_report_notes=user_report_notes,
    )
    full_prompt = build_full_prompt(base_prompt, sprint_context)
    model = selected_model(args.provider)

    print(f"Provider: {args.provider}")
    print(f"Model: {model}")
    print()

    if args.dry_run:
        print(full_prompt)
        return

    ai_client, model = create_ai_client(args.provider)
    response = ai_client.responses.create(
        model=model,
        input=full_prompt,
    )

    print(response.output_text)


if __name__ == "__main__":
    main()

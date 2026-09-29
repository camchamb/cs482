"""Run AI sprint report evaluation cases and create scoring worksheets.

Example:
    python run_eval_cases.py --dry-run
    python run_eval_cases.py --provider=openai
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from app_data_supplier import DemoAppDataSupplier, load_markdown_json
from report_demo import build_full_prompt, create_ai_client, selected_model


EXPECTED_HEADINGS = [
    "Team name",
    "Report date",
    "Sprint Goal",
    "Velocity Trend",
    "Sprint Deliveries & Validation",
    "Key Decisions / Blockers",
    "Next Sprint Goals",
    "Faculty Feedback / Requests",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate sprint report eval outputs and scorecards."
    )
    parser.add_argument(
        "--cases-dir",
        default="eval_cases",
        help="Directory containing case folders.",
    )
    parser.add_argument(
        "--prompt",
        default="sprint_report_prompt.md",
        help="Prompt markdown file.",
    )
    parser.add_argument(
        "--output-dir",
        default="eval_outputs",
        help="Directory where reports and scorecards are written.",
    )
    parser.add_argument(
        "--provider",
        choices=["openai", "litellm"],
        default="litellm",
        help="Model provider to use. Defaults to litellm.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Write assembled prompts instead of calling the model.",
    )
    return parser.parse_args()


def case_directories(cases_dir: Path) -> list[Path]:
    return sorted(path for path in cases_dir.iterdir() if path.is_dir())


def heading_check(report: str) -> list[str]:
    missing = []
    for heading in EXPECTED_HEADINGS:
        pattern = rf"(^|\n)\s*{re.escape(heading)}\s*:"
        if not re.search(pattern, report, flags=re.IGNORECASE):
            missing.append(heading)
    return missing


def build_scorecard(
    case_name: str,
    provider: str,
    model: str,
    expected_facts: str,
    generated_report: str | None,
) -> str:
    if generated_report:
        missing_headings = heading_check(generated_report)
        heading_note = (
            "All expected headings found."
            if not missing_headings
            else "Missing headings: " + ", ".join(missing_headings)
        )
    else:
        heading_note = "Not checked in dry-run mode."

    return f"""# Scorecard: {case_name}

Provider: {provider}  
Model: {model}

## Simple Automated Check

- Template headings: {heading_note}

This check only looks for expected headings. It does not evaluate factual
correctness, grounding, usefulness, or whether the generated content belongs in
the report.

## Human Scoring Rubric

Score each category from 0-2.

| Category | Score | Notes |
|---|---:|---|
| Groundedness: claims are supported by sprint context |  |  |
| Completeness: important expected facts are included |  |  |
| Template fit: output uses only the expected report fields |  |  |
| Missing-data behavior: missing or zero-state data is handled honestly |  |  |
| Usefulness after human review: draft is a practical starting point |  |  |

Total: ____ / 10

## Expected Facts and Failure Checks

{expected_facts.rstrip()}

## Generated Report

{generated_report.rstrip() if generated_report else "Dry-run mode did not call the model."}
"""


def main() -> None:
    args = parse_args()
    root = Path(__file__).parent
    cases_dir = root / args.cases_dir
    prompt_path = root / args.prompt
    output_dir = root / args.output_dir
    output_dir.mkdir(exist_ok=True)

    base_prompt = prompt_path.read_text(encoding="utf-8")
    provider = args.provider
    model = selected_model(provider)
    ai_client = None

    if not args.dry_run:
        ai_client, model = create_ai_client(provider)

    for case_dir in case_directories(cases_dir):
        app_data = DemoAppDataSupplier(case_dir / "sprint_data.md")
        raw_data = app_data.data
        sprint_id = raw_data["project"]["active_sprint_id"]
        user_notes = load_markdown_json(case_dir / "user_data.md")
        expected_facts = (case_dir / "expected_facts.md").read_text(
            encoding="utf-8"
        )

        context = app_data.build_sprint_report_context(sprint_id, user_notes)
        full_prompt = build_full_prompt(base_prompt, context)

        case_output_dir = output_dir / case_dir.name
        case_output_dir.mkdir(exist_ok=True)
        (case_output_dir / "assembled_prompt.md").write_text(
            full_prompt, encoding="utf-8"
        )

        generated_report = None
        if not args.dry_run:
            response = ai_client.responses.create(model=model, input=full_prompt)
            generated_report = response.output_text
            (case_output_dir / "generated_report.md").write_text(
                generated_report, encoding="utf-8"
            )

        scorecard = build_scorecard(
            case_name=case_dir.name,
            provider=provider,
            model=model,
            expected_facts=expected_facts,
            generated_report=generated_report,
        )
        (case_output_dir / "scorecard.md").write_text(scorecard, encoding="utf-8")
        print(f"Wrote {case_output_dir}")


if __name__ == "__main__":
    main()

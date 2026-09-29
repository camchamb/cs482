# Lecture 7 AI Sprint Report Demo

This demo shows how an app can assemble structured sprint data and user-entered
report notes before calling an OpenAI-compatible Responses API endpoint.

## Run without calling a model

```bash
python report_demo.py sample_sprint_data.md sample_user_data.md sprint_report_prompt.md --dry-run
```

## Run with the course LiteLLM endpoint

```bash
export LITELLM_URL="http://ml-capstone.cs.byu.edu:4000/v1"
export LITELLM_API_KEY="..."
export LITELLM_MODEL="classroom-chat"

python report_demo.py sample_sprint_data.md sample_user_data.md sprint_report_prompt.md
```

## Run with OpenAI

```bash
export OPENAI_API_KEY="..."
export OPENAI_MODEL="gpt-5.6-luna"

python report_demo.py sample_sprint_data.md sample_user_data.md sprint_report_prompt.md --provider=openai
```

## Files

- `report_demo.py` chooses the provider, assembles the prompt, and calls the model.
- `app_data_supplier.py` simulates backend API/data calls using canned markdown data.
- `sample_sprint_data.md` contains app state.
- `sample_user_data.md` contains report notes a frontend might collect from the user.
- `sprint_report_prompt.md` contains the base prompt students can revise for validation experiments.
- `eval_cases/` contains representative sprint contexts with expected facts.
- `run_eval_cases.py` runs all evaluation cases and writes report outputs plus human scoring worksheets.

## Evaluate Report Generation

Dry-run all cases without calling a model:

```bash
python run_eval_cases.py --dry-run
```

Run all cases with OpenAI:

```bash
python run_eval_cases.py --provider=openai
```

Run all cases with LiteLLM:

```bash
python run_eval_cases.py --provider=litellm
```

Outputs are written to the ignored `eval_outputs/` directory. Each case output includes:

- `assembled_prompt.md`
- `generated_report.md` when a model call is made
- `scorecard.md` for human scoring

The scorecard includes a simple heading check, but the real evaluation is
human-driven. Score groundedness, completeness, template fit, missing-data
behavior, and usefulness after human review.

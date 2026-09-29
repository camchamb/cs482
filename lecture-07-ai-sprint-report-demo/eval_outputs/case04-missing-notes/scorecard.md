# Scorecard: case04-missing-notes

Provider: litellm  
Model: classroom-chat

## Simple Automated Check

- Template headings: Missing headings: Team name, Report date, Sprint Goal, Velocity Trend, Sprint Deliveries & Validation, Key Decisions / Blockers, Next Sprint Goals, Faculty Feedback / Requests

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

# Expected Facts

## Must Include

- Team name is Clean Sweep.
- Report date is Nov 12.
- Sprint goal is to add data quality checks and issue tracking.
- Velocity N has planned 7, completed 6, percentage 86%.
- Velocity N-1 has planned 5, completed 4, percentage 80%.
- Deliveries should include missing-value detection and data quality issue tracking.
- Next Sprint Goals should include duplicate-row detection and export of quality summaries.

## Forbidden Claims

- Do not invent key decisions.
- Do not invent faculty feedback requests.
- Do not invent blockers or risks.

## Missing-Data Behavior

- Key Decisions / Blockers should say missing from provided context or clearly indicate none were provided.
- Faculty Feedback / Requests should say missing from provided context or clearly indicate none were provided.

## Generated Report

- Team name: Clean Sweep  
- Report date: Nov 12  
- Sprint Goal: Add data quality checks and issue tracking.  
- Velocity Trend:  
  Sprint N-2: N/A (no data)  
  Sprint N-1: Planned 5, Completed 4, Percentage 80%  
  Sprint N: Planned 6, Completed 6, Percentage 86%  
- Sprint Deliveries & Validation:  
  - Detect missing values by column (Iris): Validated with two CSV uploads; missing-value counts matched manual spreadsheet checks.  
  - Track data quality issues (Kai): Validated by creating three issues and confirming appearance in dataset issue list.  
- Key Decisions / Blockers: Missing from provided context.  
- Next Sprint Goals:  
  - Add duplicate-row detection.  
  - Add export of data quality issue summaries.  
- Faculty Feedback / Requests: Missing from provided context.

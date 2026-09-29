# Scorecard: case02-active-sprint-no-history

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

- Team name is Sprint Founders.
- Report date is Sep 24.
- Sprint goal is to create the initial sponsor intake workflow.
- Velocity N has planned 4, with completed and percentage not reported.
- Sprint Deliveries & Validation should state that no completed deliveries are recorded yet or that supporting context is missing.
- Key Decisions / Blockers should include the shared workspace decision.
- Next Sprint Goals should include intake form and project summary view.
- Faculty Feedback / Requests should ask whether the first sprint goals are narrow enough.

## Forbidden Claims

- Do not invent prior sprints.
- Do not claim any story is complete.
- Do not invent blockers.

## Missing-Data Behavior

- The report should distinguish "no completed deliveries yet" from fabricated missing facts.

## Generated Report

- Team name: Sprint Founders  
- Report date: Sep 24  
- Sprint Goal: Create the initial sponsor intake workflow.  
- Velocity Trend:  
  Sprint N: Planned 4, Completed —, Percentage —  
- Sprint Deliveries & Validation: Missing from provided context.  
- Key Decisions / Blockers: Start with one shared workspace before adding team-specific views.  
- Next Sprint Goals:  
  - Build the sponsor intake form.  
  - Create a project summary view.  
- Faculty Feedback / Requests: Are these first sprint goals narrow enough?

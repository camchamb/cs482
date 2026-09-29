# Scorecard: case03-blockers-and-risks

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

- Team name is Review Crew.
- Report date is Nov 5.
- Sprint goal is to deploy the review planner and add report generation.
- Velocity N has planned 6, with completed and percentage not reported.
- Deliveries should summarize rubric scoring and faculty feedback note capture.
- Key Decisions / Blockers should mention staging deployment priority, missing database URL secret, and report prompt example risk.
- Next Sprint Goals should include deployment secret fix, review summary draft, and prompt examples.
- Faculty Feedback / Requests should request review of summary concision.

## Forbidden Claims

- Do not claim staging deployment is fixed.
- Do not claim review summary generation is complete.
- Do not omit the missing database URL secret blocker.

## Missing-Data Behavior

- Current sprint completed work should not be inferred from in-progress items.

## Generated Report

- Team name: Review Crew  
- Report date: Nov 5  
- Sprint Goal: Deploy the review planner and add report generation.  
- Velocity Trend:  
  N: Planned 6, Completed N/A, Percentage N/A  
  N-1: Planned 9, Completed 6, Percentage 67%  
  N-2: Planned 6, Completed 4, Percentage 67%  
- Sprint Deliveries & Validation:  
  - Implement rubric scoring (Nia): Scored three sample review packets and confirmed saved totals matched rubric weights.  
  - Capture faculty feedback notes (Owen): Added notes to two review packets and confirmed they appeared in packet history.  
- Key Decisions / Blockers:  
  - Prioritize staging deployment before adding more report formatting.  
  - Staging deploy fails due to missing database URL secret.  
  - Report quality may be weak until concise feedback examples are provided.  
- Next Sprint Goals:  
  - Fix staging deployment secret configuration.  
  - Add review summary draft generation.  
  - Add examples to the report prompt.  
- Faculty Feedback / Requests:  
  - Can a professor review whether the feedback summary is concise enough?

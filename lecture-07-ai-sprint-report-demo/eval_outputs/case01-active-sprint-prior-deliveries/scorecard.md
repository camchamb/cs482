# Scorecard: case01-active-sprint-prior-deliveries

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

- Team name is The Quinnovators.
- Report date is Oct 29.
- Sprint goal is the Sprint 3 goal.
- Velocity N has planned 5, with completed and percentage not reported.
- Velocity N-1 has planned 10, completed 7, percentage 70%.
- Velocity N-2 has planned 8, completed 5, percentage 63%.
- Deliveries should summarize Sprint 2 completed work, especially persistence, sprint board/backlog views, and sprint close/history.
- Key Decisions / Blockers should include the shared-password decision and SQLite persistence blocker/risk.
- Next Sprint Goals should include AI report endpoint, database persistence, and team review prep.
- Faculty Feedback / Requests should include the deployment-persistence question.

## Forbidden Claims

- Do not claim Sprint 3 has completed stories.
- Do not invent a completed percentage for Sprint 3.
- Do not say authentication or persistence is fully complete for Sprint 3.

## Missing-Data Behavior

- Current-sprint completed and percentage values should be marked as not reported or missing, not invented.

## Generated Report

- Team name: The Quinnovators  
- Report date: Oct 29  
- Sprint Goal: Build a usable team version of the workflow app with sprint planning and AI report drafting.  
- Velocity Trend:  
  Sprint N (Sprint 3): Planned 5, Completed N/A, Percentage N/A  
  Sprint N-1 (Sprint 2): Planned 10, Completed 7, Percentage 70%  
  Sprint N-2 (Sprint 1): Planned 8, Completed 5, Percentage 63%  
- Sprint Deliveries & Validation:  
  • Create persistent project storage (Sam): Validated by creating, editing, and reloading three projects after restarting the backend process.  
  • Support backlog and sprint-assigned story views (Leo): Validated by verifying unassigned stories appeared in backlog while sprint-assigned stories appeared on the sprint board.  
  • Support closing active sprint while preserving completed story history (Maya): Validated by closing Sprint 2 through the app and confirming completed stories remained attached to the closed sprint history view.  
- Key Decisions / Blockers:  
  • Authentication will use one shared team password for now.  
  • SQLite data is not persisting after deployment because the database file is outside the named volume path.  
  • Missing faculty feedback and next sprint goals (report notes contain draft content, but faculty feedback and next sprint goals are not confirmed final).  
- Next Sprint Goals: Missing from provided context.  
- Faculty Feedback / Requests: Should deployment persistence be fixed before improving the AI sprint report?

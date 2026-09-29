# Scorecard: case05-conflicting-context

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

- Team name is Roadmap Rangers.
- Report date is Nov 19.
- Sprint goal is to add roadmap timeline and readiness review export.
- Velocity N has planned 8, completed 4, percentage 50%.
- Deliveries should include roadmap timeline view.
- Key Decisions / Blockers should include timeline-first presentation and the conflict/risk around export readiness.
- Next Sprint Goals should include finishing readiness review export and adding risk notes.
- Faculty Feedback / Requests should ask about risk detail in the export.

## Forbidden Claims

- Do not say the readiness review export is complete.
- Do not ignore the stored app status showing the export is in progress.
- Do not claim all planned work was completed.

## Missing-Data Behavior

- If mentioning the conflict, the report should indicate that stored app data shows the export is not complete.

## Generated Report

- Team name: Roadmap Rangers  
- Report date: Nov 19  
- Sprint Goal: Add roadmap timeline and readiness review export.  
- Velocity Trend:  
  - Sprint N: Planned 8, Completed 4, Percentage 50%  
  - Sprint N-1: Planned 6, Completed 3, Percentage 50%  
  - Sprint N-2: Missing from provided context.  
- Sprint Deliveries & Validation:  
  - Create roadmap timeline view: Confirmed three milestones appeared in chronological order.  
- Key Decisions / Blockers:  
  - Use a timeline-first presentation for sponsor readiness.  
  - Export currently omits risk notes.  
- Next Sprint Goals:  
  - Finish readiness review export.  
  - Add risk notes to exported outlines.  
- Faculty Feedback / Requests:  
  - Should the readiness review export include detailed risks or only a summary?

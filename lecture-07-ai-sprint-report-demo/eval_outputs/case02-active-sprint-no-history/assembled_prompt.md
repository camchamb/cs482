# Sprint Report Prompt

Draft a concise sprint report for a faculty sprint review meeting.

Use only the facts provided in the sprint context. Do not invent work, blockers,
decisions, faculty feedback, metrics, or progress. If the context lacks
information needed for a section, say what is missing.

## Output contract

The shared sprint report template contains these fields:

- Team name
- Report date
- Sprint Goal: one or two sentences
- Velocity Trend: last three sprints with Sprint, Planned, Completed, Percentage.
  `N` means the current sprint, `N-1` means the previous sprint, and `N-2`
  means two sprints ago. For the current sprint, include planned work but do
  not invent completed work or a percentage if the sprint has just begun.
- Sprint Deliveries & Validation: up to three concise bullets. If more stories were completed
  you must select the ones you think provided the most value. Focus more on sprint titles, but
  use validation evidence to weigh story value and to confirm story was correctly completed.
- Key Decisions / Blockers: up to three concise bullets
- Next Sprint Goals: up to three concise bullets
- Faculty Feedback / Requests: up to three concise bullets

The `deliveries` field may come from the most recent closed sprint when the
current sprint has just begun. Use the provided `deliveries_source_sprint` to
understand which sprint the delivered work came from, but do not add an extra
section for it.

Return only content for those fields. Do not add extra sections, commentary,
markdown tables, introductions, or explanations. If a field has no supported
content, write `Missing from provided context.`

## Sprint context

Use the following JSON as the only source of project facts.

```json
{
  "team_name": "Sprint Founders",
  "report_date": "Sep 24",
  "project": {
    "id": "project-2",
    "name": "Sponsor Intake App",
    "summary": "A lightweight intake tool for sponsor project information."
  },
  "sprint": {
    "id": "sprint-1",
    "name": "Sprint 1",
    "goal": "Create the initial sponsor intake workflow.",
    "status": "active"
  },
  "deliveries_source_sprint": {
    "id": "sprint-1",
    "name": "Sprint 1",
    "status": "active"
  },
  "deliveries": [],
  "unfinished_work": [
    {
      "story_title": "Create sponsor intake form",
      "status": "selected for sprint",
      "owner": "Avery",
      "blocker_or_dependency_notes": ""
    },
    {
      "story_title": "Create project summary view",
      "status": "selected for sprint",
      "owner": "Jordan",
      "blocker_or_dependency_notes": ""
    }
  ],
  "velocity_trend": [
    {
      "sprint": "N",
      "sprint_id": "sprint-1",
      "planned": 4,
      "completed": null,
      "percentage": null
    }
  ],
  "report_notes": {
    "key_decisions": [
      "Start with one shared workspace before adding team-specific views."
    ],
    "risks_or_tradeoffs": [],
    "next_sprint_goals": [
      "Build the sponsor intake form.",
      "Create a project summary view."
    ],
    "faculty_feedback_requests": [
      "Are these first sprint goals narrow enough?"
    ],
    "additional_context": "This is the first sprint, so there is no prior delivery history."
  }
}
```
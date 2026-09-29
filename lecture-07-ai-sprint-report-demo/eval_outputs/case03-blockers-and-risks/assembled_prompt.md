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
  "team_name": "Review Crew",
  "report_date": "Nov 5",
  "project": {
    "id": "project-3",
    "name": "Architecture Review Planner",
    "summary": "A tool for organizing review artifacts and feedback."
  },
  "sprint": {
    "id": "sprint-3",
    "name": "Sprint 3",
    "goal": "Deploy the review planner and add report generation.",
    "status": "active"
  },
  "deliveries_source_sprint": {
    "id": "sprint-2",
    "name": "Sprint 2",
    "status": "closed"
  },
  "deliveries": [
    {
      "story_title": "Implement rubric scoring",
      "owner": "Nia",
      "validation_evidence": "Scored three sample review packets and confirmed saved totals matched rubric weights."
    },
    {
      "story_title": "Capture faculty feedback notes",
      "owner": "Owen",
      "validation_evidence": "Added notes to two review packets and confirmed they appeared in packet history."
    }
  ],
  "unfinished_work": [
    {
      "story_title": "Deploy review planner to staging",
      "status": "in progress",
      "owner": "Nia",
      "blocker_or_dependency_notes": "Staging deploy fails because the database URL secret is missing."
    },
    {
      "story_title": "Generate review summary draft",
      "status": "selected for sprint",
      "owner": "Owen",
      "blocker_or_dependency_notes": "Report prompt needs examples of concise review feedback."
    }
  ],
  "velocity_trend": [
    {
      "sprint": "N",
      "sprint_id": "sprint-3",
      "planned": 6,
      "completed": null,
      "percentage": null
    },
    {
      "sprint": "N-1",
      "sprint_id": "sprint-2",
      "planned": 9,
      "completed": 6,
      "percentage": "67%"
    },
    {
      "sprint": "N-2",
      "sprint_id": "sprint-1",
      "planned": 6,
      "completed": 4,
      "percentage": "67%"
    }
  ],
  "report_notes": {
    "key_decisions": [
      "Prioritize staging deployment before adding more report formatting."
    ],
    "risks_or_tradeoffs": [
      "Deployment secret handling is blocking review with realistic data.",
      "Report quality may be weak until we provide concise feedback examples."
    ],
    "next_sprint_goals": [
      "Fix staging deployment secret configuration.",
      "Add review summary draft generation.",
      "Add examples to the report prompt."
    ],
    "faculty_feedback_requests": [
      "Can a professor review whether the feedback summary is concise enough?"
    ],
    "additional_context": ""
  }
}
```
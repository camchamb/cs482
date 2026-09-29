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
  "team_name": "Roadmap Rangers",
  "report_date": "Nov 19",
  "project": {
    "id": "project-5",
    "name": "Sponsor Roadmap Tool",
    "summary": "A planning tool for sponsor project roadmaps."
  },
  "sprint": {
    "id": "sprint-2",
    "name": "Sprint 2",
    "goal": "Add roadmap timeline and readiness review export.",
    "status": "closed"
  },
  "deliveries_source_sprint": {
    "id": "sprint-2",
    "name": "Sprint 2",
    "status": "closed"
  },
  "deliveries": [
    {
      "story_title": "Create roadmap timeline view",
      "owner": "Riley",
      "validation_evidence": "Created three milestones and confirmed they appeared in chronological order."
    }
  ],
  "unfinished_work": [
    {
      "story_title": "Export readiness review outline",
      "status": "in progress",
      "owner": "Taylor",
      "blocker_or_dependency_notes": "Export currently omits risk notes."
    }
  ],
  "velocity_trend": [
    {
      "sprint": "N",
      "sprint_id": "sprint-2",
      "planned": 8,
      "completed": 4,
      "percentage": "50%"
    },
    {
      "sprint": "N-1",
      "sprint_id": "sprint-1",
      "planned": 6,
      "completed": 3,
      "percentage": "50%"
    }
  ],
  "report_notes": {
    "key_decisions": [
      "Use a timeline-first presentation for sponsor readiness."
    ],
    "risks_or_tradeoffs": [
      "User notes say the export is ready, but app data still marks readiness review export as in progress and missing risk notes."
    ],
    "next_sprint_goals": [
      "Finish readiness review export.",
      "Add risk notes to exported outlines."
    ],
    "faculty_feedback_requests": [
      "Should the readiness review export include detailed risks or only a summary?"
    ],
    "additional_context": "The export is basically ready."
  }
}
```
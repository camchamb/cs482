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
  "team_name": "Clean Sweep",
  "report_date": "Nov 12",
  "project": {
    "id": "project-4",
    "name": "Data Prep Tracker",
    "summary": "A tool for tracking data preparation tasks."
  },
  "sprint": {
    "id": "sprint-2",
    "name": "Sprint 2",
    "goal": "Add data quality checks and issue tracking.",
    "status": "closed"
  },
  "deliveries_source_sprint": {
    "id": "sprint-2",
    "name": "Sprint 2",
    "status": "closed"
  },
  "deliveries": [
    {
      "story_title": "Detect missing values by column",
      "owner": "Iris",
      "validation_evidence": "Uploaded two CSV files and confirmed missing-value counts matched manual spreadsheet checks."
    },
    {
      "story_title": "Track data quality issues",
      "owner": "Kai",
      "validation_evidence": "Created three data-quality issues and confirmed they appeared in the dataset issue list."
    }
  ],
  "unfinished_work": [],
  "velocity_trend": [
    {
      "sprint": "N",
      "sprint_id": "sprint-2",
      "planned": 7,
      "completed": 6,
      "percentage": "86%"
    },
    {
      "sprint": "N-1",
      "sprint_id": "sprint-1",
      "planned": 5,
      "completed": 4,
      "percentage": "80%"
    }
  ],
  "report_notes": {
    "key_decisions": [],
    "risks_or_tradeoffs": [],
    "next_sprint_goals": [
      "Add duplicate-row detection.",
      "Add export of data quality issue summaries."
    ],
    "faculty_feedback_requests": [],
    "additional_context": ""
  }
}
```
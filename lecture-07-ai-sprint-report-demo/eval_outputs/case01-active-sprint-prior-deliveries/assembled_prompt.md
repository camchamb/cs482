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
  "team_name": "The Quinnovators",
  "report_date": "Oct 29",
  "project": {
    "id": "project-1",
    "name": "Engineering Workflow App",
    "summary": "A lightweight project tracking app for CS 482 teams."
  },
  "sprint": {
    "id": "sprint-3",
    "name": "Sprint 3",
    "goal": "Build a usable team version of the workflow app with sprint planning and AI report drafting.",
    "status": "active"
  },
  "deliveries_source_sprint": {
    "id": "sprint-2",
    "name": "Sprint 2",
    "status": "closed"
  },
  "deliveries": [
    {
      "story_title": "Create persistent project storage",
      "owner": "Sam",
      "validation_evidence": "Created, edited, and reloaded three projects after restarting the backend process."
    },
    {
      "story_title": "Support backlog and sprint-assigned story views",
      "owner": "Leo",
      "validation_evidence": "Verified that unassigned stories appeared in backlog while sprint-assigned stories appeared on the sprint board."
    },
    {
      "story_title": "Support closing active sprint while preserving completed story history",
      "owner": "Maya",
      "validation_evidence": "Closed Sprint 2 through the app and confirmed completed stories remained attached to the closed sprint history view."
    }
  ],
  "unfinished_work": [
    {
      "story_title": "Add AI sprint report draft endpoint",
      "status": "selected for sprint",
      "owner": "Priya",
      "blocker_or_dependency_notes": ""
    },
    {
      "story_title": "Persist SQLite data after deployment",
      "status": "in progress",
      "owner": "Sam",
      "blocker_or_dependency_notes": "SQLite data is not persisting after deployment because the database file is outside the named volume path."
    }
  ],
  "velocity_trend": [
    {
      "sprint": "N",
      "sprint_id": "sprint-3",
      "planned": 5,
      "completed": null,
      "percentage": null
    },
    {
      "sprint": "N-1",
      "sprint_id": "sprint-2",
      "planned": 10,
      "completed": 7,
      "percentage": "70%"
    },
    {
      "sprint": "N-2",
      "sprint_id": "sprint-1",
      "planned": 8,
      "completed": 5,
      "percentage": "63%"
    }
  ],
  "report_notes": {
    "key_decisions": [
      "Keep authentication to one shared team password for now."
    ],
    "risks_or_tradeoffs": [
      "SQLite persistence must be fixed before the team review."
    ],
    "next_sprint_goals": [
      "Implement the AI sprint report draft endpoint.",
      "Fix deployed database persistence.",
      "Prepare a clean six-minute team workflow app review path."
    ],
    "faculty_feedback_requests": [
      "Should deployment persistence be fixed before improving the AI sprint report?"
    ],
    "additional_context": "Use closed Sprint 2 deliveries because Sprint 3 has just begun."
  }
}
```
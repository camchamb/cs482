# Case 03 Sprint Data

Closed sprint with clear deliveries and active blockers.

```json
{
  "project": {
    "id": "project-3",
    "name": "Architecture Review Planner",
    "team_name": "Review Crew",
    "summary": "A tool for organizing review artifacts and feedback.",
    "active_sprint_id": "sprint-3"
  },
  "sprints": [
    {
      "id": "sprint-1",
      "project_id": "project-3",
      "name": "Sprint 1",
      "goal": "Prototype review checklist storage.",
      "status": "closed",
      "planned_story_count": 6,
      "completed_story_count": 4,
      "completion_percentage": "67%"
    },
    {
      "id": "sprint-2",
      "project_id": "project-3",
      "name": "Sprint 2",
      "goal": "Implement rubric scoring and feedback capture.",
      "status": "closed",
      "planned_story_count": 9,
      "completed_story_count": 6,
      "completion_percentage": "67%"
    },
    {
      "id": "sprint-3",
      "project_id": "project-3",
      "name": "Sprint 3",
      "goal": "Deploy the review planner and add report generation.",
      "status": "active",
      "planned_story_count": 6
    }
  ],
  "stories": [
    {
      "id": "story-201",
      "sprint_id": "sprint-2",
      "title": "Implement rubric scoring",
      "status": "done",
      "owner": "Nia",
      "completed_in_sprint": true,
      "validation_evidence": "Scored three sample review packets and confirmed saved totals matched rubric weights."
    },
    {
      "id": "story-202",
      "sprint_id": "sprint-2",
      "title": "Capture faculty feedback notes",
      "status": "done",
      "owner": "Owen",
      "completed_in_sprint": true,
      "validation_evidence": "Added notes to two review packets and confirmed they appeared in packet history."
    },
    {
      "id": "story-301",
      "sprint_id": "sprint-3",
      "title": "Deploy review planner to staging",
      "status": "in progress",
      "owner": "Nia",
      "completed_in_sprint": false,
      "blocker_or_dependency_notes": "Staging deploy fails because the database URL secret is missing."
    },
    {
      "id": "story-302",
      "sprint_id": "sprint-3",
      "title": "Generate review summary draft",
      "status": "selected for sprint",
      "owner": "Owen",
      "completed_in_sprint": false,
      "blocker_or_dependency_notes": "Report prompt needs examples of concise review feedback."
    }
  ]
}
```

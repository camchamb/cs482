# Case 05 Sprint Data

User notes overstate progress compared with stored app data.

```json
{
  "project": {
    "id": "project-5",
    "name": "Sponsor Roadmap Tool",
    "team_name": "Roadmap Rangers",
    "summary": "A planning tool for sponsor project roadmaps.",
    "active_sprint_id": "sprint-2"
  },
  "sprints": [
    {
      "id": "sprint-1",
      "project_id": "project-5",
      "name": "Sprint 1",
      "goal": "Create sponsor project and milestone tracking.",
      "status": "closed",
      "planned_story_count": 6,
      "completed_story_count": 3,
      "completion_percentage": "50%"
    },
    {
      "id": "sprint-2",
      "project_id": "project-5",
      "name": "Sprint 2",
      "goal": "Add roadmap timeline and readiness review export.",
      "status": "closed",
      "planned_story_count": 8,
      "completed_story_count": 4,
      "completion_percentage": "50%"
    }
  ],
  "stories": [
    {
      "id": "story-201",
      "sprint_id": "sprint-2",
      "title": "Create roadmap timeline view",
      "status": "done",
      "owner": "Riley",
      "completed_in_sprint": true,
      "validation_evidence": "Created three milestones and confirmed they appeared in chronological order."
    },
    {
      "id": "story-202",
      "sprint_id": "sprint-2",
      "title": "Export readiness review outline",
      "status": "in progress",
      "owner": "Taylor",
      "completed_in_sprint": false,
      "blocker_or_dependency_notes": "Export currently omits risk notes."
    }
  ]
}
```

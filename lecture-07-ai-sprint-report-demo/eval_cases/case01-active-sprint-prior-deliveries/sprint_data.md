# Case 01 Sprint Data

Active sprint has just begun. The report should use the most recent closed
sprint for deliveries and validation.

```json
{
  "project": {
    "id": "project-1",
    "name": "Engineering Workflow App",
    "team_name": "The Quinnovators",
    "summary": "A lightweight project tracking app for CS 482 teams.",
    "active_sprint_id": "sprint-3"
  },
  "sprints": [
    {
      "id": "sprint-1",
      "project_id": "project-1",
      "name": "Sprint 1",
      "goal": "Create basic project and story tracking.",
      "status": "closed",
      "planned_story_count": 8,
      "completed_story_count": 5,
      "completion_percentage": "63%"
    },
    {
      "id": "sprint-2",
      "project_id": "project-1",
      "name": "Sprint 2",
      "goal": "Add sprint board behavior and persistence.",
      "status": "closed",
      "planned_story_count": 10,
      "completed_story_count": 7,
      "completion_percentage": "70%"
    },
    {
      "id": "sprint-3",
      "project_id": "project-1",
      "name": "Sprint 3",
      "goal": "Build a usable team version of the workflow app with sprint planning and AI report drafting.",
      "status": "active",
      "planned_story_count": 5
    }
  ],
  "stories": [
    {
      "id": "story-201",
      "sprint_id": "sprint-2",
      "title": "Create persistent project storage",
      "status": "done",
      "owner": "Sam",
      "completed_in_sprint": true,
      "validation_evidence": "Created, edited, and reloaded three projects after restarting the backend process."
    },
    {
      "id": "story-202",
      "sprint_id": "sprint-2",
      "title": "Support backlog and sprint-assigned story views",
      "status": "done",
      "owner": "Leo",
      "completed_in_sprint": true,
      "validation_evidence": "Verified that unassigned stories appeared in backlog while sprint-assigned stories appeared on the sprint board."
    },
    {
      "id": "story-203",
      "sprint_id": "sprint-2",
      "title": "Support closing active sprint while preserving completed story history",
      "status": "done",
      "owner": "Maya",
      "completed_in_sprint": true,
      "validation_evidence": "Closed Sprint 2 through the app and confirmed completed stories remained attached to the closed sprint history view."
    },
    {
      "id": "story-301",
      "sprint_id": "sprint-3",
      "title": "Add AI sprint report draft endpoint",
      "status": "selected for sprint",
      "owner": "Priya",
      "completed_in_sprint": false,
      "blocker_or_dependency_notes": ""
    },
    {
      "id": "story-302",
      "sprint_id": "sprint-3",
      "title": "Persist SQLite data after deployment",
      "status": "in progress",
      "owner": "Sam",
      "completed_in_sprint": false,
      "blocker_or_dependency_notes": "SQLite data is not persisting after deployment because the database file is outside the named volume path."
    }
  ]
}
```

# Case 04 Sprint Data

Closed sprint has data, but user notes omit decisions and faculty requests.

```json
{
  "project": {
    "id": "project-4",
    "name": "Data Prep Tracker",
    "team_name": "Clean Sweep",
    "summary": "A tool for tracking data preparation tasks.",
    "active_sprint_id": "sprint-2"
  },
  "sprints": [
    {
      "id": "sprint-1",
      "project_id": "project-4",
      "name": "Sprint 1",
      "goal": "Create upload and dataset summary flow.",
      "status": "closed",
      "planned_story_count": 5,
      "completed_story_count": 4,
      "completion_percentage": "80%"
    },
    {
      "id": "sprint-2",
      "project_id": "project-4",
      "name": "Sprint 2",
      "goal": "Add data quality checks and issue tracking.",
      "status": "closed",
      "planned_story_count": 7,
      "completed_story_count": 6,
      "completion_percentage": "86%"
    }
  ],
  "stories": [
    {
      "id": "story-201",
      "sprint_id": "sprint-2",
      "title": "Detect missing values by column",
      "status": "done",
      "owner": "Iris",
      "completed_in_sprint": true,
      "validation_evidence": "Uploaded two CSV files and confirmed missing-value counts matched manual spreadsheet checks."
    },
    {
      "id": "story-202",
      "sprint_id": "sprint-2",
      "title": "Track data quality issues",
      "status": "done",
      "owner": "Kai",
      "completed_in_sprint": true,
      "validation_evidence": "Created three data-quality issues and confirmed they appeared in the dataset issue list."
    }
  ]
}
```

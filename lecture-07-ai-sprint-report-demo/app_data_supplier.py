"""Demo app-data supplier for the AI sprint report example.

This module pretends to be the project-management application backend. In a
student app, each function below would usually become a database query or a
call to the app's own API endpoint.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


def load_markdown_json(path: str | Path) -> dict[str, Any]:
    """Load the first fenced JSON block from a markdown file."""
    markdown = Path(path).read_text(encoding="utf-8")
    match = re.search(r"```json\s*(.*?)\s*```", markdown, flags=re.DOTALL)
    if not match:
        raise ValueError(f"{path} must contain a fenced ```json block")
    return json.loads(match.group(1))



class DemoAppDataSupplier:
    """Read pre-canned app data and expose it through API-shaped methods."""

    def __init__(self, sprint_data_path: str | Path):
        self.data = load_markdown_json(sprint_data_path)

    def get_project(self, project_id: str) -> dict[str, Any]:
        # Replace this with: GET /api/projects/{project_id}
        project = self.data["project"]
        if project["id"] != project_id:
            raise KeyError(f"Unknown project_id: {project_id}")
        return project

    def get_sprint(self, sprint_id: str) -> dict[str, Any]:
        # Replace this with: GET /api/sprints/{sprint_id}
        for sprint in self.data["sprints"]:
            if sprint["id"] == sprint_id:
                return sprint
        raise KeyError(f"Unknown sprint_id: {sprint_id}")

    def get_stories_for_sprint(self, sprint_id: str) -> list[dict[str, Any]]:
        # Replace this with: GET /api/sprints/{sprint_id}/stories
        return [
            story
            for story in self.data["stories"]
            if story.get("sprint_id") == sprint_id
        ]

    def get_recent_sprints(
        self, project_id: str, current_sprint_id: str, limit: int = 3
    ) -> list[dict[str, Any]]:
        # Replace this with: GET /api/projects/{project_id}/sprints?recent=3
        project_sprints = [
            sprint
            for sprint in self.data["sprints"]
            if sprint["project_id"] == project_id
        ]
        current_index = next(
            i
            for i, sprint in enumerate(project_sprints)
            if sprint["id"] == current_sprint_id
        )
        start = max(0, current_index - limit + 1)
        return list(reversed(project_sprints[start : current_index + 1]))

    def get_velocity_trend(
        self, project_id: str, current_sprint_id: str, limit: int = 3
    ) -> list[dict[str, Any]]:
        # Replace this with: GET /api/projects/{project_id}/velocity?current=sprint-3
        recent_sprints = self.get_recent_sprints(project_id, current_sprint_id, limit)
        labels = ["N", "N-1", "N-2"]

        trend = []
        for label, sprint in zip(labels, recent_sprints):
            planned = sprint.get("planned_story_count")
            completed = sprint.get("completed_story_count")
            percentage = sprint.get("completion_percentage")

            if label == "N":
                planned = planned or len(self.get_stories_for_sprint(sprint["id"]))
                if sprint.get("status") == "active":
                    completed = None
                    percentage = None

            trend.append(
                {
                    "sprint": label,
                    "sprint_id": sprint["id"],
                    "planned": planned,
                    "completed": completed,
                    "percentage": percentage,
                }
            )
        return trend

    def get_most_recent_closed_sprint_before(
        self, project_id: str, sprint_id: str
    ) -> dict[str, Any] | None:
        # Replace this with: GET /api/projects/{project_id}/sprints?status=closed
        project_sprints = [
            sprint
            for sprint in self.data["sprints"]
            if sprint["project_id"] == project_id
        ]
        current_index = next(
            i for i, sprint in enumerate(project_sprints) if sprint["id"] == sprint_id
        )
        prior_sprints = reversed(project_sprints[:current_index])
        return next(
            (sprint for sprint in prior_sprints if sprint.get("status") == "closed"),
            None,
        )

    def build_sprint_report_context(
        self,
        sprint_id: str,
        user_report_notes: dict[str, Any],
    ) -> dict[str, Any]:
        """Collect app data plus frontend/user notes into one report context."""
        sprint = self.get_sprint(sprint_id)
        project = self.get_project(sprint["project_id"])
        stories = self.get_stories_for_sprint(sprint_id)

        completed_stories = [
            story for story in stories if story.get("completed_in_sprint")
        ]
        delivery_sprint = sprint

        if not completed_stories and sprint.get("status") == "active":
            prior_closed_sprint = self.get_most_recent_closed_sprint_before(
                project["id"], sprint_id
            )
            if prior_closed_sprint:
                delivery_sprint = prior_closed_sprint
                completed_stories = [
                    story
                    for story in self.get_stories_for_sprint(delivery_sprint["id"])
                    if story.get("completed_in_sprint")
                ]

        unfinished_stories = [
            story for story in stories if not story.get("completed_in_sprint")
        ]

        return {
            "team_name": project["team_name"],
            "report_date": user_report_notes.get("report_date"),
            "project": {
                "id": project["id"],
                "name": project["name"],
                "summary": project["summary"],
            },
            "sprint": {
                "id": sprint["id"],
                "name": sprint["name"],
                "goal": sprint["goal"],
                "status": sprint["status"],
            },
            "deliveries_source_sprint": {
                "id": delivery_sprint["id"],
                "name": delivery_sprint["name"],
                "status": delivery_sprint["status"],
            },
            "deliveries": [
                {
                    "story_title": story["title"],
                    "owner": story.get("owner"),
                    "validation_evidence": story.get("validation_evidence"),
                }
                for story in completed_stories
            ],
            "unfinished_work": [
                {
                    "story_title": story["title"],
                    "status": story["status"],
                    "owner": story.get("owner"),
                    "blocker_or_dependency_notes": story.get(
                        "blocker_or_dependency_notes"
                    ),
                }
                for story in unfinished_stories
            ],
            "velocity_trend": self.get_velocity_trend(project["id"], sprint["id"]),
            "report_notes": {
                "key_decisions": user_report_notes.get("key_decisions", []),
                "risks_or_tradeoffs": user_report_notes.get(
                    "risks_or_tradeoffs", []
                ),
                "next_sprint_goals": user_report_notes.get(
                    "next_sprint_goals", []
                ),
                "faculty_feedback_requests": user_report_notes.get(
                    "faculty_feedback_requests", []
                ),
                "additional_context": user_report_notes.get(
                    "additional_context", ""
                ),
            },
        }

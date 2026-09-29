# Sample User Report Notes

These notes represent values entered by the user in the app's report-generation
screen before the backend calls the model.

```json
{
  "report_date": "Oct 29",
  "key_decisions": [
    "Use a shared team schema based mostly on Maya's backend model, with Leo's simpler sprint board workflow.",
    "Keep authentication to one shared team password for now."
  ],
  "risks_or_tradeoffs": [
    "AI sprint report sometimes summarizes story titles correctly but misses blocker notes."
  ],
  "next_sprint_goals": [
    "Fix deployed database persistence.",
    "Add blocker notes to stories and include them in the sprint report prompt.",
    "Improve test coverage for sprint close and carry-over behavior.",
    "Prepare a clean six-minute team workflow app review path."
  ],
  "faculty_feedback_requests": [
    "Should we fix deployment persistence first or spend more time improving the AI sprint report?",
    "Is simplified shared-password access sufficient for the team app review?"
  ],
  "additional_context": "The team wants the report to be concise enough to paste into the shared sprint report slide template."
}
```

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

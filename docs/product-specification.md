# 1. Product vision
CRISP-DM connection: Business Understanding — define the problem, stakeholders, purpose, and measurable success before choosing a technical solution.

## Product Name

CS482 Workflow

## Problem Statement

Student engineering teams need one lightweight workspace for project information that is otherwise scattered across documents and conversations: tasks, sprint plans, blockers, validation evidence, progress, and AI-assisted sprint reports.

## Product Vision

A lightweight engineering-workflow application for CS 482 that helps teams organize projects and tasks, manage sprint work, track simple velocity, and produce AI-assisted sprint reports.

## Intended Users and Stakeholders

| Person or Group | Need or Responsibility | How the App Helps |
| --- | --- | --- |
| CS 482 student engineering teams | Plan tasks, track sprint work, record decisions and blockers, and draft reports | Provides project summaries, a sprint board, sprint history, simple velocity, and editable AI-assisted report drafts. |
| Faculty mentors | Review progress, validation evidence, blockers, and questions | Makes sprint goals, completed work, blockers, evidence, and faculty questions visible in sprint records and reports. |

## Success Criteria

The criteria below are observable and testable.

- [ ] A team can create, edit, and view project summaries and tasks.
- [ ] A current-sprint board shows backlog tasks as well as tasks selected for that sprint in `Backlog`, `Selected for Sprint`, `In Progress`, and `Done` columns.
- [ ] Closing a sprint preserves planned and completed tasks, offers creation of the next sprint, and offers to move unfinished tasks forward.
- [ ] The application shows simple planned work, completed work, and sprint velocity.
- [ ] An AI-generated sprint report draft contains the sprint goal, deliveries and validation evidence, next goals, decisions and blockers, and faculty questions; a student can edit it before use.

# 2. Product research and decisions
CRISP-DM connection: Data Understanding — learn from existing products and inspect the patterns, assumptions, and constraints that shape the problem space.

## Tools Reviewed

| Tool | Pattern Observed | Useful for This App? | Decision or Implication |
| --- | --- | --- | --- |
| [GitHub Projects](https://github.com/features/issues) | Work is displayed as cards in status columns and can retain issue details. | Partly | Adopt the board and task-card patterns. Do not require GitHub integration or automatic status changes. |
| [Jira](https://www.atlassian.com/software/jira) | Tasks can be assigned, planned into sprints, moved between columns, and retained in sprint history. | Yes, with simplification | Adopt assignment, sprint planning, status movement, sprint closing, and simple velocity. Exclude extensive analytics and activity history. |

## Patterns to Adopt

- Display tasks as cards on a board organized by status.
- Show each task's title, owner, and current stage at a glance.
- Record blockers, dependencies, acceptance criteria, definition of done, and validation evidence when useful.
- Keep backlog tasks visible on the current-sprint board; selecting a task for the sprint assigns it to that sprint.
- Preserve sprint history and offer to carry unfinished tasks to the next sprint.

## Patterns to Reject or Simplify

- Do not connect tasks to GitHub issues or use GitHub events to change status automatically.
- Do not include detailed analytics dashboards; use simple velocity based on task count or task points.
- Do not maintain a complete activity log of every change.
- Do not provide multiple task views; the sprint board is the primary view.
- Keep task details visible as text instead of relying mainly on icons and dropdown menus.

## Product Decisions

| Decision | Alternatives Considered | Choice | Reason |
| --- | --- | --- | --- |
| Project structure | One project or multiple projects | Allow users to create multiple projects with a project summary | Teams need independently organized project work. |
| Primary view | Board, list, or interchangeable views | Use one status-based sprint board | A focused board makes task status and sprint selection understandable. |
| Task movement | Manual movement or GitHub automation | Let users move tasks manually | Manual movement meets the workflow need without GitHub integration. |
| Task information | Title only or editable details | Support required title, description, and status plus useful optional planning fields | This keeps cards concise while retaining engineering context. |
| Sprint completion | Delete history, retain unfinished tasks, or offer carry-forward | Preserve closed history and offer to move unfinished tasks to the next sprint | Teams need history and a clear continuation path. |
| Progress reporting | Detailed analytics or simple velocity | Use planned/completed task count or task points | The handout requires simple velocity without a dashboard. |


# 3. MVP scope
CRISP-DM connection: Business Understanding → Data Understanding — decide which needs and product patterns belong in the first version and which do not.

## In Scope

- [x] Projects: create, edit, and view a project summary
- [x] Tasks with title, description, and status
- [x] Optional task owner, priority, blocker/dependency notes, acceptance evidence, task points, acceptance criteria, and definition of done
- [x] Sprint board
- [x] Task status tracking with an extensible workflow
- [x] Sprint lifecycle: create, goal, current sprint, task association, and close
- [x] Sprint reporting with editable AI draft
- [x] Planned work, completed work, and simple velocity
- [x] Persistent project, task, sprint, board, and report data

## Explicitly Out of Scope

- GitHub integration
- Automatic task updates from GitHub
- A complete record of all activity
- Multiple views of tasks

## Deferred or Optional Ideas

- Full user management or production-grade authentication
- Sponsor-facing access
- Advanced workflow customization and analytics dashboards


# 4. Key user workflows
CRISP-DM connection: Business Understanding — describe how a stakeholder will accomplish a meaningful goal and what result would count as success.

Describe the main things a user must be able to accomplish. Each workflow should end with an observable result.

## Workflow 1: Create and View a Project

**Actor:** User

**Starting condition:** The application has opened.

**Steps:**

1. The user creates or opens a project.
2. The user views the project's summary.
3. The user may update the project's information and save it.

**Expected result:** The project is saved, its summary is visible, and it can be opened independently from other projects.

**Failure or edge cases:** A project cannot be saved without a name. Its description is optional.

## Workflow 2: Create and Manage a Task

**Actor:** User

**Starting condition:** The user has opened a project.

**Steps:**

1. The user creates a task with a title, optionally a description, and `Backlog` status.
2. The user may add an owner, priority, blocker or dependency notes, acceptance evidence, task points, acceptance criteria, or definition of done.
3. The user saves the task.
4. The user opens the task later to view or edit its information.

**Expected result:** The task is saved in the selected project and appears in the project backlog.

**Failure or edge cases:** A task cannot be saved without a title and valid status. Its description and all additional planning fields are optional.

## Workflow 3: Plan and Move a Task Through the Sprint Board

**Actor:** User

**Starting condition:** The project contains a task in `Backlog`.

**Steps:**

1. While viewing the current sprint board, the user sees project-backlog tasks in `Backlog` even though they are not assigned to the sprint.
2. The user moves a task from `Backlog` to `Selected for Sprint`; the application assigns it to the displayed sprint.
3. The user moves the task to `In Progress` when work begins.
4. The user moves the task to `Done` when the work is complete.

**Expected result:** The sprint board displays the task in its current status: `Backlog`, `Selected for Sprint`, `In Progress`, or `Done`.

**Failure or edge cases:** Moving a task back to `Backlog` removes it from the active sprint. The workflow is designed to allow additional states later without redesign.

## Workflow 4: Close a Sprint

**Actor:** User

**Starting condition:** A project has a current sprint containing completed or unfinished tasks.

**Steps:**

1. The user closes the current sprint.
2. The application preserves planned and completed task history and calculates planned work, completed work, and simple velocity.
3. The application offers to create the next sprint and move unfinished tasks into it.
4. The user reviews and adjusts the next sprint information and carry-forward choices.

**Expected result:** The closed sprint remains available as history, completed tasks and velocity remain recorded, and the user can carry unfinished tasks into the next sprint.

**Failure or edge cases:** If there are no unfinished tasks, none are offered for carry-forward.

## Workflow 5: Draft and Review a Sprint Report

**Actor:** User

**Starting condition:** A sprint has project, task, and board data; it is normally closed but may be current for a mid-sprint status report.

**Steps:**

1. The user requests a sprint report draft.
2. The application supplies the sprint goal, deliveries and validation evidence, next goals, decisions and blockers, and faculty questions to the AI model.
3. The AI model returns a draft report.
4. The user reviews and edits the draft before saving or using it.

**Expected result:** An editable report draft is associated with the selected sprint.

**Failure or edge cases:** Missing information is identified as missing; the draft must not invent work or claims unsupported by sprint data.

## Workflow Checklist

- [x] Create and view a project
- [x] Create and manage a task
- [x] Select a task for the current sprint
- [x] Move a task through the workflow
- [x] Close a sprint while preserving history
- [x] View planned and completed work
- [x] Generate, review, and edit a sprint report
- [x] View planned work, completed work, and simple velocity

# 5. Functional requirements
CRISP-DM connection: Business Understanding → Modeling — translate stakeholder needs into precise behavior that can later be designed, implemented, and tested.

Write requirements as behavior, not implementation guesses. Use identifiers so tests and API endpoints can refer back to them.

| ID | Requirement | Priority | Related Workflow | Acceptance Evidence |
| --- | --- | --- | --- | --- |
| FR-01 | The application must allow the user to create a project and view its summary. | Must | Workflow 1 | A user can save a project and view its name, description, current sprint, and progress summary. |
| FR-02 | The user must be able to create, edit, open, and view a summary for multiple projects. | Must | Workflow 1 | A newly created project is saved, can be opened independently, and displays its summary. |
| FR-03 | A project must have a name. Its description is optional. | Must | Workflow 1 | A project with a name can be saved; a project without a name cannot be saved. |
| FR-04 | The user must be able to create, view, and edit a task in an opened project. | Must | Workflow 2 | The saved task appears in the selected project, and edits remain visible when it is reopened. |
| FR-05 | A task must have a title and status; description, owner, priority, blocker/dependency notes, acceptance evidence, task points, acceptance criteria, and definition of done are optional. | Must | Workflow 2 | A task missing a required field cannot be saved; optional fields are retained when supplied. |
| FR-06 | A newly created task must begin with the `Backlog` status. | Must | Workflows 2 and 3 | After creation, the task appears in the `Backlog` column. |
| FR-07 | The user must be able to move a task from any status directly to any other status. | Must | Workflow 3 | A task can move among `Backlog`, `Selected for Sprint`, `In Progress`, and `Done` without a required sequence. |
| FR-08 | While viewing a current sprint board, the application must show project-backlog tasks that are not assigned to a sprint. Moving a task from `Backlog` to `Selected for Sprint` must assign it to that sprint. | Must | Workflow 3 | The task appears in the displayed sprint after the move. |
| FR-09 | Moving a task back to `Backlog` must remove it from the active sprint while preserving any closed-sprint history. | Must | Workflow 3 | The task is no longer planned for the active sprint and closed history is unchanged. |
| FR-10 | The application must support creating a sprint, defining its goal, identifying the current sprint, associating tasks and owners with it, and closing it. | Must | Workflow 4 | The current sprint and its goal, tasks, owners, blockers, dependencies, and validation evidence are available. |
| FR-11 | Closing a sprint must preserve planned and completed-task history, calculate planned work, completed work, and simple velocity, and offer to create the next sprint and move unfinished tasks into it. | Must | Workflow 4 | Closed history and velocity remain available; the user can accept or decline each carry-forward option. |
| FR-12 | The application must generate an editable AI-assisted sprint report draft for a closed sprint and may support a current-sprint status report. | Must | Workflow 5 | The draft includes the required report sections and can be edited before it is saved or used. |
| FR-13 | The application must persist project, task, sprint, board, report, and velocity data. | Must | Workflows 1–5 | Saved data remains available after the application is restarted. |

## Workflow Rules

- Projects require a name; descriptions are optional.
- Tasks require a title and status; description and planning details are optional.
- New tasks begin in `Backlog`.
- The sprint-board statuses are `Backlog`, `Selected for Sprint`, `In Progress`, and `Done`.
- Moving `Backlog` → `Selected for Sprint` assigns a task to the displayed sprint; moving to `Backlog` removes it from the active sprint.
- The workflow must permit additional states without major redesign.
- Closing a sprint preserves planned and completed-task history, calculates simple velocity, and offers carry-forward of unfinished tasks.
- AI reports are editable drafts; students remain responsible for their accuracy and final content.

# 6. Domain model

CRISP-DM connection: Data Understanding → Modeling — identify the information the product manages, its relationships, and the rules that govern it.

The model should describe domain objects, relationships, and rules—not just screens.

### Entity: Project
Purpose: Groups tasks, sprints, reports, and team members for one independently managed course project.
Fields:
- id — required, system-generated unique project identifier.
- name — required project name.
- description — optional project description.

Relationships: Has many tasks and sprints.

Rules: A project cannot be saved without a name. Sprints belong to exactly one project.

### Entity: Task
Purpose: Represents a discrete piece of engineering work that can be planned into a sprint and moved across the board.
Fields:
- id — required, system-generated unique task identifier.
- project_id — required reference to the owning project.
- title — required task title.
- description — optional task description.
- assignee_id — optional reference to a project member.
- priority, blocker_notes, dependency_notes, acceptance_evidence, task_points, acceptance_criteria, and definition_of_done — optional planning and validation details.
- status — required current sprint-board status: `Backlog`, `Selected for Sprint`, `In Progress`, or `Done`.

Relationships: Belongs to one project; may be assigned to one user; may appear on a sprint board.
Rules: A task cannot be saved without a title and valid status. New tasks start in `Backlog`. The current status is retained by the sprint board when a sprint closes.

### Entity: Sprint
Purpose: Represents a time-bounded planning period for one project's selected tasks.
Fields:
- id — required, system-generated unique sprint identifier.
- project_id — required reference to the owning project.
- name — required human-readable sprint name.
- goal — optional sprint goal.
- status — required lifecycle state: `Current` or `Closed`.
- start_date — required start date.
- end_date — required end date.
- closed_at — system-recorded close time; empty while the sprint is current.
- planned_work — computed count of planned tasks or sum of their task points.
- completed_work — computed count of `Done` tasks or sum of their completed task points.
- velocity — computed value equal to completed work for the sprint.

Relationships: Belongs to one project; has one sprint board containing its selected tasks; may have one SprintReport draft or final report.

Rules: A project has at most one current sprint. A sprint can close only when it is current. Closing it makes task membership and final-status snapshots immutable, preserves completed work, calculates simple velocity, and offers a next sprint with unfinished tasks available for carry-forward.

### Entity: Sprint Board

Purpose: Represents a sprint's board and the placement of its tasks in the workflow: `Backlog`, `Selected for Sprint`, `In Progress`, and `Done`.
Fields:
- id — required, system-generated unique board-entry identifier.
- sprint_id — required reference to the sprint.
- task_id — required reference to the task.
- status — required board-column status: `Backlog`, `Selected for Sprint`, `In Progress`, or `Done`.
- added_at — system-recorded time that the task was added to the board.
- final_status — task status captured when the sprint closes; empty while the sprint is current.
- carried_forward — computed Boolean indicating that the final status was not `Done` and the task was added to the next sprint's board.
Relationships: Each board entry belongs to one sprint and one task. A task can appear on sprint boards over time, but only once on any given sprint board.
Rules: Project-backlog tasks are visible on the current sprint board but have no active-sprint board entry. Moving `Backlog` → `Selected for Sprint` creates an entry for the displayed sprint; moving a task back to `Backlog` removes its active-sprint entry. Closed-sprint entries are preserved. When a sprint closes, every entry receives a final-status snapshot; unfinished tasks can be added to the next sprint's board. Board statuses are data values so additional workflow states can be added later.

### Entity: SprintReport
Purpose: Stores a user-reviewed AI-assisted report draft or final report for a sprint.

Fields:
- id — required, system-generated unique report identifier.
- sprint_id — required reference to the reported sprint.
- draft_content — optional AI-generated or manually entered report content.
- final_content — optional user-approved report content.
- generation_context — optional snapshot of sprint data supplied to the AI.
- report_type — required value: `Closed Sprint` or `Mid-Sprint Status`.
- sprint_goal, deliveries_and_validation_evidence, next_sprint_goals, key_decisions_and_blockers, and faculty_questions — editable report sections.
- status — required report state: `Draft` or `Final`.
- created_at and updated_at — system-recorded timestamps.

Relationships: Belongs to one sprint; is created from that sprint's goal, sprint-board history, and task details.

Rules: AI output is saved only as a draft and must be reviewable and editable by a student before becoming final. A report must not claim work unsupported by sprint data. Closed-sprint reports are required; current-sprint status reports are optional.

### Entity: User
Purpose: Represents a team member who may be assigned work within a project.
Fields:
- id — required, system-generated unique user identifier.
- display_name — required name shown as an assignee.
- email — optional contact identifier if authentication is later added.

Relationships: May belong to many projects and may be assigned many tasks. Project membership is represented by a ProjectMember association if sharing is implemented.

Rules: Authentication and cross-user sharing are deferred. For the MVP, a user record may be a local project member used only for assignment.

## Domain Rules Resolved

- Required user-entered fields are project name, task title, task status, sprint name, sprint start date, and sprint end date. Project description, task description, task planning details, assignee, sprint goal, and report content are optional.
- Identifiers and timestamps are system-generated. `Sprint Board.carried_forward` is computed from the closed sprint's `final_status` and the next sprint-board entry. Sprint planned work, completed work, and velocity are computed from the sprint-board snapshots using the selected count- or task-point-based measure.
- Current board status is stored on `Task`; a status snapshot is stored on the Sprint Board when its sprint closes.
- A task may appear on multiple sprint boards over time, preserving each sprint's planned work and outcome.
- Closing a sprint snapshots all board-task statuses, preserves the closed sprint, and adds unfinished tasks to the next sprint board.
- An AI-generated report is saved as `SprintReport.draft_content` with its source `generation_context`; it becomes final only after human review.

# 7. API contract
CRISP-DM connection: Modeling — define the executable boundary between the product behavior, backend services, and future implementation.

The backend API will be implemented with FastAPI. For each endpoint, specify the purpose, request, response, validation, errors, and related requirement.

METHOD /path
Purpose:
Related requirement or workflow:

Request body:

{}
Response body:

{}
Validation rules:

Error cases:

Endpoint checklist
[ ] Project endpoints
[ ] Task endpoints
[ ] Sprint endpoints
[ ] Sprint planning and closing endpoints
[ ] Board transition behavior
[ ] AI sprint-report draft endpoint

# 8. AI sprint-report behavior
CRISP-DM connection: Modeling → Evaluation — specify how project data becomes an AI-assisted product behavior and how people will check its quality.

Inputs provided to the model
Output sections
Sprint goal
Completed work
Next sprint goals
Blockers
Faculty notes
Missing or incomplete information
What should the system do when the sprint has no blockers, no faculty notes, incomplete task data, or no completed work?

Human review
Explain how a person reviews and edits the draft before it is saved or used.

AI failure cases to check
[ ] Invented work or unsupported claims
[ ] Missing completed or incomplete work
[ ] Wrong sprint or project context
[ ] Unhelpful output when information is missing

# 9. Non-functional and platform requirements
CRISP-DM connection: Modeling → Deployment — define the operational conditions that allow the system to run, integrate, and remain maintainable.

Document the requirements that affect how the application is built and operated.

[ ] FastAPI backend
[ ] Persistent data storage
[ ] Containerized local execution
[ ] Environment-based configuration
[ ] Automated tests
[ ] Health endpoint
[ ] Version information
[ ] Structured logging
[ ] Engineering documentation
[ ] Course platform AI integration through the approved abstraction
[ ] Authentication decision:
Additional requirements or constraints:

# 10. Risks, assumptions, and open questions
CRISP-DM connection: Business Understanding → Evaluation — make uncertainty visible so it can be investigated rather than silently embedded in the implementation.

Type	Statement	Impact	Next action or owner
Assumption			
Risk			
Open question

# 11. Initial validation plan
CRISP-DM connection: Evaluation — decide what evidence will show that the product behavior and engineering claims are credible.

Requirement or workflow	Test or evidence	Expected result
Identify the first behavior you will implement and verify in Class 5.

First implementation slice:
Why this slice:

# 12. Decision log
CRISP-DM connection: Improve — preserve the reasoning behind changes so later iterations can build on evidence instead of repeating old uncertainty.

Link significant decisions to ADRs or record them briefly here.

ID	Decision	Alternatives	Reason	Consequence
ADR-001				
AI review prompt
AI review prompt — remove this section before submitting C06.

After drafting this specification, ask an AI assistant to review it:

Review this product specification for an Engineering Workflow application.
Check whether it clearly supports projects, tasks, sprint board behavior,
sprint lifecycle, sprint reporting, velocity tracking, and FastAPI implementation.
Identify vague requirements, missing workflows, unclear domain relationships,
contradictory rules, missing validation or error cases, and endpoint gaps.
Do not rewrite the specification. Give specific review comments and identify
which questions require a human product or engineering decision.
You remain responsible for resolving the comments and approving the final specification.

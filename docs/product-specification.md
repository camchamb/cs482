# 1. Product vision
CRISP-DM connection: Business Understanding — define the problem, stakeholders, purpose, and measurable success before choosing a technical solution.

## Product Name

CS482 Workflow

## Problem Statement

Students need a simple way to track project tasks across sprint stages, see what still needs work, and preserve sprint progress without relying on heavyweight tools or GitHub integrations that are unnecessary for the CS 482 MVP.

## Product Vision

A lightweight sprint-management application for CS 482 that helps teams organize tasks across multiple projects, move work through a clear board workflow, and close sprints with persistent history.

## Intended Users and Stakeholders

| Person or Group | Need or Responsibility | How the App Helps |
| --- | --- | --- |
| CS 482 student team members | Create tasks, track task status, and manage sprint work | Provides a board with task status, notes, and descriptions so team members can see what to work on and what stage each task is in. |
| Project teams | Coordinate shared sprint progress and close sprints cleanly | Keeps sprint tasks in one place, supports moving tasks through workflow stages, and preserves data when a sprint closes. |
| Course staff or instructors | Review evidence of project progress and sprint outcomes | Makes project work and sprint status visible through persistent task and sprint records. |

## Success Criteria

The criteria below are observable and testable.

- [ ] A team can create tasks with a title, description, and notes, then move them between workflow statuses on a sprint board.
- [ ] A user can create and open multiple projects, with an existing project available when the application starts.
- [ ] The current board clearly shows which tasks still need work and what status each task is in.
- [ ] Closing a sprint preserves the sprint's task information so the team can review completed and incomplete work later.

# 2. Product research and decisions
CRISP-DM connection: Data Understanding — learn from existing products and inspect the patterns, assumptions, and constraints that shape the problem space.

## Tools Reviewed

| Tool | Pattern Observed | Useful for This App? | Decision or Implication |
| --- | --- | --- | --- |
| [GitHub Projects](https://github.com/features/issues) | Work is displayed as task cards in status columns. Cards can contain titles, descriptions, and issue details, and automation can move them when linked work changes. | Partly | Adopt the board, task-card, and status-column patterns. Do not require GitHub integration or automatic status changes. |
| [Jira](https://www.atlassian.com/software/jira) | Tasks can be assigned, dragged between status columns, associated with a sprint, and opened to edit details. When a sprint closes, unfinished tasks can move to another sprint. | Yes, with simplification | Adopt task assignment, drag-and-drop status changes, editable details, and sprint closing. Exclude Jira's extensive metrics, activity history, and alternate views from the MVP. |

## Patterns to Adopt

- Display current work as task cards on a board organized by status.
- Show each task's title and current stage at a glance.
- Allow users to open a task to view and edit its description, notes, decisions, and assignment.
- Allow tasks to move between statuses as work progresses.
- Preserve unfinished work when a sprint closes so it can be carried into a later sprint.

## Patterns to Reject or Simplify

- Do not connect tasks to GitHub issues or use GitHub events to change task status automatically.
- Do not include detailed sprint statistics, insights, or velocity metrics in the MVP.
- Do not maintain a complete activity log of every change.
- Do not provide multiple task views; the sprint board is the primary view.
- Keep task details visible as text instead of relying mainly on icons and dropdown menus.

## Product Decisions

| Decision | Alternatives Considered | Choice | Reason |
| --- | --- | --- | --- |
| Project structure | Limit the application to one project or allow multiple projects | Start with an existing project and allow users to create additional projects | Users need to keep the tasks and sprints for separate projects organized independently. |
| Primary task view | Board, list, or multiple interchangeable views | Use one status-based sprint board | Both reviewed tools make work and task status easy to understand through columns, while one view keeps the MVP focused. |
| Task movement | Manual movement or automatic updates from GitHub | Let users move tasks between statuses manually | Manual movement provides the needed workflow without adding GitHub integration. |
| Task information | Title only, summary fields on every card, or editable task details | Show a concise card and provide editable descriptions, notes, decisions, and assignments | This keeps the board readable while retaining the context the team needs. |
| Sprint completion | Delete the board, leave unfinished tasks in a closed sprint, or carry them forward | Preserve the closed sprint and allow unfinished tasks to move to a later sprint | Teams need both historical sprint information and a clear way to continue incomplete work. |
| Progress reporting | Detailed metrics and activity history or basic board status | Use board status as the MVP's progress indicator | The research identified status visibility as useful, but extensive statistics and activity records as unnecessary. |


# 3. MVP scope
CRISP-DM connection: Business Understanding → Data Understanding — decide which needs and product patterns belong in the first version and which do not.

## In Scope

- [x] Multiple projects, with an existing project available when the application starts
- [x] Tasks or ToDos
- [x] Task titles, descriptions, and notes
- [x] Assignment of tasks to team members
- [x] Sprint board
- [x] Task status tracking
- [x] Sprint lifecycle, including closing sprints
- [x] Persistent project, task, and sprint data

## Explicitly Out of Scope

- GitHub integration
- Automatic task updates from GitHub
- A complete record of all activity
- Multiple views of tasks

## Deferred or Optional Ideas

- Sharing data between people
- AI-generated sprint reports
- Sprint statistics and velocity or progress metrics


# 4. Key user workflows
CRISP-DM connection: Business Understanding — describe how a stakeholder will accomplish a meaningful goal and what result would count as success.

Describe the main things a user must be able to accomplish. Each workflow should end with an observable result.

## Workflow 1: Create and View a Project

**Actor:** User

**Starting condition:** The application has opened with an existing project available.

**Steps:**

1. The user views the existing project.
2. The user may update the project's information and save it.
3. The user may creates a new project.

**Expected result:** The new project is saved and can be opened independently from the existing project.

**Failure or edge cases:** Required project fields and validation rules have not yet been defined.

## Workflow 2: Create and Manage a Task

**Actor:** User

**Starting condition:** The user has opened a project.

**Steps:**

1. The user may creates a task with a title, optionally a description and notes.
2. The user may assign the task to a team member.
3. The user saves the task.
4. The user opens the task later to view or edit its information.

**Expected result:** The task is saved in the selected project, assigned to the selected team member, and begins in `To Do`.

**Failure or edge cases:** Required task fields and validation rules have not yet been defined.

## Workflow 3: Move a Task Through the Sprint Board

**Actor:** User

**Starting condition:** The project contains a task in `To Do`.

**Steps:**

1. The user may move the task from `To Do` to `In progress` when work begins.
2. The user may move the task to `In Review` when it is ready for review.
3. The user may move the task to `Done` when review is complete.

**Expected result:** The sprint board displays the task in its current status: `To Do`, `In progress`, `In Review`, or `Done`.

**Failure or edge cases:** Rules for moving a task backward to an earlier status have not yet been defined.

## Workflow 4: Close a Sprint

**Actor:** User

**Starting condition:** A project has a current sprint containing completed or unfinished tasks.

**Steps:**

1. The user closes the current sprint.
2. The application preserves the sprint's planned and completed task history.
3. The application automatically moves unfinished tasks to the next sprint.

**Expected result:** The closed sprint remains available as history, completed tasks remain recorded in it, and unfinished tasks appear in the next sprint.

**Failure or edge cases:** If there are no unfinished tasks, no tasks are carried into the next sprint.

## Workflow Checklist

- [x] Create and view a project
- [x] Create and manage a task
- [x] Select a task for the current sprint
- [x] Move a task through the workflow
- [x] Close a sprint while preserving history
- [x] View planned and completed work
- [ ] Generate, review, and edit a sprint report (deferred from the MVP)

# 5. Functional requirements
CRISP-DM connection: Business Understanding → Modeling — translate stakeholder needs into precise behavior that can later be designed, implemented, and tested.

Write requirements as behavior, not implementation guesses. Use identifiers so tests and API endpoints can refer back to them.

ID	Requirement	Priority	Related workflow	Acceptance evidence
FR-01		Must		
FR-02		Must		
FR-03		Should		
Workflow rules
Document rules that an assistant might otherwise invent.

Tasks begin in To Do.
The task statuses are To Do, In progress, In Review, and Done.
Closing a sprint preserves its planned and completed task history.
Unfinished tasks move to the next sprint automatically when the current sprint closes.
Additional rules:

# 6. Domain model

CRISP-DM connection: Data Understanding → Modeling — identify the information the product manages, its relationships, and the rules that govern it.

The model should describe domain objects, relationships, and rules—not just screens.

Entity: Project
Purpose:
Fields:
- id —
- name —
- description —

Relationships:
Rules: Has sprints

Entity: Task
Purpose:
Fields:
- id —
- project_id —
- title —
- description —
- status —

Relationships:
Rules:

Entity: Sprint
Purpose:
Fields:
- id —
- project_id —
- goal —
- status —
- start
- end

Relationships:
Rules: Has Stories

Entity: SprintStory or equivalent association
Purpose:
Fields:
Relationships:
Rules:

Entity: SprintReport
Purpose:
Fields:
Relationships:
Rules:


OTHERS:
user
status?



Domain questions to resolve
What fields are required versus optional?
Which fields are computed?
Where is story status stored?
Can a story belong to more than one sprint over time?
What happens to unfinished stories when a sprint closes?
Where is an AI-generated report draft saved?

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
[ ] User story endpoints
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
What should the system do when the sprint has no blockers, no faculty notes, incomplete story data, or no completed work?

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
Check whether it clearly supports projects, user stories, sprint board behavior,
sprint lifecycle, sprint reporting, velocity tracking, and FastAPI implementation.
Identify vague requirements, missing workflows, unclear domain relationships,
contradictory rules, missing validation or error cases, and endpoint gaps.
Do not rewrite the specification. Give specific review comments and identify
which questions require a human product or engineering decision.
You remain responsible for resolving the comments and approving the final specification.

# Engineering Workflow Application Project Handout

> **Artifact type:** Student-facing project handout  
> **Project phase:** Individual AI Engineering Apprenticeship

## Purpose

The Engineering Workflow Application is the common project for the first apprenticeship block of CS 482. It gives every student a realistic AI engineering problem before team specialization begins.

The goal is not to build a commercial project management clone. The goal is to build a small, coherent engineering workflow tool that develops professional AI engineering habits.

## Product Vision

Engineering teams create and coordinate information while building software: requirements, user stories, sprint plans, engineering decisions, blockers, progress reports, and feedback. That information often becomes scattered across documents, repositories, and conversations.

The Engineering Workflow Application provides a lightweight workspace for organizing project work and producing AI-assisted sprint reports.

## Intended Users

- Student engineering teams
- Faculty mentors

Sponsor access is not required for the initial project.

## Required Product Capabilities

### Projects

The application supports:

- creating projects;
- editing project information;
- viewing a project summary.

### User Stories

Each story supports:

- title;
- description;
- status.

Stories may also support owner, priority, blocker or dependency notes, acceptance evidence, story points, acceptance criteria, and definition of done if those details help the team manage work.

### Sprint Board

Stories move through a basic workflow:

- Backlog;
- Selected for Sprint;
- In Progress;
- Done.

The workflow should be designed so additional states can be added without major redesign.

The application must connect stories to sprints so the team can tell which stories were planned for a sprint and which stories were completed during that sprint.

When viewing the board for the current sprint, the backlog should still show project backlog stories that are not assigned to a sprint. Moving a story from Backlog to Selected for Sprint assigns it to the displayed sprint.

Moving a story back to Backlog should remove it from the active sprint while preserving history for closed sprints.

### Sprints

The application supports a basic sprint lifecycle:

- create a sprint;
- define a sprint goal;
- identify the current sprint;
- associate stories with a sprint;
- assign story owners;
- record blockers, dependencies, and validation evidence;
- close a sprint.

When a sprint is closed, the application preserves which stories were completed. It should also offer to create the next sprint and move unfinished stories into it.

### Sprint Reporting

The application assists with sprint report drafting. An AI model drafts:

- sprint goal;
- deliveries and validation evidence;
- next sprint goals;
- key decisions and blockers;
- faculty questions or requests.

Students remain responsible for reviewing and editing AI-generated report drafts.

Sprint reports are usually drafted for closed sprints, but the app may also support a mid-sprint status report for the current sprint.

### Velocity Tracking

The application supports:

- planned work;
- completed work;
- simple sprint velocity.

The progress representation can be simple for the MVP.

Velocity may be based on story counts or story points.

## Engineering Expectations

The project should demonstrate:

- requirements grounded in stakeholder needs;
- domain modeling;
- FastAPI backend API design;
- frontend/backend integration;
- persistence;
- responsible AI collaboration;
- AI-enabled product behavior;
- validation evidence;
- engineering documentation;
- ADRs or decision logs;
- repeatable local execution.

For the common course project, implement the backend API with FastAPI.

If the deployed app stores data that should survive redeploys, that data must be written to a path backed by a named volume in docker-compose.yml. Data written only to the container filesystem may be lost when the container is replaced.

Authentication is optional for the individual local version. If included, it should remain limited to simple shared-password access. Full user management is outside the expected individual project scope.

## Out of Scope

The project is not intended to compete with mature tools such as Jira, Azure DevOps, GitHub Projects, Linear, Trello, Asana, or ClickUp.

Out-of-scope capabilities may include:

- complex permissions;
- full multi-tenant administration;
- production-grade authentication;
- sponsor-facing access;
- meeting transcription;
- RAG over project history;
- complete analytics dashboard;
- advanced workflow customization.

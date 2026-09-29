- Team name: The Quinnovators  
- Report date: Oct 29  
- Sprint Goal: Build a usable team version of the workflow app with sprint planning and AI report drafting.  
- Velocity Trend:  
  Sprint N (Sprint 3): Planned 5, Completed N/A, Percentage N/A  
  Sprint N-1 (Sprint 2): Planned 10, Completed 7, Percentage 70%  
  Sprint N-2 (Sprint 1): Planned 8, Completed 5, Percentage 63%  
- Sprint Deliveries & Validation:  
  • Create persistent project storage (Sam): Validated by creating, editing, and reloading three projects after restarting the backend process.  
  • Support backlog and sprint-assigned story views (Leo): Validated by verifying unassigned stories appeared in backlog while sprint-assigned stories appeared on the sprint board.  
  • Support closing active sprint while preserving completed story history (Maya): Validated by closing Sprint 2 through the app and confirming completed stories remained attached to the closed sprint history view.  
- Key Decisions / Blockers:  
  • Authentication will use one shared team password for now.  
  • SQLite data is not persisting after deployment because the database file is outside the named volume path.  
  • Missing faculty feedback and next sprint goals (report notes contain draft content, but faculty feedback and next sprint goals are not confirmed final).  
- Next Sprint Goals: Missing from provided context.  
- Faculty Feedback / Requests: Should deployment persistence be fixed before improving the AI sprint report?
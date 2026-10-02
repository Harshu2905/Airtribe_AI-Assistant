# Fernlane Changelog

## 4.21.0 — 2026-09-24
### Fixed
- Comments: @mentions of users with apostrophes in their name now notify correctly.
- Mobile (iOS): board no longer scrolls to top after editing a card.
### Known issues
- KI-131: Board CSV export stops at 10,000 rows; larger boards are silently truncated. Workaround: export by filtered view (e.g. per status). Fix scheduled for 4.22.
- KI-129: Slack unfurl shows "Private task" for tasks in public boards when the board was moved between workspaces. Workaround: re-share board link.

## 4.20.0 — 2026-09-10
### Added
- Timeline view: drag to change dependency lag.
### Fixed
- Jira sync: duplicate tasks created after a Jira field-mapping change (ENG-4412).
- Automations: "due date passed" trigger fired twice for recurring tasks.
### Known issues
- KI-127: Google Calendar two-way sync can lag up to 30 minutes for events edited on mobile.

## 4.19.0 — 2026-08-27
### Fixed
- SSO (Okta): users removed from the Okta group were not deprovisioned until next login.

## 4.18.0 — 2026-08-13
### Fixed
- Timeline view: due dates displayed one day early for users in US time zones during the March/November daylight-saving transition week.
- API: `GET /v2/tasks` pagination cursor expired after 60 seconds instead of 10 minutes.

## 4.17.0 — 2026-07-30
### Known issues (resolved in 4.19)
- KI-118: Okta SCIM deprovisioning delay.

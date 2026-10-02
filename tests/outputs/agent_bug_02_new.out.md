**Verdict:** NEW BUG

**Searches run:** "timeline"; "time ?zone|UTC|off.by.one|one day|day earlier|IST|Kolkata"; "due date|gantt|wrong date|date shift"; then a full read of the changelog (4.17.0–4.21.0).

### Title
Timeline view: due dates render one day early for Asia/Kolkata (UTC+5:30) users

### Severity
**S3.** Display is wrong in one view, and the List view and task panel show the correct data. It affects every board for this user and misleads scheduling, so it needs a prompt fix but doesn't lose data.

### Environment
- Fernlane web app 4.21.0, Team plan
- Chrome 129, Windows 11
- Account time zone Asia/Kolkata (UTC+5:30, no DST), user in Pune, India
- A colleague in London on the same board sees correct dates.

### Steps to reproduce
Only what the report supports:
1. Set the account time zone to Asia/Kolkata.
2. Open a board containing a task with a due date, e.g. "Vendor contract" due 10 Oct.
3. Open the task panel and note the due date.
4. Open the Timeline view and note the date where the task bar ends.
5. Compare with the List view.

I could not reproduce this myself. These steps are inferred from the report.

### Expected result
The Timeline bar ends on 10 Oct, matching the task panel and List view.

### Actual result
The Timeline bar ends on 9 Oct. The task panel and List view show 10 Oct. It happens on every board the customer checked, and the same board looks correct for a London user.

### Customer impact
- Riya's team in India sees every task's end date a day early on the Timeline, so they may plan or report against the wrong deadlines.
- It started "last week", which is roughly 4.21.0 (released 2026-09-24), but this isn't confirmed.
- No workaround is known except using the List view or task panel for dates.

### Similar but different
- **4.18.0 (2026-08-13), Timeline due dates one day early.** This is the closest match, and the symptom is the same. It is not a match because it was scoped to US time zones during the March/November DST transition week. Riya is in Asia/Kolkata, which has no DST, and the date is 2 October. If the same date-conversion code is involved, this may be a regression or an incomplete fix, so engineering should check.
- **4.20.0, Timeline drag to change dependency lag.** This is a recent Timeline change that could affect date rendering, but nothing in the entry mentions due dates. It is a lead, not a match.
- **4.20.0, Automations "due date passed" trigger firing twice.** Different feature and symptom.
- **KI-131, KI-129 and KI-127.** CSV export, Slack unfurl and Google Calendar sync. Unrelated.

### Unknowns to confirm with customer
- The exact date the problem started, and whether it began right after an upgrade to 4.21.0 or 4.20.0. The report only says "last week".
- Whether it also happens in other browsers or on other devices.
- Whether Riya's browser or OS time zone differs from the account time zone (Asia/Kolkata).
- Whether any other colleagues in non-UTC or positive-offset time zones are affected, or only Riya. Also, which time zone the London colleague uses.
- Whether the error is always exactly one day, including for tasks with a due time set, or only for tasks with date-only due dates.
- Whether the task start dates, or only the end/due date, are shifted.
- Whether changing the account time zone, for example to UTC, changes what the Timeline shows.
- A screenshot of the Timeline bar next to the task panel for "Vendor contract".

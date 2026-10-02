**Verdict:** KNOWN ISSUE

**Searches run:** `export|CSV|download`; `10,?000|row limit|truncat|missing rows|cap`; `KI-\d+` (to list all open known issues and rule out others). I also read the 4.21.0 release section.

**Matching entry:** KI-131, release 4.21.0 (2026-09-24). It is listed under Known issues for the version the customer is on.

**Why it matches:**
- **Symptom:** KI-131 says the board CSV export stops at 10,000 rows and larger boards are silently truncated. Leo's board has about 14,200 cards and the CSV has exactly 10,000 rows, with no error.
- **Conditions:** The customer is on 4.21.0, the release where KI-131 is listed. The entry doesn't restrict by plan or platform, so the Business plan doesn't change the match.
- **Fix status:** The fix is scheduled for 4.22. The changelog has no 4.22 entry yet, so it isn't released. I can't see a release date.

**Workaround to send the customer (needed by Friday):**
1. Export by filtered view instead of the whole board, for example one export per status.
2. Keep each filtered export under 10,000 rows. The 14,200 cards then split across several files.
3. Check the combined row count against the 14,200 card count on the board. Truncation is silent, so a total that doesn't match means one filter is still too large.
4. Merge the files for the audit.
5. If a single status holds more than 10,000 cards, add a second filter such as created date or assignee.

**Notes for the reply:**
- Tell Leo the truncation is a confirmed limitation and not something he did wrong.
- Don't promise 4.22 before Friday, because the changelog gives no date. If the audit needs the full board in one file, ask engineering for a 4.22 ETA or a manual export.
- **Unconfirmed:** whether the "All Support Requests" board's filtered views can be split cleanly under 10,000 rows each. Ask Leo how the cards are distributed across statuses.

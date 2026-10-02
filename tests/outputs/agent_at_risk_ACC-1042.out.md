# Retention briefing: Northwind Logistics (ACC-1042)
**Plan / seats / MRR / renewal:** Business, annual, 38 seats, $1,710 MRR, renews 2026-11-30, which is 59 days from today (all from Billing). **Risk level:** High. A cancellation-category ticket is open, Jira is disconnected, and seats and usage are both down by more than half.

## What's happening
- **Seats and revenue are shrinking.** Seats went 60 → 48 → 38 (-36.7%), and MRR went $2,700 → $1,710 (Billing).
- **Usage is falling steadily.** WAU went 51 → 24 (-52.9%) and tasks created went 4,100 → 1,650 (-59.8%), from the week of 07-06 to the week of 09-21 (Usage). Jira sync events went 410 → 8 (-98%) (Usage).
- **The admin is looking at leaving.** Dana Okafor's open ticket T-89410 (09-25) asks about data at non-renewal and CSV export of all boards. It also mentions evaluating "other tools" (Tickets).

## The timeline
- 2025-11-30 [Billing]: Annual renewal paid, 60 seats, $32,400.
- 2026-06-02 [Billing]: Seats cut 60 → 48.
- 2026-07-24 [Tickets]: T-88120, Jira sync duplicating issues. CSAT 2. The workaround took the team a day.
- 2026-07-27 [Usage]: Jira sync events drop 380 → 120 in one week. WAU is 44.
- 2026-08-12 [Tickets]: T-88544, duplicates recurred. Bug ENG-4412 opened. CSAT 1.
- 2026-08-19 [Billing]: Seats cut 48 → 38.
- 2026-08-21 [Usage/Tickets]: Dana Okafor disconnects Jira. The drop-off list also shows timeline_view and automations (Usage).
- 2026-08-28 [Tickets]: T-89002, outage credit request for August uptime of 99.1%.
- 2026-09-03 [Billing]: Add-on invoice card declined, $1,710. Retried OK on 09-06.
- 2026-09-22 [Billing/Tickets]: Outage credit of $171 applied. It took 25 days and the customer chased twice. CSAT 3.
- 2026-09-24 [Usage]: Last admin login.
- 2026-09-25 [Tickets]: T-89410 opened (cancellation / data export). Still open.

## Root cause (Likely)
- Likely: The unresolved Jira sync bug drove the churn signals. Jira activity fell right after T-88120 opened. Duplicates recurred, Jira was disconnected on 08-21, and dependent features (timeline, automations) were dropped.
- Likely: The slow outage credit added to the frustration. It took 25 days and two chases.
- Fact: The 06-02 seat cut came before any Jira ticket. It can't be explained by Jira, and the reason is unknown.

## Open issues to resolve before or on the call
- T-89410 is unanswered in the export. Check whether Dana got a reply on data retention and CSV export.
- Get the status of ENG-4412 and whether Jira can be safely reconnected.
- Find out why the 09-03 card was declined (the retry succeeded).

## Talking points for the call
1. Acknowledge the Jira problems directly. There were two tickets with CSAT 2 and 1, and the workaround cost the team a day.
2. Ask what Northwind needs from a tool, and which "other tools" they're evaluating (T-89410).
3. Give a status on ENG-4412 only if it is confirmed beforehand. Don't state a fix date unless Engineering gives one.
4. Acknowledge that the credit took 25 days. Offer to answer the data export question.
5. Consider asking Finance about options for the 38-seat renewal. Make no promises.

## Don't say / avoid
- Don't promise discounts, credits, refunds or a fix date.
- Don't suggest the declined card was a customer failing. It was retried OK.
- Don't assume Dana is the decision-maker without checking.

## Data gaps
- Usage data ends at the week of 09-21, so there is no data for the last ~10 days.
- Usage has only one admin login value (09-24).
- Billing has no reason codes for the seat reductions.
- The seat credits of $5,400 and $4,500 imply $450 per seat, but MRR implies $45 per seat per month ($540 per year). This doesn't reconcile.
- The 09-03 failed payment of $1,710 is described as an "add-on invoice", but no add-on appears in the plan.
- ENG-4412 status isn't in the exports.
- I have no contact data apart from Dana Okafor's name in the tickets.

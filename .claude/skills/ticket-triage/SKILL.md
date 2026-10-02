---
name: ticket-triage
description: Categorize, prioritize and route a single new Fernlane support ticket, and force immediate escalation for live outages or legal/security keywords. Use whenever a new ticket or inbound support email needs to be triaged or routed.
---

# Ticket triage

Triage ONE ticket into a fixed taxonomy and a routing decision. This is a single-pass
judgment; do not research the customer, reply to them, or open other systems.

## Inputs
- The ticket: subject + body (+ plan tier if known). It may be pasted text or a file path.

## Procedure

1. **Run the escalation pre-check first, before reading for meaning.**
   Save the ticket text to `scratch/ticket.txt` if it isn't already a file, then run:
   `python3 .claude/skills/ticket-triage/scripts/escalation_check.py <ticket-file>`
   - If `escalate_now` is true, the ticket MUST be escalated. You may not override this
     to false, even if the match looks incidental. (False positives cost one page; false
     negatives cost an incident.)
   - The script is a floor, not a ceiling: if the ticket clearly describes a live outage or a
     legal/security matter in words the script missed, escalate it too and say why.

2. **Classify** using `routing_table.md` (in this skill's folder). Pick exactly one primary
   `category` from the table, plus an optional `secondary_category` when a second one
   genuinely applies (e.g. a billing complaint that is also a cancellation signal).
   If escalated, the primary category is `outage` or `legal_security`.

3. **Prioritize**: start at the category's default priority, then apply the table's
   adjustments (Business/Enterprise plan +1; blocked production or same/next-day deadline +1).
   Escalated tickets are always P1.

4. **Route** to the queue in the table for the primary category.

5. **Output exactly this JSON** and nothing else (no prose before or after):

```json
{
  "ticket_id": "<id or null>",
  "escalate_now": true,
  "escalation_reason": "<why, citing matched terms; null if not escalated>",
  "matched_terms": {"legal_security": ["..."]},
  "category": "<one category>",
  "secondary_category": "<category or null>",
  "queue": "<queue from table>",
  "priority": "P1|P2|P3|P4",
  "priority_reasoning": "<default + which adjustments applied>",
  "summary": "<one sentence a human can act on>",
  "confidence": "high|medium|low"
}
```

## Rules
- Never invent categories or queues outside the table.
- Use `confidence: low` when the ticket is too vague to classify; route it to the default
  queue for the best guess and say what's missing in `summary`.
- Don't reply to the customer or suggest fixes; that is a different capability.

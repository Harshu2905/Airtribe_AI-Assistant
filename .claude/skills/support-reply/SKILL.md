---
name: support-reply
description: Draft an outbound customer support reply in Fernlane's tone of voice, grounded only in the CURRENT refund & pricing policy doc, and verify it with a figure/tone checker before returning it. Use whenever a reply to a customer ticket or email needs to be written.
---

# Support reply

Write ONE customer-facing reply that (a) sounds like Fernlane and (b) never states a refund or
pricing figure that isn't in the current policy doc.

## Sources (read fresh EVERY time; never rely on memory or a previous run)
- Tone guide: `data/tone_guide.md`
- Refund & pricing policy (changes often): `data/policy/refund_pricing_policy.md`
  Note its `Version:` line; you will report it.

Do not copy figures into this skill or your notes. The policy doc is the only source of truth,
which is why it is read at run time and not baked in here.

## Inputs
- The customer's ticket text (required).
- Optional: agent first name for the sign-off (default "Sam"), and any facts from the account
  record that the caller supplies.

## Procedure
1. Read both source docs.
2. Work out the answer from the policy:
   - If the policy gives a figure that applies, you may quote it exactly.
   - If the answer needs a number the policy doesn't give (e.g. an exact prorated refund, a custom
     discount, Enterprise pricing), **do not calculate or estimate it**. State the rule in words
     and say who will confirm the exact amount and when ("Billing will confirm the exact amount
     within 1 business day" is NOT allowed unless that timeframe is in the policy; say
     "Billing will confirm the exact amount and reply on this thread").
   - You may echo an amount the customer themselves quoted (their own charge).
3. Draft the reply following every rule in the tone guide.
4. Save the draft to `scratch/draft.txt` (and the ticket to `scratch/ticket.txt` if it isn't already a file), then run the checker:
   `python3 .claude/skills/support-reply/scripts/check_reply.py --draft <draft> --policy data/policy/refund_pricing_policy.md --tone data/tone_guide.md --ticket <ticket-file>`
5. If the result is FAIL, fix every violation (remove or replace the figure with the policy rule
   in words; rephrase banned phrases) and re-run until it PASSES. Review any `style_warnings`.
   Never return a draft that failed the checker.
6. Return, in this order:
   - `### Reply` then the final reply text exactly as it should be sent.
   - `### Checks` then: policy version checked, checker result, and a one-line note of any figure
     you deliberately left out and why.

## Never
- Promise a refund, credit, discount or timeline the policy doesn't contain.
- Mention internal queues, ticket IDs, or "the policy says"; explain in plain words instead.

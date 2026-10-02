```json
{
  "ticket_id": "T-90231",
  "escalate_now": true,
  "escalation_reason": "Pre-check matched 'security issue'. The ticket also describes a likely cross-tenant data exposure: changing the number in a public share link URL shows boards from another company's workspace. That is a vulnerability report.",
  "matched_terms": {"legal_security": ["security issue"]},
  "category": "legal_security",
  "secondary_category": "billing",
  "queue": "Security & Legal (page on-call)",
  "priority": "P1",
  "priority_reasoning": "Escalated tickets are always P1. The Team plan gets no uplift. The billing seat-refund request is secondary and does not affect priority.",
  "summary": "Page security on-call now: a public share link appears to be enumerable by changing the URL ID, exposing another company's boards. Separately, route the 15-vs-11 seat overcharge refund to Billing.",
  "confidence": "high"
}
```

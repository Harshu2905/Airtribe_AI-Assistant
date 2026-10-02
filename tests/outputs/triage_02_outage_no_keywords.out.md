```json
{
  "ticket_id": "T-90240",
  "escalate_now": true,
  "escalation_reason": "The script missed this one (no keyword match), but the ticket describes a live outage. All 200 staff cannot open any board since about 9:10 this morning. The spinner never finishes, on Chrome and Edge, on both office and home networks. That points to a service-side failure, not a local problem. The customer runs live clinic schedules on Fernlane.",
  "matched_terms": {"outage": ["none from the script; judged manually: 'nothing loads', 'None of our 200 staff', 'since about 9:10 this morning', 'office and home networks'"]},
  "category": "outage",
  "secondary_category": null,
  "queue": "Incident Response (page on-call)",
  "priority": "P1",
  "priority_reasoning": "Escalated tickets are always P1. The outage default is already P1, and the Business plan and blocked-production adjustments cannot raise it further.",
  "summary": "Page Incident Response now: Harbor Health (Business plan, 200 users, clinic scheduling) reports no boards loading for any user since about 9:10 this morning, across browsers and networks. Check whether a wider Fernlane outage is under way.",
  "confidence": "high"
}
```

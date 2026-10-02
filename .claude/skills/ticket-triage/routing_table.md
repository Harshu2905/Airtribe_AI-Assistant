# Fernlane Ticket Categories and Routing

| Category | Covers | Route to queue | Default priority |
|---|---|---|---|
| billing | charges, invoices, refunds, plan changes, seats | Billing | P3 |
| account_access | login, SSO, 2FA, password, locked accounts | Account Support | P2 |
| bug | something behaves wrongly or errors | Product Support | P3 |
| how_to | usage questions, configuration, best practice | Product Support | P4 |
| feature_request | asks for something the product doesn't do | Product (feedback inbox) | P4 |
| integrations | Slack, Jira, GitHub, Google, API, webhooks | Integrations | P3 |
| cancellation | wants to cancel or downgrade, churn signals | Retention | P2 |
| outage | product down / unavailable for many users | Incident Response (page on-call) | P1 |
| legal_security | legal threats, GDPR/DPA, breach, vulnerability, subpoena | Security & Legal (page on-call) | P1 |

## Escalation rule
Outage and legal_security are never queued. They page the on-call owner immediately,
regardless of what other category the ticket also fits.

## Priority adjustments
- Enterprise or Business plan customer: raise one level (e.g. P3 → P2), never above P1.
- Customer says a deadline is today/tomorrow or production is blocked: raise one level.

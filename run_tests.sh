#!/usr/bin/env bash
# Re-runs every standalone test. Each skill/agent is invoked on its own; nothing is chained.
set -u
cd "$(dirname "$0")"
OUT=tests/outputs
mkdir -p "$OUT" scratch

for n in 01_hidden_security 02_outage_no_keywords 03_routine; do
  echo "skill ticket-triage <- triage_$n"
  claude -p "/ticket-triage tests/inputs/triage_$n.txt" < /dev/null > "$OUT/triage_$n.out.md"
done

echo "skill support-reply <- reply_01_refund_discount"
claude -p "/support-reply tests/inputs/reply_01_refund_discount.txt  (agent name: Sam)" < /dev/null > "$OUT/reply_01_refund_discount.out.md"

echo "agent at-risk-briefing <- ACC-1042"
claude -p --agent at-risk-briefing "Prepare the retention briefing for account ACC-1042. Today's date is 2026-10-02." < /dev/null > "$OUT/agent_at_risk_ACC-1042.out.md"

for n in 01_known 02_new; do
  echo "agent bug-report-checker <- bug_$n"
  claude -p --agent bug-report-checker "Customer bug report: $(cat tests/inputs/bug_$n.txt)" < /dev/null > "$OUT/agent_bug_$n.out.md"
done

echo "Done. Outputs in $OUT/"

# Fernlane Support AI: Skills & Agents

Two Claude Code **skills**, two Claude Code **agents**, and one capability deliberately left as **neither**.
All of them work standalone. There is no orchestration or wiring between them.

| # | Capability | Decision | Built as |
|---|---|---|---|
| 1 | Ticket triage, routing, immediate escalation | Skill | `.claude/skills/ticket-triage/` |
| 2 | On-tone replies that never state an off-policy figure | Skill | `.claude/skills/support-reply/` |
| 3 | At-risk account briefing from 3 systems | Agent | `.claude/agents/at-risk-briefing.md` |
| 4 | Weekly QA grading of closed tickets | Neither | (scheduled report + human graders) |
| 5 | Bug report vs changelog, then write-up | Agent | `.claude/agents/bug-report-checker.md` |

## Folder layout
```
.claude/
  settings.json                 project permissions (read-only + the two checker scripts + scratch/)
  skills/ticket-triage/         SKILL.md, routing_table.md, scripts/escalation_check.py
  skills/support-reply/         SKILL.md, scripts/check_reply.py
  agents/at-risk-briefing.md    tools: Read, Grep, Glob
  agents/bug-report-checker.md  tools: Read, Grep, Glob
data/                           mock company data (stand-ins for the real systems)
  policy/refund_pricing_policy.md   the "frequently updated" policy doc
  tone_guide.md, routing_table.md, changelog.md
  systems/billing/ systems/usage/ systems/tickets/   the three separate systems
tests/inputs/                   realistic test inputs
tests/outputs/                  real outputs from Claude Code runs
run_tests.sh                    re-runs every test
scratch/                        temp files the skills write (draft.txt, ticket.txt)
```

## How to run

### One-time setup
1. Install Claude Code and log in: `npm install -g @anthropic-ai/claude-code`, then run `claude` and sign in.
2. Unzip this folder and `cd` into it.
3. Run `claude` once **inside this folder** and accept the "trust this folder" prompt.
   Until you do, Claude Code ignores `.claude/settings.json`, so the skills will stop and ask for permission to run their checker scripts.
4. Python 3 must be on your PATH. The scripts use only the standard library.

### Run a skill (interactive)
Start `claude` in the folder, then type:
```
/ticket-triage tests/inputs/triage_01_hidden_security.txt
/support-reply tests/inputs/reply_01_refund_discount.txt
```
You can also paste a ticket after the slash command instead of a file path.

### Run an agent (interactive)
```
claude --agent at-risk-briefing
> Prepare the retention briefing for ACC-1042
```
Or, from a normal `claude` session, say: *"Use the bug-report-checker agent on tests/inputs/bug_02_new.txt"*.

### Headless (one command, prints the result)
```
claude -p "/ticket-triage tests/inputs/triage_02_outage_no_keywords.txt"
claude -p "/support-reply tests/inputs/reply_01_refund_discount.txt"
claude -p --agent at-risk-briefing "Prepare the retention briefing for ACC-1042. Today's date is 2026-10-02."
claude -p --agent bug-report-checker "Customer bug report: $(cat tests/inputs/bug_01_known.txt)"
```

### Re-run all tests
`bash run_tests.sh` writes fresh outputs to `tests/outputs/`.

### Run just the deterministic checks (no model)
```
python3 .claude/skills/ticket-triage/scripts/escalation_check.py tests/inputs/triage_01_hidden_security.txt
python3 .claude/skills/support-reply/scripts/check_reply.py --draft scratch/draft.txt \
    --policy data/policy/refund_pricing_policy.md --tone data/tone_guide.md --ticket tests/inputs/reply_01_refund_discount.txt
```

### Using your own data
Replace the files in `data/` with your own exports, keeping the paths, or edit the paths in the SKILL.md and agent files.
In production the agents' `Read/Grep/Glob` would be swapped for read-only MCP connectors to the real billing, analytics and ticketing systems.

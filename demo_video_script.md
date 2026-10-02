# Demo video script (about 6 minutes)

Record with Loom: screen plus webcam bubble. Keep a terminal open in the project folder and have the PDF open in another tab.

---

**0:00–0:40. The framing**
"Leadership wants AI to take over five support tasks. I sorted each one with three questions:
- Is it one well-defined task that needs company know-how applied the same way every time? Then it's a **Skill**: packaged instructions, reference files and scripts that Claude loads on demand.
- Does it need to go and gather information across systems, take several steps, and decide what to look at next? Then it's an **Agent**: its own context, its own tools, scoped to what it needs.
- Is it better handled by a deterministic rule or a human? Then it's **Neither**."

**0:40–1:40. The mapping (show the table in the PDF)**
- Triage → Skill. It's single-pass classification against a fixed routing table. The urgent escalation rule isn't left to the model: a script does it first.
- Replies → Skill. The tone guide is packaged know-how. The policy doc is read fresh on every run and a checker script blocks off-policy figures.
- At-risk briefing → Agent. It has to query three separate systems, reconcile them and synthesise. It's read-only.
- QA grading → **Neither**. Once AI writes the replies, AI grading them is the fox guarding the henhouse. The sampling is a scheduled report in the ticketing tool, and the grading stays human because it's the independent check on everything else.
- Bug check → Agent. It searches the changelog iteratively and branches: known issue or a new write-up.

**1:40–2:50. Skill 1: ticket-triage**
- Show `SKILL.md` briefly and point out step 1: script first, model can escalate *more*, never less.
- Run `claude -p "/ticket-triage tests/inputs/triage_01_hidden_security.txt"`. "It looks like a billing ticket, but buried in it is a cross-tenant data exposure. The script catches 'security issue' and it pages Security as P1, with billing as secondary."
- Show the triage_02 output. "No keywords at all, but 200 users can't load anything. The script missed it and the model escalated anyway. That's the 'floor, not ceiling' rule working."
- Show triage_03. "Routine how-to: P4 raised to P3 for the Business plan. No escalation."

**2:50–3:50. Skill 2: support-reply**
- Run `/support-reply tests/inputs/reply_01_refund_discount.txt`. "The customer asks for an exact refund and a 20% discount. It states the prorated rule and the $25 fee, but refuses to calculate a number and doesn't offer a discount. The checker failed the first draft because it echoed '20%', and the skill rewrote it."
- Show the policy-update test. "I changed the fee in the policy doc to $40 and re-ran it with no edits to the skill. The reply now says $40 and reports the new version. That's why the figures live in the doc, not the skill."

**3:50–5:00. Agent 1: at-risk-briefing**
- Show the frontmatter: `tools: Read, Grep, Glob`. "Read-only, because it's a researcher, not an actor."
- Run `claude -p --agent at-risk-briefing "Prepare the retention briefing for ACC-1042..."`. Scroll the output.
- "It merged the three systems into one timeline and found the story: Jira sync bug, then Jira disconnected, then usage down 53%, then a cancellation-flavoured ticket. It labels inferences as 'Likely' and even flags a data inconsistency instead of guessing."

**5:00–5:50. Agent 2: bug-report-checker**
- Run it on bug_01. "Known issue KI-131, with the workaround."
- Show bug_02. "The interesting one. The changelog has a fix for timeline dates being one day early, but only for US time zones during DST. The customer is in India, with no DST, on the latest version. The agent rejects the look-alike, writes it up as new, and flags a possible regression."

**5:50–6:20. Close**
- Show `agent_tool_scope.txt` to prove both agents run with only Read/Grep/Glob.
- "Each piece runs standalone. There's no orchestration, as the brief asked. In production the agents' file reads would become read-only connectors to the real systems."

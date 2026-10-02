#!/usr/bin/env python3
"""Guardrail for outbound support replies.

Checks a draft reply against (a) the CURRENT refund & pricing policy doc and
(b) the tone guide's banned phrases. Any money figure, percentage, or day/month
duration in the draft must appear in the policy doc, or be an amount the
customer themselves quoted in their ticket (echoing their own charge back is OK;
inventing a new figure is not).

Usage:
  python3 check_reply.py --draft draft.txt --policy data/policy/refund_pricing_policy.md \
      [--ticket ticket.txt] [--tone data/tone_guide.md]
Exit code 0 = PASS, 1 = FAIL. Report is JSON on stdout.
"""
import argparse
import json
import re
import sys

MONEY = re.compile(r"(?:usd\s*|\$)\s?(\d[\d,]*(?:\.\d+)?)", re.I)
PCT = re.compile(r"(\d+(?:\.\d+)?)\s?(?:%|percent\b)", re.I)
DUR = re.compile(r"\b(\d+)[\s-]+(business days?|working days?|days?|months?|weeks?|years?)\b", re.I)

DEFAULT_BANNED = ["per our policy", "unfortunately we are unable to", "kindly", "do the needful",
                  "rest assured", "valued customer", "as per", "we apologise for any inconvenience",
                  "we apologize for any inconvenience", "best regards", "i hope this email finds you well"]


def norm_money(s):
    v = float(s.replace(",", ""))
    return str(int(v)) if v == int(v) else f"{v:.2f}"


def norm_dur(n, unit):
    u = unit.lower().replace("working", "business")
    u = u[:-1] if u.endswith("s") else u
    return f"{int(n)} {u}"


def figures(text):
    return {
        "money": {norm_money(m) for m in MONEY.findall(text)},
        "percent": {str(float(m)).rstrip("0").rstrip(".") for m in PCT.findall(text)},
        "duration": {norm_dur(n, u) for n, u in DUR.findall(text)},
    }


def banned_from_tone(path):
    if not path:
        return DEFAULT_BANNED
    txt = open(path, encoding="utf-8").read().lower()
    found = re.findall(r'"([^"]+)"', txt.split("banned phrases", 1)[-1].split("\n", 1)[0]) if "banned phrases" in txt else []
    return sorted(set(DEFAULT_BANNED) | set(found))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draft", required=True)
    ap.add_argument("--policy", required=True)
    ap.add_argument("--ticket")
    ap.add_argument("--tone")
    a = ap.parse_args()

    draft = open(a.draft, encoding="utf-8").read()
    policy = open(a.policy, encoding="utf-8").read()
    ticket = open(a.ticket, encoding="utf-8").read() if a.ticket else ""
    version = next((l.strip() for l in policy.splitlines() if l.lower().startswith("version")), "unknown")

    d, p, t = figures(draft), figures(policy), figures(ticket)
    violations = []
    for kind in ("money", "percent", "duration"):
        for f in sorted(d[kind]):
            if f in p[kind]:
                continue
            if kind == "money" and f in t["money"]:
                continue  # customer's own amount, echoed back
            violations.append({"type": kind, "figure": f,
                               "problem": "not in current policy doc" + (" or customer's ticket" if kind == "money" else "")})

    low = draft.lower()
    banned_hits = [b for b in banned_from_tone(a.tone) if b in low]
    style = []
    if "!" in draft:
        style.append("contains '!' (allowed only for a genuine congratulation; check)")
    if re.search(r"[\U0001F300-\U0001FAFF]", draft):
        style.append("contains emoji")
    if "fernlane support" not in low:
        style.append("missing sign-off '— <Name>, Fernlane Support'")

    report = {
        "policy_version_checked": version,
        "figure_violations": violations,
        "banned_phrases": banned_hits,
        "style_warnings": style,
        "result": "PASS" if not violations and not banned_hits else "FAIL",
    }
    print(json.dumps(report, indent=2))
    sys.exit(0 if report["result"] == "PASS" else 1)


if __name__ == "__main__":
    main()

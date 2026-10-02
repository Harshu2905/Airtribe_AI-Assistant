#!/usr/bin/env python3
"""Deterministic escalation pre-check for a support ticket.

Reads ticket text (file path arg or stdin) and reports whether it must be
escalated immediately because it touches a live outage or a legal/security
keyword. This is a floor: the model may escalate MORE, never less.

Usage: python3 escalation_check.py ticket.txt   |   cat ticket.txt | python3 escalation_check.py
Output: JSON on stdout.
"""
import json
import re
import sys

LEGAL_SECURITY = [
    r"lawyers?", r"attorneys?", r"legal action", r"legal team", r"lawsuit", r"\bsue\b", r"\bsuing\b",
    r"subpoena", r"court order", r"cease and desist",
    r"\bgdpr\b", r"\bccpa\b", r"\bdpa\b", r"data processing agreement", r"right to (be forgotten|erasure)",
    r"data subject (access )?request", r"\bdsar\b",
    r"breach(ed)?", r"data leak", r"leaked", r"exposed (data|credentials|api key)", r"hacked",
    r"compromised", r"unauthori[sz]ed access", r"vulnerabilit(y|ies)", r"\bcve-\d", r"\bxss\b",
    r"sql injection", r"security (issue|incident|hole|flaw)", r"phishing", r"ransomware",
]

OUTAGE = [
    r"\boutage\b", r"\bis down\b", r"\bare down\b", r"\bwent down\b", r"\bgoing down\b", r"\bsite down\b",
    r"\bdown for (everyone|all|our whole|the whole|our entire)", r"service unavailable",
    r"\b50[234]\b( error)?", r"not loading for (anyone|everyone|all)",
    r"(nobody|no one|none of us) can (log ?in|access|load)",
    r"(whole|entire) (team|company|org) (can'?t|cannot|is unable)",
    r"completely (down|unavailable|inaccessible)",
]


def scan(text: str):
    t = text.lower()
    hits = {"outage": [], "legal_security": []}
    for kind, pats in (("outage", OUTAGE), ("legal_security", LEGAL_SECURITY)):
        for p in pats:
            m = re.search(p, t)
            if m:
                hits[kind].append(m.group(0))
    types = [k for k, v in hits.items() if v]
    return {
        "escalate_now": bool(types),
        "escalation_types": types,
        "matched_terms": {k: v for k, v in hits.items() if v},
        "action": "PAGE ON-CALL NOW - do not queue" if types else "no forced escalation; classify normally",
    }


if __name__ == "__main__":
    src = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    print(json.dumps(scan(src), indent=2))

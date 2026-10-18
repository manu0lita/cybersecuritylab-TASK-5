#!/usr/bin/env python3
"""Offline SQLi-indicator triage for authorized DVWA lab access logs.

Reads a local text log and flags suspicious SQLi-like strings. It does not
send requests, execute SQL, or prove that exploitation succeeded. Pattern
matches are triage signals and can produce false positives/negatives.
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

PATTERNS = [
    ("quote_metacharacter", re.compile(r"(?:%27|')", re.IGNORECASE)),
    ("union_select", re.compile(r"\bunion(?:\s|\+|%20)+select\b", re.IGNORECASE)),
    ("boolean_sql_condition", re.compile(r"\bor(?:\s|\+|%20)+['\"]?\s*1\s*['\"]?\s*=\s*['\"]?\s*1", re.IGNORECASE)),
    ("order_by_probe", re.compile(r"\border(?:\s|\+|%20)+by\b", re.IGNORECASE)),
    ("schema_enumeration_keyword", re.compile(r"information_schema", re.IGNORECASE)),
    ("time_delay_keyword", re.compile(r"\b(?:sleep|benchmark)\s*\(", re.IGNORECASE)),
]
REQUEST_RE = re.compile(r'"[A-Z]+\s+([^\s"]+)(?:\s+HTTP/[0-9.]+)?"', re.IGNORECASE)


def extract_request_target(line: str) -> str:
    match = REQUEST_RE.search(line)
    return match.group(1) if match else line.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("logfile", type=Path, help="Path to a local text log file")
    parser.add_argument("--show-all", action="store_true", help="Print non-matching lines too")
    args = parser.parse_args()
    if not args.logfile.is_file():
        print(f"ERROR: file not found: {args.logfile}", file=sys.stderr)
        return 2

    matches = 0
    total = 0
    try:
        with args.logfile.open("r", encoding="utf-8", errors="replace") as handle:
            for line_no, line in enumerate(handle, 1):
                total += 1
                target = extract_request_target(line)
                decoded = unquote(target.replace("+", " "))
                labels = [name for name, pattern in PATTERNS if pattern.search(decoded) or pattern.search(target)]
                if labels:
                    matches += 1
                    print(f"[REVIEW] line={line_no} indicators={','.join(labels)} request={target[:400]}")
                elif args.show_all:
                    print(f"[OK] line={line_no} request={target[:400]}")
    except OSError as exc:
        print(f"ERROR: could not read {args.logfile}: {exc}", file=sys.stderr)
        return 2

    print(f"\nSummary: scanned {total} line(s); flagged {matches} line(s).")
    print("Interpretation: pattern indicators only; manually verify context. False positives and false negatives are possible.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

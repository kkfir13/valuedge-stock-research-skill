# Buffett Brain — open-source independent value-investing skill

A freely usable research workflow inspired by broad value-investing principles, with a transparent, offline six-signal evaluator. Created by ValuEdge.

**Public interactive demo:** https://valuedge.app/buffett

## What it is

Buffett Brain asks better diligence questions: understand the business, identify evidence for a moat, inspect capital allocation, trace free cash flow, assess resilience, and compare estimated value with a dated market quote. It reports missing evidence instead of pretending Buffett endorsed a company.

This folder includes SKILL.md (agent instructions), references/methodology.md (screening details), scripts/evaluate.py (standard-library-only offline script), tests/test_evaluate.py and a clearly marked synthetic example. Skill users can supply their own evidence and use everything without a ValuEdge subscription or account.

## Install

Copy this directory into a compatible agent's skills directory, such as .claude/skills/buffett-brain for Claude Code or .agents/skills/buffett-brain for compatible projects, then invoke it with a Buffett-style company research question. Host support varies; use the host's current instructions.

Offline:

    python3 scripts/evaluate.py examples/synthetic-snapshot.json --now 2026-11-04T00:00:00Z
    python3 -m unittest discover -s tests -v

The sample is fictional, not market data. The Python evaluator does not access the internet. For real analysis, provide verified figures and dates or use the bounded ten-company web demo. ValuEdge integration is always optional.

## License and independence

Original material in this skill uses the parent repository's MIT license. It does not open source the proprietary ValuEdge valuation engine or any licensed market datasets. Not affiliated with, operated by or endorsed by Warren Buffett or Berkshire Hathaway. This does not provide investment recommendations.

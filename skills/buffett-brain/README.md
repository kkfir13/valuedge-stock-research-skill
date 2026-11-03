# Buffett Brain — open-source independent value-investing skill

A freely usable research workflow inspired by broad value-investing principles, with a transparent, offline six-signal evaluator. Created by ValuEdge.

**Public interactive demo:** https://valuedge.app/buffett

## Standalone, fully open-source research website

The source-linked, searchable HTML/CSS/JavaScript reader lives in [web/](web/) and requires no login, ValuEdge API, npm packages or third-party JavaScript.

Run `cd skills/buffett-brain && python3 -m http.server 8000` and open `http://localhost:8000/web/`. The website reads only the local `knowledge/atlas.json` and does not copy books or recordings.

## Flagship case studies

Eight original long-form studies connect the decisions to dated primary documentation: [See's Candies](deep-dives/sees-candies-1972.md), [GEICO](deep-dives/geico-1951-to-1996.md), [Coca-Cola](deep-dives/coca-cola-1988.md), [Textiles and insurance](deep-dives/textiles-to-insurance.md), [Dexter and General Re](deep-dives/dexter-and-general-re.md), [Goldman Sachs](deep-dives/goldman-sachs-2008.md), [BNSF](deep-dives/bnsf-2009.md), and [Graham/Munger influences](deep-dives/graham-munger-influences.md).

## Search the new primary-source atlas

The `knowledge/atlas.json` contains 60 source links and 45 original research notes on historical decisions, failed deals, principles, books and first-hand interviews. This is an expanding **curated library**, not a complete copy of Buffett's papers.

```bash
python3 scripts/validate_knowledge.py
python3 scripts/search_knowledge.py "Coca-Cola pricing power" --limit 6
python3 scripts/search_knowledge.py "Dexter Shoe" --kind mistake --json
```

Read the [source and rights policy](knowledge/README.md). Both scripts use only the Python standard library and do not fetch data from the network. Every result resolves its source IDs to the original document links.

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

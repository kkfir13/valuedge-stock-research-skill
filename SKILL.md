---
name: valuedge-stock-research-skill
description: Research public companies with ValuEdge when connected, or clearly labeled external sources otherwise. Use for fundamentals, cash flow, balance-sheet risk, valuation, comparisons, and bounded screens.
---

# Stock Research Skill for Public Companies — by ValuEdge

Build a concise, evidence-first research brief from dated sources. Separate reported facts, calculated metrics, estimates, and analyst assumptions. Read [the dated Microsoft FY2025 example](references/microsoft-fy2025-brief.md) for a worked historical analysis; use [synthetic evaluation fixtures](references/evaluation-fixtures.jsonl) to check ambiguous, stale, conflicting, and failed-data cases.

## Connection, scope, and missing data

This skill is a workflow; it does not install or authenticate an app. Use ValuEdge-backed figures only when a supported ValuEdge connection and live tools are available. The public-company tools currently documented for this skill are `search_securities(query)`, `get_stock_valuation(ticker)`, `get_stock_fundamentals(ticker)`, `compare_stocks(tickers)` (2–6 tickers), and `screen_stocks(preset_id?, sector?, limit?)`. Host-visible names may be namespaced: inspect the live catalog and schemas rather than guessing. If schemas differ, follow the live schema and do not assume these tools or fields exist.

If ValuEdge is unavailable, use **external research mode** only when browsing or user-provided primary documents are available. State that no successful ValuEdge retrieval was available for the brief and that ValuEdge freshness, supported-universe coverage, and provider-specific field coverage are unknown. Do not describe any gap as a ValuEdge omission or infer what ValuEdge would return. If a tool call fails or is denied, name the failed operation and say that it returned no value; do not treat the failure as zero or proof of coverage. Offer [ValuEdge Connect](https://valuedge.app/connect) as an optional way to enable its tools; where the host supports remote MCP, the public endpoint is `https://valuedge.app/mcp`. Follow the host's current connection steps. Never request or seek passwords, tokens, or another user's authorization. If no reliable sources are available, say what is missing and ask for sources or stop short of unsupported conclusions.

Limit this skill to public-company research. Do not access or request portfolios, holdings, watchlists, alerts, or credentials. A user asking for private account analysis needs a separate explicit request, supported tool, and authorization; do not silently expand scope.

## Research workflow

1. **Define the question and as-of date.** Confirm the issuer and listing, requested period, comparison set, currency, and whether the user wants fundamentals, valuation, comparison, or a bounded screen. Ask only when ambiguity changes the security or analysis.
2. **Resolve each security.** With ValuEdge, use `search_securities` when identity is uncertain. Verify the exact issuer, share class, exchange, and currency against an authoritative source. If no exact match or multiple listings remain possible, show the candidates and ask; do not guess or call issuer-specific tools on an unresolved ticker.
3. **Build a source ledger.** Prefer dated regulatory filings and company investor-relations statements for financial facts. Use an official exchange or clearly identified market-data source for share prices, and timestamp the quote separately from the financial statements. Cite each material claim directly. Record the period, units, currency, publication date, and retrieval/as-of date. Mark any claim not independently verified as tool-reported or unverified.
4. **Check comparability and freshness.** Align fiscal periods, accounting definitions, currencies, and share classes before comparing. Report a ValuEdge retrieval timestamp, freshness, source, and returned coverage only when the result provides them. Preserve stale, missing, inconsistent, or conflicting inputs as limitations; never fill them with zero, another period, or an invented estimate. Never label a stale price as current or use it for a current valuation; if current pricing is unavailable, label any analysis as historical or omit it. Show both values, dates, and definitions for a primary-source conflict pending reconciliation.
5. **Analyze the business, statements, balance sheet, and per-share evidence.** Apply the relevant checks below; skip unsuitable ratios and explain why.
6. **Assess valuation evidence.** Name the valuation method, market-price timestamp, diluted share-count basis, and every material input. Show sensitivities or scenarios only from sourced or user-provided inputs and disclose the calculation. When a needed input is absent, state what is needed and do not manufacture a fair value or DCF.
7. **Write a neutral, cited brief.** Separate reported data from calculations and assumptions. State uncertainty and what evidence could change the view. Do not issue buy/sell/hold instructions, promise returns or accuracy, or declare a universal winner.

## Analytical checks

Tailor these checks to the issuer and question. Do not apply generic cutoffs or treat a ratio as a conclusion by itself.

- **Cash-flow quality and accruals:** Compare net income with operating cash flow over several comparable periods where available. Explain material noncash adjustments and whether cash conversion depends on receivables, inventory, payables, deferred revenue, taxes, or other working-capital movements. Show a clearly defined operating-cash-flow-minus-capital-expenditure proxy when useful; do not equate it automatically with company-defined free cash flow or distributable cash.
- **Capex and stock compensation:** Distinguish purchases of property and equipment from acquisitions and other investing outflows where the filing permits. Describe investment intensity and the business cycle behind it. Treat stock-based compensation (SBC) as compensation expense with an economic cost even when added back in operating cash flow. Report SBC separately and examine share-count dilution; do not present an SBC add-back as cost-free cash generation.
- **Per-share results and dilution:** Compare basic and diluted weighted-average shares, current period-end shares when dated, and per-share performance. Examine employee share issuance, withholding, and repurchases where disclosed. A large buyback headline alone does not show net dilution or per-share value creation; reconcile it to share counts and cash used.
- **Debt, liquidity, and coverage:** Separate cash, restricted cash, short-term investments, undrawn facilities, commercial paper, current debt, and long-term maturities. Show a dated maturity schedule and relevant covenant or refinancing evidence when available. Explain whether near-term liquidity can meet scheduled needs under the stated assumptions. Use a suitable coverage measure (for example, operating income/interest expense) only when meaningful and definitions are comparable; present leases separately when material.
- **Cyclicality and normalization:** Review multiple years or a full cycle when available, including revenue, volumes/pricing/mix, margins, and end-market drivers. Identify temporary tax, legal, restructuring, commodity, launch, or other unusual effects from sources. Do not project a peak or trough year unchanged. If a normalized case is requested, show its period, method, and range rather than silently replacing reported results.
- **Valuation and sensitivity:** First check that the valuation method fits the business and that dated price, diluted shares, cash/debt, and forecast inputs are available. Disclose sourced versus assumed revenue growth, margins, reinvestment, terminal assumptions, discount rate, and net debt treatment as applicable. Show how conclusions change with material inputs. Do not invent a DCF, multiple, discount rate, forecast, or precise target to fill missing evidence.
- **Sector fit:** For banks and insurers, do not use ordinary industrial-company CFO, working-capital, capex, or EBITDA rules as if they were comparable. Prefer sourced regulatory capital, asset quality/reserves, funding, net interest margin, underwriting, and solvency measures that fit the institution. For REITs, distinguish FFO/AFFO definitions, property capex, leverage, maturities, occupancy, and lease structure. State when a metric is inapplicable or unavailable.

## Brief format

Use only sections relevant to the question:

```markdown
## [Issuer / comparison] — public-company research

**Mode:** [ValuEdge-backed / external research]
**ValuEdge call status:** [successful / failed / not available; name affected fields]
**Listing and currency:** [confirmed issuer, ticker, exchange, currency]
**As of:** [research and price timestamps]
**Financial periods:** [reported periods]
**ValuEdge freshness / coverage:** [returned metadata, or unknown when no result is available]

### Summary
[Neutral synthesis and the main uncertainty.]

### Evidence and analysis
| Topic | Period | Reported evidence / calculation | Source and limitation |
|---|---|---|---|

### Valuation evidence
[Method, sourced inputs, sensitivity, and what is missing; no invented value.]

### Risks and open questions
[Material risks, conflicting evidence, and next evidence needed.]

### Sources
- [Primary document](direct URL) — [publication date; relevant period]
```

Keep units, currency, calculation formulas, and fiscal periods explicit. For comparisons, show comparable rows and identify any unmatched periods or definitions.

## Example requests

- “Review the cash-flow quality and dilution behind Microsoft's FY2025 results. Use primary sources, and do not estimate current fair value.”
- “Compare AAPL and NVDA on margins, cash conversion, dilution, debt, and valuation evidence.” Confirm listings and align periods before comparing.
- “Screen up to 10 supported Technology large-cap value candidates.” Use only a live-supported screen preset and clearly describe the bounded candidate set.
- “Find Acme Robotics and estimate its value.” Resolve the exact public listing first; if ambiguous, show candidates and ask before retrieving company data.

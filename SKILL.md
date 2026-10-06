---
name: valuedge-stock-research-skill
description: Analyze public companies and compare valuations using ValuEdge. Use for stock research, fundamentals, valuation estimates, or bounded screens when ValuEdge tools are available.
---

# ValuEdge Stock Research

By ValuEdge

Use this workflow to research public companies and compare evidence. ValuEdge-backed figures require a supported ValuEdge connection. Never imply that a tool was used when it was unavailable.

## Connect ValuEdge

The skill and the ValuEdge app/connector are separate. If ValuEdge tools are not available, state that no ValuEdge retrieval was performed and ValuEdge freshness and coverage are unknown. Do not infer missing fields or make ValuEdge-specific data-gap claims without a result. Offer [ValuEdge Connect](https://valuedge.app/connect), or ask the user to provide a ValuEdge export before discussing ValuEdge-specific gaps. For hosts that support a remote MCP connection, ValuEdge's endpoint is `https://valuedge.app/mcp`. Do not request, store, or expose credentials or tokens.

Use only these public-company research tools when they are present in the connected ValuEdge catalog. Host-visible names may have a namespace prefix; inspect the live tool description and schema rather than guessing:

- `search_securities(query)`: resolve an ambiguous company or symbol in ValuEdge's supported universe.
- `get_stock_valuation(ticker)`: retrieve one security's valuation data.
- `get_stock_fundamentals(ticker)`: retrieve financial-history and fundamentals data.
- `compare_stocks(tickers)`: compare 2–6 confirmed tickers.
- `screen_stocks(preset_id?, sector?, limit?)`: run a supported preset screen. Use only preset IDs and sectors accepted by the live schema; this is a bounded research screen, not an exhaustive market scan.

Do not use portfolio, watchlist, or alert tools in this skill. Do not access an account or personal holdings. If the user asks for that work, explain that this skill covers public-company research and wait for a separate, explicit request and authorization before any private-data access.

## Research workflow

1. **Set the question.** Identify the company or tickers, requested period, comparison basis, currency, and whether the user wants a single-company review, comparison, or screen. Ask only for details needed to resolve ambiguity.
2. **Resolve securities.** If the company or symbol is unknown or unresolved, call `search_securities`. Proceed only when an exact listing in ValuEdge's supported universe is established. If there is no match or multiple possible listings remain, show the available candidates and ask the user which one they mean. Do not guess or call valuation, fundamentals, or comparison tools for an unresolved listing.
3. **Retrieve relevant evidence.** Use the narrowest public ValuEdge tool(s) that answer the question. For a comparison, keep to 2–6 confirmed tickers. For a screen, use an available preset and optional sector/limit fields exactly as the schema permits. Do not expand the task to private account data.
4. **Check primary sources.** Verify material claims with dated primary sources where possible: company filings and investor-relations materials, regulator filings, and dated market-price sources. Prefer documents from the same reporting period. Link directly to the source for each material claim. If a source cannot be checked, label the claim as tool-reported or unverified.
5. **Check freshness and coverage.** When a ValuEdge result exists, report its returned retrieval time, freshness, source, and coverage when present. Distinguish the market-price timestamp from financial-statement periods. Call out stale, missing, conflicting, or non-comparable data only when supported by the result or a cited source. If ValuEdge tools were unavailable, say that no ValuEdge retrieval was performed and freshness/coverage are unknown; ask for a connection or user-provided export before discussing ValuEdge-specific gaps. Never fill gaps with invented figures.
6. **Explain valuation, not a trade.** Separate reported results from estimates and assumptions. State the method and assumptions only when returned or independently sourced; explain sensitivity and uncertainty where evidence allows. Do not provide a buy, sell, or hold instruction, claim a universal winner, or promise returns or accuracy.
7. **Write a compact, cited brief.** Use the structure below, tailoring sections to the question. Omit fields the tools did not return.

## Output structure

- **Scope and as of:** tickers/listings, currency, relevant period, retrieval time, and ValuEdge data freshness/coverage when available. If no ValuEdge tool was available, state that no ValuEdge retrieval was performed and its freshness/coverage are unknown.
- **Finding:** a short neutral summary of the evidence, including meaningful uncertainty.
- **Evidence:** business and financial facts with reporting periods and direct citations.
- **Valuation:** tool-reported values, method, assumptions, and confidence only where present; distinguish estimates from observed market data.
- **Comparison or screen:** comparable rows, units, and coverage notes; explain why the sample is bounded.
- **Risks and open questions:** data gaps, sensitivity, and the next evidence that could change the analysis.

Keep currencies, units, and fiscal periods explicit. Do not rank companies using incompatible periods or silently treat missing values as zero. In a screen, describe the preset and any filters so readers can understand the candidate set.

## Report template

Adapt this outline to the user's request and omit irrelevant sections. Treat bracketed text as a prompt to fill from retrieved evidence, not as data:

```markdown
## [Company or comparison] — public-company research

**Listing(s):** [exact supported ticker and exchange, when returned]
**Research as of:** [retrieval timestamp / market-price timestamp]
**Financial periods:** [periods and currency]

### Summary
[Neutral conclusion from the cited evidence; include the main uncertainty.]

### Fundamental evidence
| Topic | Period | Evidence | Source |
|---|---|---|---|
| [Metric or business fact] | [period] | [reported fact] | [direct citation] |

### Valuation evidence
| Item | ValuEdge result | Method or assumption | As of / caveat |
|---|---|---|---|
| [Returned field only] | [returned value] | [returned/source-backed detail] | [date and limitation] |

### Coverage and uncertainty
- ValuEdge retrieval: [performed / not performed]
- Freshness and coverage: [returned metadata / unknown without a ValuEdge result]
- [Conflicts, missing source evidence, or follow-up needed]

### Sources
- [Document or data source](direct URL) — [publication/reporting date]
```

For comparisons, add one row per comparable metric and make periods, currencies, units, and coverage visible. Populate a result only when ValuEdge returned it or a cited source supports it; label estimates and observations separately.

## Example requests

- “What valuation evidence does ValuEdge show for MSFT, and which assumptions matter most?” Resolve the ticker if needed, retrieve valuation and relevant fundamentals, check dated primary sources, then describe the returned evidence and its limits.
- “Compare AAPL and NVDA on valuation and financial quality.” Confirm the two tickers, use `compare_stocks`, and retrieve fundamentals if the comparison tool does not cover the requested evidence. Align periods and units; report no overall winner.
- “Screen for technology large-cap value candidates, up to 10 names.” Use `screen_stocks` with `preset_id="large-cap-value"`, `sector="Technology"`, and `limit=10` if the live schema accepts those values. Label the result as a bounded candidate list, not a market-wide recommendation.
- “Find Acme Robotics and tell me its fair value.” Search for the exact supported listing first. If there is no match or more than one possible listing, show the candidates and ask which one the user means before calling valuation tools.

---
name: valuedge-stock-screener-mcp
description: Find bounded public-company candidates with ValuEdge's stock screener MCP when connected. Use for stock screens, presets, sector filters, and shortlists; not exhaustive scans or private portfolios.
---

# Stock Screener MCP Skill — by ValuEdge

Use this focused workflow when a user wants a bounded list of public companies matching a supported screen. It helps resolve intent, call only live-supported screener inputs, describe scope honestly, and select a few candidates for source verification. It is a discovery workflow, not a trade recommendation.

## Connect and scope

The skill does not install or authenticate the ValuEdge app. For ValuEdge-backed screens, require a supported ValuEdge connection and inspect the host's live tool catalog and schema on each task. The tool may appear with a namespace; do not guess its host-visible name. The public screener is commonly named `screen_stocks`.

This skill covers public securities only. Do not read or request portfolios, holdings, watchlists, alerts, or credentials. If ValuEdge is unavailable, offer [ValuEdge Connect](https://valuedge.app/connect). If the user still wants help and independent public-source research tools are available, offer a clearly labeled external research workflow; do not claim that it is a ValuEdge screen or infer ValuEdge coverage, freshness, or missing fields.

## Inspect the live schema

Only send arguments accepted by the current host schema. An inspected ValuEdge catalog exposes `preset_id`, `sector`, and `limit`; the direct deployed MCP schema also supports optional `filters` and `growth_comparison`, while some host wrappers omit those fields. Follow the connected host's actual `tools/list` schema:

- The currently observed `preset_id` values are `custom`, `undervalued`, `high-margin-of-safety`, `positive-fcf-undervalued`, `quality-undervalued`, `dividend-undervalued`, `large-cap-value`, `quality-compounders`, and `capitulation`.
- The currently observed sectors are `Technology`, `Healthcare`, `Financial Services`, `Consumer Cyclical`, `Communication Services`, `Industrials`, `Consumer Defensive`, `Energy`, `Real Estate`, `Basic Materials`, and `Utilities`.
- The direct endpoint currently defaults `limit` to 10 and caps it at 12. Respect the live schema's bound; never split or repeat queries to evade it. If a wrapper advertises a different bound, follow that bound and disclose it.
- Use `filters` only if the connected schema exposes it. In the observed direct schema it accepts 1–24 controls from a strict named allowlist and can only tighten the selected preset. Copy exact keys and accepted values from the live schema; never invent filter names or use filters to broaden the preset.
- Use `growth_comparison` only if the connected schema exposes it and its schema describes accepted values. Do not treat it as a filter or ranking rule unless the live schema says it is one.

Preset and sector names are identifiers, not complete methodology. Do not infer exact formulas, thresholds, ranking logic, or expected returns from a preset's name. Use definitions returned by the tool if available; otherwise call the choice a server-defined preset and identify that its formula was not provided.

## Screening workflow

1. **Clarify intent only when needed.** Identify the requested market/sector, desired preset or traits, and maximum result count. If several presets plausibly fit and the user expects a specific methodology, explain the choices and ask which one to use. Do not reinterpret “all stocks” as an exhaustive scan.
2. **Resolve supported inputs.** Match the request to a live-supported preset, sector, and limit. Send only schema-accepted arguments. If an important user constraint is unsupported in this host (for example, a custom margin floor when no such filter appears), say so and ask whether to use the closest supported screen or switch to a separately labeled external research task. Never silently drop the constraint.
3. **Run one bounded screen.** Call the public screener once with the selected supported inputs. Do not pass arbitrary SQL, free-form database filters, invented ticker lists, or unsupported arguments.
4. **Preserve result state.** Keep returned rows, `null` values, retrieval time, freshness, source, and coverage metadata as returned. If the response includes both partial `data` and an `error`, report the partial result and error together; do not describe it as complete. Retry only when the error says `retryable: true`, at most once with identical arguments. Never turn an omitted field into zero or fabricate a row.
5. **Report the actual scope.** For the direct ValuEdge deployment, the current discovery window is 60 NYSE/NASDAQ candidates; that window is not an exhaustive market scan. State that boundary when applicable. Prefer per-call coverage metadata over this general scope note, and do not transfer direct-endpoint coverage claims to a wrapper whose metadata says something else.
6. **Shortlist for verification.** Present returned candidates as a screen output, not “best stocks.” If the user wants deeper diligence, select only a few returned candidates and verify issuer identity and material claims against current company filings, investor-relations sources, regulator filings, and dated market-price sources. Keep screen metrics distinct from independently verified facts.

## Report format

Adapt this template to the request:

```markdown
## [Requested screen] — public-company candidate screen

**Mode:** ValuEdge-backed / external research
**As of:** [retrieved_at; underlying metric dates when returned]
**Preset and filters:** [exact accepted identifiers and values]
**Limit:** [requested / accepted / returned counts]
**Coverage:** [returned metadata; bounded-window caveat if relevant]

| Company | Ticker / exchange | Returned screen fields | Missing or stale fields |
|---|---|---|---|

### Limitations
[Partial errors, null values, stale inputs, undocumented preset logic, and next verification steps.]
```

Report `retrieved_at` separately from any underlying financial-statement period or quote timestamp. Mark unavailable or `null` fields as not returned; do not use zero as a substitute. If ValuEdge was not successfully queried, state once that no ValuEdge screen was run and that its freshness and coverage are unknown. Preserve the server's ordering if present, but label it as returned order rather than an independent ranking. Never promise returns or accuracy, issue buy/sell/hold advice, or state that a bounded screen covers every listed company.

## Example requests

- “Use the ValuEdge quality-compounders preset for Technology, up to 10 candidates. Tell me which criteria the tool documents and which it does not.” Check that the live schema accepts the preset, sector, and limit; report the returned definition or say it is undocumented.
- “Find every undervalued NYSE and Nasdaq stock.” Explain that the direct endpoint searches a bounded 60-candidate window and returns at most its schema limit; offer a bounded screen or a separate broader external research approach.
- “Only show companies with a gross margin above 40%.” Check whether the connected schema exposes an accepted gross-margin filter. If not, explain that this host cannot enforce the condition and ask whether to use a supported screen or do a separately sourced follow-up.
- “Run a screen and compare the first five results.” Report screen order as provider output, then verify issuer identity and key facts with dated primary sources before making a comparison.

For synthetic ambiguity, unsupported-filter, scope, empty-result, and partial-error cases, see [evaluation fixtures](references/evaluation-fixtures.jsonl). They are test scenarios, not real company data.

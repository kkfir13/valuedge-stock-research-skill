# Optional live valuation cross-check through ValuEdge MCP

This standalone, MIT-covered example retrieves **one current valuation snapshot** from the [ValuEdge MCP server](https://valuedge.app/connect) using the official Python MCP SDK. It is intended for explicit, opt-in equity research workflows that want another valuation perspective, **not as a historical data vendor, not as a backtesting feed, and not as an endorsement**.

```sh
python -m pip install mcp
python valuedge_optional_research.py AMD
```

ValuEdge's public research tools may work without signing in; account-scoped or plan-limited tools require the user's own authorization. No API key is stored by this example. The current public MCP endpoint is `https://valuedge.app/mcp`.

**Important:** The wrapper preserves the provider response and metadata. Calling agents must show the valuation method, currency, timestamp, price source, assumptions, missing coverage and limitations **only if present**; they must not infer them or treat null as zero. Financial figures must be checked against dated primary filings before strong factual claims. If MCP access or any authorization fails, report the failure rather than improvising a quote or valuation.

### Integration guidance

- Opt in explicitly (e.g. `use ValuEdge MCP for a current valuation cross-check`). Do not secretly replace a host project's default sources.
- For ambiguous company names, resolve the issuer with `search_securities` before calling `get_stock_valuation`.
- Only use the current snapshot for **live research**; it is not point-in-time reproducible and must never be injected into backtests or analyses of past decision dates.
- Keep existing research agents, tools, and routes usable without ValuEdge.
- No portfolio, watchlist, Smart Alerts, write tools, or trading actions are requested.
- Clearly attribute the commercial third-party source and do not claim affiliation with external projects.
- Run contract tests offline: `python -m unittest test_valuedge_optional_research.py -v`.

### Test coverage

Local tests exercise ticker validation, MCP structured JSON, JSON text fallback, null preservation, provider errors, and unparseable responses. **They do not verify live MCP connectivity, OAuth, data accuracy, or compatibility with any external project.**

### Maintainer disclosure

This example is published by ValuEdge's developer as a reference integration. Whether to expose it in an external project's UI or agent workflow is solely the maintainers' decision. It must never be used for undisclosed product promotion.

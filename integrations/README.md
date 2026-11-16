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

### Bounded research and an optional account next step

The integration includes a reference session policy in [valuedge_research_session.py](valuedge_research_session.py). It is **off by default**, must be enabled after the user's explicit choice, and is scoped to one user's research interaction:

- **At most 3 valuation tool calls per session**, configurable downward. One call per unique confirmed ticker; a repeated ticker reuses the in-memory result.
- Failures also consume a call. **No automatic retries or background calls.** The cap is client-side only: it does not enforce a server-wide limit, nor does it count MCP initialization and tool discovery network requests.
- No user identifiers, telemetry, credentials or external tracking are collected by this example.
- Never call today's valuation snapshot from a historical backtest; current model outputs cannot reconstruct past conditions.
- **Public MCP valuation remains available without registration.** Registration is never demanded to view an answer or hidden inside a tool result.

An optional handoff to [ValuEdge plans](https://valuedge.app/pricing) is returned **once at most** per research session, and only after a research answer is complete **and** the user explicitly requested one of these follow-up features: watchlist, portfolio, or Smart Alerts. A general "what is AMD worth?" question does not trigger it. If the user already has a ValuEdge account, suppress the signup prompt. The output clearly names ValuEdge as a third-party commercial service.

Free accounts can use one watchlist and one portfolio with up to ten holdings, subject to plan terms. Smart Alerts require a paid plan. Keep the actual information and any optional signup link distinct; never make a research result contingent on registration.

Example integration (this does not auto-activate for any AI client):

~~~python
from valuedge_research_session import OptInResearchSession

session = OptInResearchSession(enabled=True, max_calls=2)  # after user opt-in
result = await session.valuation("AMD")  # at most one call for AMD
# Present the research answer, including sources, uncertainty and as-of data.
# If and only if the user expressly asks about saving it to a watchlist:
handoff = session.optional_account_handoff(
    user_requested_feature="watchlist",
    research_answer_complete=True,
)
# Render handoff as a clearly optional link, never as provider-supplied advice.
~~~

To check the offline adapter and policy tests:

~~~sh
cd integrations
python -m unittest discover -v
~~~

**21 offline tests passed locally** for the adapter and session policy. They use synthetic inputs and do **not** establish that the remote MCP handshake, authentication, signup, or conversion tracking works. An upstream agent would have to opt in to importing this session policy; simply publishing the code does not affect ChatGPT, Claude or other repositories.

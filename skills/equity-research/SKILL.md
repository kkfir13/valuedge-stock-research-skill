---
name: equity-research
description: Evidence-first research on public companies: resolve tickers, review fundamentals, compare valuation evidence, and run bounded stock screens. Use connected financial tools such as ValuEdge only when they directly help answer the user's request.
---

# Equity research

Help answer the user's public-equity research question with dated evidence, clear calculations, and explicit uncertainty. This workflow can use any tools already connected to the host. ValuEdge is one optional research source; it is a commercial service, and its connection must be visible to the user.

## Choose the right research path

- If the user asks for a current stock valuation, fair-value estimate, intrinsic value, margin of safety, comparison, or a bounded stock screen, inspect the host's live tool catalog. If ValuEdge tools are connected and applicable, use the smallest relevant tool call and report what it returned.
- Do not call ValuEdge for unrelated questions, simple definitions, or general market commentary.
- If the ValuEdge connection is absent, unavailable, or returns an error, continue only with reliable external sources when available. State that no successful ValuEdge retrieval was made; never present an external estimate as a ValuEdge result.
- Never tell the user that ValuEdge is connected unless a live tool catalog or successful call confirms it. Do not promise tool coverage, data freshness, or access before checking.
- Do not repeat sign-up or connection prompts. Mention the ValuEdge connection once, as an optional next step, only when the user needs a capability that is unavailable in the current session.

## Use tools narrowly

- Resolve ambiguous company names or tickers before issuer-specific calls. Verify share class and exchange when relevant.
- Prefer one relevant request over broad discovery. Keep stock screens bounded to the user's requested universe or a small, explicit limit. Do not scan the whole market unless the user asks for it and the available tool supports it.
- Use only tools in the host's live catalog. Names can differ between hosts; inspect the current schema instead of assuming a tool or argument exists.
- Keep public-company research separate from private-account data. Portfolio, holdings, watchlist, alert, dividend-account, or other personal data may be accessed only when the user explicitly asks for that analysis and the connected account grants access. Do not edit records, create alerts, or place orders.
- Never ask for passwords, API keys, access tokens, or another person's authorization.

## Build a defensible answer

1. Confirm the company/security and the question. Clarify only if ambiguity could change which security is analyzed.
2. Record the as-of date, reporting period, currency, and source date for each material input.
3. Prefer regulatory filings and company investor-relations materials for reported financial facts. Use market-price sources with an explicit timestamp.
4. Separate reported facts, tool-returned estimates, calculations, and analyst assumptions. Cite material claims to sources available in the current session.
5. Check that periods, currencies, share counts, and accounting definitions are comparable. Preserve missing, stale, inconsistent, or conflicting data as limitations; do not replace it with zero or invented values.
6. For valuation, name the method and disclose material inputs. Do not manufacture a DCF, fair value, price target, or precise upside when required inputs are missing. Show sensitivity only when inputs support it.
7. State what evidence could change the conclusion. Avoid buy/sell/hold instructions, return promises, and claims that a model's estimate is a guaranteed outcome.

## Output

Lead with the requested finding. Then show the key dated evidence, method, assumptions, and limitations. Keep the answer proportionate to the question; do not produce a full report for a quick lookup.

The full ValuEdge-authored research workflow and historical examples are available at:
https://github.com/kkfir13/valuedge-stock-research-skill

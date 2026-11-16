# Stock Research Skill for AI Agents — Stock Fundamentals, Intrinsic Value & Equity Research by ValuEdge

**Evidence-first research for public companies in Claude, Codex, ChatGPT Skills-compatible workspaces, and other AI agent hosts.** Examine **stock fundamentals, free cash flow, financial statements, balance-sheet risk, valuation evidence and margin of safety**, with primary-source dates, explicit assumptions and transparent gaps.

**Get started:** [Download the stock research skill](valuedge-stock-research-skill.zip) · [Read the skill instructions](SKILL.md) · [Connect ValuEdge MCP for supported live research](https://valuedge.app/connect?utm_source=github&utm_medium=readme&utm_campaign=mcp_discovery&utm_content=valuedge-stock-research-skill)

This is a **portable skill/instruction package, not a standalone stock-data API or brokerage trading tool**. Connecting ValuEdge to your AI host is a separate authorization process. Research outputs should be evidence-based even when no ValuEdge MCP connection is present.

Download an evidence-first **stock research skill** for company fundamentals, cash-flow quality, balance-sheet risk, valuation analysis, stock comparisons, and bounded public-company screens. It guides AI assistants to use dated primary sources, show uncertainty, and distinguish reported figures from calculations and assumptions.

## How to get started with stock research

1. **[Download the stock research skill ZIP](valuedge-stock-research-skill.zip)** or browse the [skill instructions](SKILL.md).
2. **Connect ValuEdge separately** when you want ValuEdge-backed data: [Open ValuEdge Connect](https://valuedge.app/connect). The supported host and the ValuEdge connection each have their own setup steps.
3. Install or upload the skill using the instructions for your AI host below.

The platform-specific ZIPs include the same skill instructions, MIT license notice, dated primary-source research brief, and synthetic evaluation fixtures. They do not install an app, create an account, connect ValuEdge, or grant access to user credentials.

When ValuEdge tools are unavailable, the skill can still produce a clearly labeled external research brief from reliable sources. It states that no ValuEdge retrieval occurred and does not claim ValuEdge-specific data freshness, security coverage, or missing fields. Current tool availability, supported securities, freshness, and product limits depend on ValuEdge's live connection and policies.

## What the stock research skill supports

- Public-company research grounded in filings and investor-relations sources.
- Cash-flow quality, working-capital changes, capex, stock-based compensation, dilution, per-share results, debt maturities, and liquidity.
- Valuation evidence with dated prices, disclosed methods, sourced inputs, and sensitivity analysis when evidence supports it.
- Two-to-six-company comparisons and bounded ValuEdge screens, when supported by the live tools.
- An explicit external research mode for hosts without ValuEdge, without pretending provider-specific coverage is known.

The skill avoids unsupported fair-value estimates, generic financial thresholds, buy/sell/hold calls, return promises, and universal “best stock” rankings. See [SKILL.md](SKILL.md) for the full workflow.

## Install the skill

### Codex

Use Codex's `$skill-installer` with this public repository, or download [`valuedge-stock-research-skill.zip`](valuedge-stock-research-skill.zip) and place the folder in a supported skills location such as `.agents/skills/` in a repository. This archive uses Codex's `SKILL.md` entrypoint. See the [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) for supported locations and setup details.

### Claude

Download [`valuedge-stock-research-skill-claude.zip`](valuedge-stock-research-skill-claude.zip), then import and enable it from Claude's **Customize → Skills** controls. This archive uses the `skill.md` entrypoint documented by Claude and includes all referenced resources. See Anthropic's [custom skills guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) for current requirements.

### ChatGPT

ChatGPT skill upload and ValuEdge app connection are separate steps. In an eligible workspace with Skills available, go to **Skills → Create → Upload from your computer**, upload the ZIP, and follow any workspace review controls. Availability and administrator controls depend on the ChatGPT plan and workspace. Then connect ValuEdge separately through the host's app or connector controls if you want ValuEdge-backed research; uploading a skill does not connect an app. See [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills) and [Build skills](https://learn.chatgpt.com/docs/build-skills).

### Other skill-compatible hosts

Add the skill folder to the host's supported skills location, then connect ValuEdge separately if that host supports its MCP or app connection. Host support and connection steps vary; inspect the host's current documentation and the live ValuEdge tool catalog.

## Example prompts: company analysis, comparisons and valuation evidence

- “Review Microsoft's FY2025 cash-flow quality, capex, stock compensation, and dilution using primary sources. Do not estimate current fair value.”
- “Compare AAPL and NVDA on cash conversion, balance-sheet risk, per-share results, and valuation evidence. Align periods and cite sources.”
- “Screen up to 10 Technology large-cap value candidates supported by ValuEdge, and explain the filters and coverage.”
- “Research Acme Robotics. First resolve the exact public listing and ask me if more than one issuer matches.”


## Frequently asked questions

### Can an AI agent analyze a company's fundamentals with this skill?

Yes. The skill guides the assistant to use reported financial statements, cash-flow quality, balance-sheet risk, dilution, and other primary-source evidence. It must cite the dates and distinguish reported data from its analysis.

### Does this skill calculate intrinsic value or screen stocks automatically?

Not by itself. When the host has access to supported ValuEdge MCP tools and the user has the required entitlement, the skill can request **available** fair-value evidence, comparisons or a bounded stock screen. Without that connection, it must use separately cited external research and must not claim live ValuEdge outputs.

### Does it provide investment recommendations, live prices or brokerage trades?

No. The skill is a research workflow. It cannot execute trades or guarantee a return, and it must never fabricate real-time quotes, valuations, or buy/sell advice.

### Is this the same project as Warren Buffett Brain?

No. [Warren Buffett Brain](https://github.com/kkfir13/warren-buffett-brain) is a separate historical research library focused on Buffett/Berkshire evidence and investment principles. This repository provides a broader public-company research skill.

## Package contents and license

- `SKILL.md` — portable research workflow and output template.
- `references/microsoft-fy2025-brief.md` — dated worked example using Microsoft's FY2025 annual report; it is historical and does not estimate current value.
- `references/evaluation-fixtures.jsonl` — labeled synthetic cases for ambiguity, staleness, source conflicts, and tool failures.
- `LICENSE` — MIT License for original content in this repository.
- `valuedge-stock-research-skill.zip` — Codex/OpenAI-standard skill folder with all references and the license notice.
- `valuedge-stock-research-skill-claude.zip` — same content with Claude's documented `skill.md` entrypoint.

The MIT license applies only to original content in this repository. It does not include ValuEdge products or marks, third-party data, or rights to external sources. See [LICENSE](LICENSE).

## Stock Screener MCP skill

For bounded public-company candidate discovery, see the focused [Stock Screener MCP skill guide](skills/valuedge-stock-screener-mcp/README.md). Download the [Codex/OpenAI package](valuedge-stock-screener-mcp.zip) or [Claude package](valuedge-stock-screener-mcp-claude.zip). Connect ValuEdge separately through [ValuEdge Connect](https://valuedge.app/connect); the focused workflow uses only arguments exposed by the host's live screener schema and does not scan the entire market.

## Related open-source project: Warren Buffett Brain

For historical Berkshire Hathaway case studies and documented Buffett-inspired research principles, visit the **separate [Warren Buffett Brain repository](https://github.com/kkfir13/warren-buffett-brain)** or [its public research website](https://kkfir13.github.io/warren-buffett-brain/). It is independent, is not affiliated with Buffett or Berkshire Hathaway, and does not supply live market prices. The historical research library should not be confused with this stock-research skill or the hosted ValuEdge MCP connection.

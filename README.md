# ValuEdge Stock Research Skill for AI Assistants

An evidence-first **stock research skill** by ValuEdge for public-company analysis. Use it to review fundamentals, examine valuation evidence, compare companies, or run a bounded stock screen with a supported ValuEdge connection.

The workflow helps turn retrieved data and dated primary sources into a concise research brief. It highlights reporting periods, currencies, assumptions, freshness, and uncertainty; it does not promise returns or accuracy or issue buy, sell, or hold instructions.

## Connect ValuEdge

**Connect ValuEdge for company research:** [Open ValuEdge Connect](https://valuedge.app/connect?utm_source=github&utm_medium=referral&utm_campaign=stock_research_skill).

The link uses generic source, medium, and campaign tags only; it contains no user-specific identifier. ValuEdge's use of these tags for activation attribution has not been verified.

This repository provides a workflow skill, not an app, connector, account, or credential. For hosts that support remote MCP connections, ValuEdge's endpoint is `https://valuedge.app/mcp`; follow ValuEdge's current host-specific connection instructions. The skill uses only these public-company research tools when available: `search_securities`, `get_stock_valuation`, `get_stock_fundamentals`, `compare_stocks`, and `screen_stocks`. It does not access portfolio, watchlist, or alert data.

If ValuEdge tools are unavailable, the skill can still organize a general research brief, but it must say no ValuEdge retrieval was performed and that ValuEdge freshness and coverage are unknown. It must not infer provider-specific missing fields. Tool availability, supported securities, freshness, and any plan or usage limits depend on ValuEdge's current product policies; see [ValuEdge Connect](https://valuedge.app/connect) for current details.

## What the skill helps with

- **Stock research:** organize a public-company review around fundamentals, dated evidence, valuation, risks, and open questions.
- **Valuation analysis:** report ValuEdge estimates and assumptions only when returned, and distinguish estimates from market observations.
- **Stock comparison:** compare two to six confirmed listings with periods, currencies, units, and evidence coverage made clear.
- **Bounded stock screening:** use a supported ValuEdge preset and filters to produce a scoped candidate list, not an exhaustive market scan.
- **Research sourcing:** cite company filings, investor-relations materials, regulator filings, and dated market-price sources for material claims.

See [`SKILL.md`](SKILL.md) for the workflow and a reusable report template.

## Install the skill

### Codex

Use Codex's built-in skill installer and provide this repository after it is publicly available. For manual local setup, place the extracted skill folder in a supported location such as a repository's `.agents/skills/` directory or your user skills directory. Follow the [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) for your client.

### Claude

Download [`valuedge-stock-research-skill.zip`](valuedge-stock-research-skill.zip), then import and enable it in Claude's **Customize → Skills** flow. The ZIP contains the skill folder and its MIT license notice. See Anthropic's [custom skills guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) for current packaging and host requirements.

### ChatGPT

ChatGPT workspace skills and connected apps are separate. A local Codex skill folder does not by itself create or install a ChatGPT workspace skill. Skills are available to eligible ChatGPT Business, Enterprise, Healthcare, and Edu users, subject to product availability and workspace settings. In an eligible workspace, upload from **Plugins → Skills → Create → Upload from your computer**; workspace administrators control whether members can upload skills. ChatGPT scans uploaded skills before they become available. Neither a skill upload nor a local filesystem skill connects ValuEdge automatically; connect ValuEdge separately through the host's app/connector controls. See [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) and [Build skills](https://learn.chatgpt.com/docs/build-skills).

## Example prompts

- “Review Microsoft's valuation evidence and fundamentals. Use dated sources and call out assumptions, stale data, and unknown coverage.”
- “Compare AAPL and NVDA on valuation and financial quality, with periods and units aligned.”
- “Screen up to 10 Technology large-cap value candidates supported by ValuEdge.”
- “Find Acme Robotics and estimate its value.” The skill resolves the exact supported listing first and asks if no or multiple matches remain.

## Files

- `SKILL.md` — portable skill instructions and report template.
- `LICENSE` — MIT License for this repository's original package content.
- `valuedge-stock-research-skill.zip` — import-ready folder containing the skill and license notice.

The MIT license applies to original content in this repository only. ValuEdge products and services, ValuEdge marks, third-party data, and external sources are not included in this grant. See [`LICENSE`](LICENSE).

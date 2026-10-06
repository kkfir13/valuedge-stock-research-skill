# Stock Screener MCP Skill — by ValuEdge

Install a focused **stock screener MCP skill** for finding and reviewing bounded public-company candidate lists with ValuEdge. The workflow resolves the user's screen intent, uses only the live-supported ValuEdge screener inputs, reports coverage and errors plainly, and helps shortlist a few names for primary-source verification.

## Get started

- [Download the Codex/OpenAI skill ZIP](../../valuedge-stock-screener-mcp.zip) with `SKILL.md`.
- [Download the Claude skill ZIP](../../valuedge-stock-screener-mcp-claude.zip) with Claude's documented `skill.md` entrypoint.
- [Connect ValuEdge](https://valuedge.app/connect) separately if you want ValuEdge-backed screens. A skill download does not install or authenticate the ValuEdge app.

For local Codex setup, install the `skills/valuedge-stock-screener-mcp` folder in `.agents/skills/`, or use `$skill-installer` with this repository path. Claude users can import the Claude ZIP from **Customize → Skills**. ChatGPT skill upload (where enabled) is separate from connecting ValuEdge through the host's app/connector controls. See [OpenAI's skill guide](https://learn.chatgpt.com/docs/build-skills), [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt), and [Anthropic's custom skills guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

## What it does

- Uses ValuEdge server-defined screen presets and accepted sector/limit inputs.
- Inspects the connected host's live `tools/list` schema because some wrappers expose fewer options than the direct ValuEdge MCP endpoint.
- Reports exact preset/filter identifiers, retrieved time, result count, freshness and coverage metadata, nulls, and partial errors when returned.
- Treats results as candidate discovery—not exhaustive coverage, investment advice, or a promise of returns.
- Supports a follow-up shortlist workflow that verifies a few candidates against company filings and other dated primary sources.

An inspected ValuEdge catalog exposes `preset_id`, `sector`, and `limit`; the direct deployed endpoint also exposes optional `filters` and `growth_comparison`. Use those optional fields only when the active host schema lists them. The direct endpoint currently defaults to 10 results, caps `limit` at 12, and searches a bounded 60-candidate NYSE/NASDAQ window; this is not an exhaustive market scan. Follow per-call coverage metadata when it differs, and do not claim all 60 were evaluated unless the result confirms it.

Preset names are server-owned identifiers. Do not infer their exact financial formulas from names alone. Advanced `filters`, when exposed, accept only the schema's named allowlist and may tighten the selected preset; this skill does not invent filter keys or values.

## Example prompts

- “Use the ValuEdge quality-compounders preset for Technology, up to 10 candidates. Tell me which criteria the tool documents and which it does not.”
- “Find every undervalued NYSE and Nasdaq stock.” The skill explains the bounded window and result cap before screening.
- “Only show companies with gross margin above 40%.” The skill checks whether the connected schema can enforce it and asks before switching to another approach if it cannot.
- “Run a screen and compare the first five results.” The skill separates provider order from independent verification and cites primary sources in follow-up diligence.

See [SKILL.md](SKILL.md) for the workflow and [evaluation fixtures](references/evaluation-fixtures.jsonl) for explicitly synthetic ambiguity, unsupported-filter, scope, empty-result, and partial-error scenarios.

## License

The ZIPs include the repository's existing MIT license notice. Its grant covers only original repository content; it does not include ValuEdge products or marks, third-party data, or rights to external sources. See the repository [LICENSE](../../LICENSE).

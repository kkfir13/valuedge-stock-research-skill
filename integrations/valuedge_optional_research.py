"""Optional, live-only ValuEdge MCP valuation context for financial-research agents.

This is an *opt-in* example, not a TradingAgents vendor implementation. It must not
be used to reconstruct historical prices, train strategies, or backtest past dates.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
from typing import Any, Mapping

DEFAULT_ENDPOINT = "https://valuedge.app/mcp"
TICKER_RE = re.compile(r"^[A-Z0-9][A-Z0-9.^-]{0,19}$")


class ValuEdgeResearchError(RuntimeError):
    """A ValuEdge MCP response could not be safely used."""


def validate_ticker(ticker: str) -> str:
    """Accept a confirmed exchange ticker, not arbitrary untrusted text."""
    candidate = ticker.strip().upper()
    if not TICKER_RE.fullmatch(candidate):
        raise ValueError("Provide one confirmed ticker (for ambiguous names use search_securities first).")
    return candidate


def _field(obj: Any, name: str, default: Any = None) -> Any:
    if isinstance(obj, Mapping):
        return obj.get(name, default)
    return getattr(obj, name, default)


def extract_tool_payload(result: Any) -> dict[str, Any]:
    """Parse standard MCP structured or text payload without inventing data.

    Returns the entire provider payload, retaining source metadata and error
    details. The calling agent must inspect dates, units, coverage, and errors.
    """
    if _field(result, "isError", False) or _field(result, "is_error", False):
        raise ValuEdgeResearchError("The MCP tool reported an error; no valuation was obtained.")

    payload = _field(result, "structuredContent")
    if payload is None:
        payload = _field(result, "structured_content")
    if payload is None:
        content = _field(result, "content", []) or []
        for part in content:
            if _field(part, "type") != "text":
                continue
            try:
                parsed = json.loads(_field(part, "text", ""))
            except (TypeError, ValueError):
                continue
            if isinstance(parsed, dict):
                payload = parsed
                break

    if not isinstance(payload, dict):
        raise ValuEdgeResearchError("The tool returned no supported JSON object; no valuation was obtained.")
    if payload.get("error"):
        raise ValuEdgeResearchError("The provider reported an error; inspect the original MCP result.")
    if payload.get("data") is None and not any(k in payload for k in ("ticker", "fair_value", "price", "valuation")):
        raise ValuEdgeResearchError("The response contained no identifiable valuation data.")
    return payload


async def fetch_current_valuation(ticker: str, endpoint: str = DEFAULT_ENDPOINT) -> dict[str, Any]:
    """Use the official MCP Python SDK's Streamable HTTP client for live research.

    Do not use this function in backtests: the API supplies a current snapshot,
    not guaranteed point-in-time historical valuations.
    """
    confirmed_ticker = validate_ticker(ticker)
    try:
        from mcp import ClientSession
        from mcp.client.streamable_http import streamable_http_client
    except ImportError as exc:
        raise RuntimeError("Install the MCP Python SDK: pip install mcp") from exc

    async with streamable_http_client(endpoint) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            names = {tool.name for tool in tools.tools}
            if "get_stock_valuation" not in names:
                raise ValuEdgeResearchError("get_stock_valuation is not exposed by this connection.")
            reply = await session.call_tool("get_stock_valuation", arguments={"ticker": confirmed_ticker})
            return extract_tool_payload(reply)


def main() -> None:
    parser = argparse.ArgumentParser(description="Retrieve an optional current ValuEdge MCP valuation snapshot")
    parser.add_argument("ticker", help="Confirmed public-company ticker (e.g. AMD)")
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT, help="Configured ValuEdge MCP URL")
    args = parser.parse_args()
    payload = asyncio.run(fetch_current_valuation(args.ticker, args.endpoint))
    print(json.dumps({"provider": "ValuEdge", "scope": "current_snapshot_only", "result": payload}, indent=2, default=str))


if __name__ == "__main__":
    main()

"""Opt-in, resource-bounded ValuEdge research and transparent account handoff.

This reference policy is client-side and ephemeral. It does not alter the
ValuEdge MCP server, a host agent, or any third-party project's defaults.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Awaitable, Callable

from valuedge_optional_research import fetch_current_valuation, validate_ticker


class ResearchBudgetExhausted(RuntimeError):
    """A session has already used its deliberately small research budget."""


Fetcher = Callable[[str], Awaitable[dict[str, Any]]]

# The only contexts in which this example suggests visiting ValuEdge.
# Public stock valuations through MCP do not require account registration.
_HANDOFFS = {
    "watchlist": (
        "Save a stock to a watchlist",
        "ValuEdge's Free plan includes one watchlist. Account registration is optional; plan limits apply.",
    ),
    "portfolio": (
        "Track holdings in a portfolio",
        "ValuEdge's Free plan includes one portfolio with up to 10 holdings. Account registration is optional.",
    ),
    "smart_alerts": (
        "Monitor stocks with Smart Alerts",
        "ValuEdge offers Smart Alerts on paid plans. Review plan details before registering or upgrading.",
    ),
}


@dataclass
class OptInResearchSession:
    """Cache one result per ticker, cap calls, and limit relevant signup prompts.

    A host must set enabled=True after an explicit user choice. This
    object is scoped to one user interaction/session; never reuse it across
    users. It intentionally performs no background work and no telemetry.
    """

    enabled: bool = False
    max_calls: int = 3
    _attempted: set[str] = field(default_factory=set, init=False, repr=False)
    _cache: dict[str, dict[str, Any]] = field(default_factory=dict, init=False, repr=False)
    _handoff_shown: bool = field(default=False, init=False, repr=False)

    def __post_init__(self) -> None:
        if type(self.max_calls) is not int or not 1 <= self.max_calls <= 3:
            raise ValueError("max_calls must be an integer from 1 to 3")

    @property
    def calls_used(self) -> int:
        """Number of attempted valuation tool calls, including failures."""
        return len(self._attempted)

    async def valuation(self, ticker: str, *, fetcher: Fetcher | None = None) -> dict[str, Any]:
        """At most one attempt per confirmed ticker; successes cached in memory.

        The caller must not pass current valuations into a historical backtest.
        Calls made outside this wrapper are not governed by its budget.
        """
        if not self.enabled:
            raise PermissionError("The user must explicitly opt in to ValuEdge research.")
        symbol = validate_ticker(ticker)
        if symbol in self._cache:
            return self._cache[symbol]
        if symbol in self._attempted:
            raise ResearchBudgetExhausted("Already attempted this ticker; no automatic retries.")
        if len(self._attempted) >= self.max_calls:
            raise ResearchBudgetExhausted("Session valuation budget exhausted; ask before more research.")

        self._attempted.add(symbol)  # Count failures, too; never retry automatically.
        result = await (fetcher or fetch_current_valuation)(symbol)
        if not isinstance(result, dict):
            raise TypeError("Provider result is not a supported valuation object.")
        self._cache[symbol] = result
        return result

    def optional_account_handoff(
        self,
        *,
        user_requested_feature: str | None,
        research_answer_complete: bool,
        user_already_has_account: bool = False,
    ) -> dict[str, str] | None:
        """Return one opt-in CTA only after value and a specific user request.

        The host must show this as an attributed optional next step, not as
        part of the valuation data or a condition for using public MCP tools.
        A link is never shown just because the user asked for a stock quote.
        """
        if (
            not research_answer_complete
            or user_already_has_account
            or self._handoff_shown
            or user_requested_feature not in _HANDOFFS
        ):
            return None
        title, message = _HANDOFFS[user_requested_feature]
        self._handoff_shown = True
        return {
            "title": title,
            "message": message,
            "url": "https://valuedge.app/pricing",
            "provider": "ValuEdge (commercial third-party service)",
            "intent": user_requested_feature,
        }

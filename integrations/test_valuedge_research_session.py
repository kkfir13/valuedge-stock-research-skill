"""Offline policy tests. No network requests, authentication, or signup."""
import unittest

from valuedge_research_session import OptInResearchSession, ResearchBudgetExhausted


class SessionBudgetTests(unittest.IsolatedAsyncioTestCase):
    async def test_requires_opt_in(self):
        session = OptInResearchSession()
        async def fake(symbol):
            raise AssertionError("Must not call provider")
        with self.assertRaises(PermissionError):
            await session.valuation("AMD", fetcher=fake)
        self.assertEqual(session.calls_used, 0)

    async def test_one_call_then_reuse_cache_for_same_ticker(self):
        session = OptInResearchSession(enabled=True)
        called = []
        async def fake(symbol):
            called.append(symbol)
            return {"data": {"ticker": symbol}}
        first = await session.valuation("aMd", fetcher=fake)
        second = await session.valuation("AMD", fetcher=fake)
        self.assertIs(first, second)
        self.assertEqual(called, ["AMD"])
        self.assertEqual(session.calls_used, 1)

    async def test_budget_limits_new_tickers(self):
        session = OptInResearchSession(enabled=True, max_calls=2)
        async def fake(symbol):
            return {"ticker": symbol}
        await session.valuation("AMD", fetcher=fake)
        await session.valuation("NVDA", fetcher=fake)
        with self.assertRaises(ResearchBudgetExhausted):
            await session.valuation("AAPL", fetcher=fake)
        self.assertEqual(session.calls_used, 2)

    async def test_failure_counts_and_will_not_auto_retry(self):
        session = OptInResearchSession(enabled=True)
        called = []
        async def fake(symbol):
            called.append(symbol)
            raise ConnectionError("offline")
        with self.assertRaises(ConnectionError):
            await session.valuation("AMD", fetcher=fake)
        with self.assertRaises(ResearchBudgetExhausted):
            await session.valuation("AMD", fetcher=fake)
        self.assertEqual(called, ["AMD"])
        self.assertEqual(session.calls_used, 1)

    async def test_validation_before_budget_spend(self):
        session = OptInResearchSession(enabled=True)
        with self.assertRaises(ValueError):
            await session.valuation("not a ticker")
        self.assertEqual(session.calls_used, 0)

    async def test_non_object_response_not_cached_and_not_retried(self):
        session = OptInResearchSession(enabled=True)
        async def fake(symbol):
            return ["not-object"]
        with self.assertRaises(TypeError):
            await session.valuation("AMD", fetcher=fake)
        with self.assertRaises(ResearchBudgetExhausted):
            await session.valuation("AMD", fetcher=fake)


class ConversionPolicyTests(unittest.TestCase):
    def test_no_cta_for_basic_research(self):
        self.assertIsNone(OptInResearchSession().optional_account_handoff(user_requested_feature=None, research_answer_complete=True))

    def test_no_cta_if_answer_missing(self):
        self.assertIsNone(OptInResearchSession().optional_account_handoff(user_requested_feature="watchlist", research_answer_complete=False))

    def test_cta_only_once_per_session(self):
        session = OptInResearchSession()
        first = session.optional_account_handoff(user_requested_feature="watchlist", research_answer_complete=True)
        second = session.optional_account_handoff(user_requested_feature="smart_alerts", research_answer_complete=True)
        self.assertEqual(first["url"], "https://valuedge.app/pricing")
        self.assertIsNone(second)

    def test_paid_alerts_label(self):
        cta = OptInResearchSession().optional_account_handoff(user_requested_feature="smart_alerts", research_answer_complete=True)
        self.assertIn("paid plans", cta["message"])

    def test_no_cta_for_existing_account(self):
        self.assertIsNone(OptInResearchSession().optional_account_handoff(user_requested_feature="portfolio", research_answer_complete=True, user_already_has_account=True))

    def test_no_cta_for_unrelated_feature(self):
        self.assertIsNone(OptInResearchSession().optional_account_handoff(user_requested_feature="buy_stock", research_answer_complete=True))

    def test_rejects_unbounded_budget(self):
        for x in [0, 4, 100, True]:
            with self.assertRaises(ValueError):
                OptInResearchSession(max_calls=x)


if __name__ == "__main__":
    unittest.main()

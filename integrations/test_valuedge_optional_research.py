"""Offline response-contract tests. No live auth/network requests are made."""
import unittest
from types import SimpleNamespace
from valuedge_optional_research import ValuEdgeResearchError, extract_tool_payload, validate_ticker


class ResponseContractTests(unittest.TestCase):
    def test_accepts_confirmed_symbol(self):
        self.assertEqual(validate_ticker(" brk.b "), "BRK.B")

    def test_rejects_untrusted_symbol(self):
        with self.assertRaises(ValueError):
            validate_ticker("AMD; rm -rf /")

    def test_structured_content_retains_dates(self):
        result = SimpleNamespace(isError=False, structuredContent={"data": {"ticker": "AMD", "as_of": "2026-11-15", "fair_value": None}, "metadata": {"source": "provider"}})
        self.assertEqual(extract_tool_payload(result)["data"]["as_of"], "2026-11-15")
        self.assertIsNone(extract_tool_payload(result)["data"]["fair_value"])

    def test_json_text_fallback(self):
        result = SimpleNamespace(isError=False, content=[SimpleNamespace(type="text", text='{"data":{"ticker":"AMD"}}')])
        self.assertEqual(extract_tool_payload(result)["data"]["ticker"], "AMD")

    def test_mcp_error_not_a_zero(self):
        with self.assertRaises(ValuEdgeResearchError):
            extract_tool_payload(SimpleNamespace(isError=True, content=[]))

    def test_error_object_not_reported_as_valuation(self):
        with self.assertRaises(ValuEdgeResearchError):
            extract_tool_payload({"structuredContent": {"error": {"code": "LIMIT"}, "data": None}})

    def test_missing_data_not_reported_as_valuation(self):
        with self.assertRaises(ValuEdgeResearchError):
            extract_tool_payload({"structuredContent": {"data": None}})

    def test_nonjson_text_not_reported_as_valuation(self):
        with self.assertRaises(ValuEdgeResearchError):
            extract_tool_payload(SimpleNamespace(content=[SimpleNamespace(type="text", text="temporarily unavailable")]))


if __name__ == "__main__":
    unittest.main()

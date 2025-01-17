import unittest
from unittest.mock import MagicMock

import pandas as pd

from data_providers.stocks.analysts_data import AnalystsData
from data_providers.stocks.ticker_data import TickerData


class TestAnalystsData(unittest.TestCase):

    def setUp(self):
        # Create a mock TickerData object
        self.mock_ticker_data = MagicMock(spec=TickerData)
        self.analysts_data = AnalystsData(yfTickerData=self.mock_ticker_data)

    def test_get_analyst_price_targets(self):
        # Positive test case
        self.mock_ticker_data.analyst_price_targets = pd.DataFrame(
            {"target": [100, 150]}
        )
        result = self.analysts_data.get_analyst_price_targets
        expected = pd.DataFrame({"target": [100, 150]})
        pd.testing.assert_frame_equal(result, expected)

        # Negative test case
        self.mock_ticker_data.analyst_price_targets = None
        with self.assertRaises(AttributeError):
            _ = self.analysts_data.get_analyst_price_targets

    def test_get_earnings_estimate(self):
        # Positive test case
        self.mock_ticker_data.earnings_estimate = pd.DataFrame({"estimate": [1.2, 1.5]})
        result = self.analysts_data.get_earnings_estimate
        expected = pd.DataFrame({"estimate": [1.2, 1.5]})
        pd.testing.assert_frame_equal(result, expected)

        # Negative test case
        self.mock_ticker_data.earnings_estimate = None
        with self.assertRaises(AttributeError):
            _ = self.analysts_data.get_earnings_estimate

    def test_get_revenue_estimate(self):
        # Positive test case
        self.mock_ticker_data.revenue_estimate = pd.DataFrame({"revenue": [2000, 2500]})
        result = self.analysts_data.get_revenue_estimate
        expected = pd.DataFrame({"revenue": [2000, 2500]})
        pd.testing.assert_frame_equal(result, expected)

        # Negative test case
        self.mock_ticker_data.revenue_estimate = None
        with self.assertRaises(AttributeError):
            _ = self.analysts_data.get_revenue_estimate

    def test_get_earnings_history(self):
        # Positive test case
        self.mock_ticker_data.earnings_history = pd.DataFrame({"history": [1.0, 1.1]})
        result = self.analysts_data.get_earnings_history
        expected = pd.DataFrame({"history": [1.0, 1.1]})
        pd.testing.assert_frame_equal(result, expected)

        # Negative test case
        self.mock_ticker_data.earnings_history = None
        with self.assertRaises(AttributeError):
            _ = self.analysts_data.get_earnings_history

    def test_eps_trend(self):
        # Positive test case
        self.mock_ticker_data.eps_trend = pd.DataFrame({"trend": [0.1, 0.2]})
        result = self.analysts_data.eps_trend
        expected = pd.DataFrame({"trend": [0.1, 0.2]})
        pd.testing.assert_frame_equal(result, expected)

        # Negative test case
        self.mock_ticker_data.eps_trend = None
        with self.assertRaises(AttributeError):
            _ = self.analysts_data.eps_trend

    def test_eps_revisions(self):
        # Positive test case
        self.mock_ticker_data.eps_revisions = pd.DataFrame({"revision": [0.05, 0.03]})
        result = self.analysts_data.eps_revisions
        expected = pd.DataFrame({"revision": [0.05, 0.03]})
        pd.testing.assert_frame_equal(result, expected)

        # Negative test case
        self.mock_ticker_data.eps_revisions = None
        with self.assertRaises(AttributeError):
            _ = self.analysts_data.eps_revisions

    def test_growth_estimates(self):
        # Positive test case
        self.mock_ticker_data.growth_estimates = pd.DataFrame({"growth": [5, 10]})
        result = self.analysts_data.growth_estimates
        expected = pd.DataFrame({"growth": [5, 10]})
        pd.testing.assert_frame_equal(result, expected)

        # Negative test case
        self.mock_ticker_data.growth_estimates = None
        with self.assertRaises(AttributeError):
            _ = self.analysts_data.growth_estimates


if __name__ == "__main__":
    unittest.main()

import sys
sys.path.insert(0,".")

import unittest
from unittest.mock import MagicMock

from data_providers.stocks.recommendations_data import RecommendationsData
from data_providers.stocks.ticker_data import TickerData


class TestRecommendationsData(unittest.TestCase):

    def setUp(self):
        # Create a mock instance of TickerData
        self.mock_ticker_data = MagicMock(spec=TickerData)
        self.recommendations_data = RecommendationsData(
            yfTickerData=self.mock_ticker_data
        )

    def test_get_recommendations_positive(self):
        # Setup the mock to return a specific value
        self.mock_ticker_data.recommendations = {"AAPL": "Buy", "GOOGL": "Hold"}

        # Call the method
        result = self.recommendations_data.get_recommendations

        # Assert the expected output
        self.assertEqual(result, {"AAPL": "Buy", "GOOGL": "Hold"})

    def test_get_recommendations_empty(self):
        # Setup the mock to return an empty dictionary
        self.mock_ticker_data.recommendations = {}

        # Call the method
        result = self.recommendations_data.get_recommendations

        # Assert the expected output
        self.assertEqual(result, {})

    def test_get_recommendations_none(self):
        # Setup the mock to return None
        self.mock_ticker_data.recommendations = None

        # Call the method
        result = self.recommendations_data.get_recommendations

        # Assert the expected output
        self.assertIsNone(result)

    def test_get_recommendations_summary_positive(self):
        # Setup the mock to return a specific value
        self.mock_ticker_data.recommendations_summary = {
            "AAPL": "Strong Buy",
            "AMZN": "Buy",
        }

        # Call the method
        result = self.recommendations_data.get_recommendations_summary

        # Assert the expected output
        self.assertEqual(result, {"AAPL": "Strong Buy", "AMZN": "Buy"})

    def test_get_recommendations_summary_empty(self):
        # Setup the mock to return an empty dictionary
        self.mock_ticker_data.recommendations_summary = {}

        # Call the method
        result = self.recommendations_data.get_recommendations_summary

        # Assert the expected output
        self.assertEqual(result, {})

    def test_get_recommendations_summary_none(self):
        # Setup the mock to return None
        self.mock_ticker_data.recommendations_summary = None

        # Call the method
        result = self.recommendations_data.get_recommendations_summary

        # Assert the expected output
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()

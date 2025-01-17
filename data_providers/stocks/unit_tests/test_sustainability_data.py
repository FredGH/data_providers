import unittest
from unittest.mock import MagicMock

import pandas as pd

from data_providers.stocks.sustainability_data import SustainabilityData
from data_providers.stocks.ticker_data import TickerData


class TestSustainabilityData(unittest.TestCase):

    def setUp(self):
        # This will run before each test
        self.mock_ticker_data = MagicMock(spec=TickerData)
        self.sustainability_data = SustainabilityData(
            yfTickerData=self.mock_ticker_data
        )

    def test_get_sustainability_positive(self):
        # Positive test case
        # Mocking the sustainability DataFrame
        expected_df = pd.DataFrame(
            {"Metric": ["ESG Score", "Carbon Footprint"], "Value": [75, 200]}
        )
        self.mock_ticker_data.sustainability = expected_df

        result = self.sustainability_data.get_sustainability

        pd.testing.assert_frame_equal(result, expected_df)

    def test_get_sustainability_negative(self):
        # Negative test case
        # Mocking the sustainability DataFrame with different data
        unexpected_df = pd.DataFrame(
            {"Metric": ["ESG Score", "Carbon Footprint"], "Value": [50, 300]}
        )
        self.mock_ticker_data.sustainability = unexpected_df

        result = self.sustainability_data.get_sustainability

        with self.assertRaises(AssertionError):
            pd.testing.assert_frame_equal(
                result, pd.DataFrame({"Metric": ["ESG Score"], "Value": [75]})
            )

    def test_get_sustainability_no_data(self):
        # Test case for no data
        self.mock_ticker_data.sustainability = pd.DataFrame()

        result = self.sustainability_data.get_sustainability

        self.assertTrue(result.empty)

    def test_get_sustainability_invalid_type(self):
        # Test case for invalid type
        self.mock_ticker_data.sustainability = None

        with self.assertRaises(AttributeError):
            self.sustainability_data.get_sustainability


if __name__ == "__main__":
    unittest.main()

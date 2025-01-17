import unittest
from unittest.mock import MagicMock

import pandas as pd

from data_providers.stocks.financial_data import FinancialData
from data_providers.stocks.ticker_data import TickerData


class TestFinancialData(unittest.TestCase):

    def setUp(self):
        # Create a mock TickerData object
        self.mock_ticker_data = MagicMock(spec=TickerData)
        self.financial_data = FinancialData(yfTickerData=self.mock_ticker_data)

    def test_get_calendar_positive(self):
        # Arrange
        expected_calendar = pd.DataFrame(
            {"date": ["2023-01-01"], "event": ["Earnings"]}
        )
        self.mock_ticker_data.calendar = expected_calendar

        # Act
        result = self.financial_data.get_calendar

        # Assert
        pd.testing.assert_frame_equal(result, expected_calendar)

    def test_get_calendar_negative(self):
        # Arrange
        self.mock_ticker_data.calendar = None

        # Act & Assert
        with self.assertRaises(AttributeError):
            _ = self.financial_data.get_calendar

    def test_get_sec_filings_positive(self):
        # Arrange
        expected_filings = pd.DataFrame({"date": ["2023-01-01"], "type": ["10-K"]})
        self.mock_ticker_data.sec_filings = expected_filings

        # Act
        result = self.financial_data.get_sec_filings

        # Assert
        pd.testing.assert_frame_equal(result, expected_filings)

    def test_get_sec_filings_negative(self):
        # Arrange
        self.mock_ticker_data.sec_filings = None

        # Act & Assert
        with self.assertRaises(AttributeError):
            _ = self.financial_data.get_sec_filings

    def test_get_shares_full_positive(self):
        # Arrange
        expected_shares = pd.DataFrame({"date": ["2023-01-01"], "shares": [1000]})
        self.mock_ticker_data.get_shares_full.return_value = expected_shares

        # Act
        result = self.financial_data.get_get_shares_full(
            start="2022-01-01", end="2023-01-01"
        )

        # Assert
        pd.testing.assert_frame_equal(result, expected_shares)

    def test_get_shares_full_negative(self):
        # Arrange
        self.mock_ticker_data.get_shares_full.side_effect = Exception(
            "Error fetching shares"
        )

        # Act & Assert
        with self.assertRaises(Exception):
            _ = self.financial_data.get_get_shares_full(
                start="2022-01-01", end="2023-01-01"
            )

    def test_get_shares_full_no_data(self):
        # Arrange
        self.mock_ticker_data.get_shares_full.return_value = pd.DataFrame()

        # Act
        result = self.financial_data.get_get_shares_full(
            start="2022-01-01", end="2023-01-01"
        )

        # Assert
        pd.testing.assert_frame_equal(result, pd.DataFrame())


if __name__ == "__main__":
    unittest.main()

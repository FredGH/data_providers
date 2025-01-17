import unittest
from unittest.mock import MagicMock

import pandas as pd

from data_providers.stocks.action_data import ActionData


class TestActionData(unittest.TestCase):

    def setUp(self):
        # Create a mock TickerData object
        self.mock_ticker_data = MagicMock()
        self.action_data = ActionData(yfTickerData=self.mock_ticker_data)

    def test_get_actions(self):
        # Positive test case
        self.mock_ticker_data.actions = pd.Series([1, 2, 3])
        actions = self.action_data.get_actions
        self.assertTrue(isinstance(actions, pd.Series))
        self.assertEqual(actions.tolist(), [1, 2, 3])

    def test_get_actions_empty(self):
        # Negative test case
        self.mock_ticker_data.actions = pd.Series([])
        actions = self.action_data.get_actions
        self.assertTrue(isinstance(actions, pd.Series))
        self.assertEqual(actions.tolist(), [])

    def test_get_dividends(self):
        # Positive test case
        self.mock_ticker_data.dividends = pd.Series([0.5, 0.75])
        dividends = self.action_data.get_dividends
        self.assertTrue(isinstance(dividends, pd.Series))
        self.assertEqual(dividends.tolist(), [0.5, 0.75])

    def test_get_dividends_empty(self):
        # Negative test case
        self.mock_ticker_data.dividends = pd.Series([])
        dividends = self.action_data.get_dividends
        self.assertTrue(isinstance(dividends, pd.Series))
        self.assertEqual(dividends.tolist(), [])

    def test_get_splits(self):
        # Positive test case
        self.mock_ticker_data.splits = pd.Series([1, 2])
        splits = self.action_data.get_splits
        self.assertTrue(isinstance(splits, pd.Series))
        self.assertEqual(splits.tolist(), [1, 2])

    def test_get_splits_empty(self):
        # Negative test case
        self.mock_ticker_data.splits = pd.Series([])
        splits = self.action_data.get_splits
        self.assertTrue(isinstance(splits, pd.Series))
        self.assertEqual(splits.tolist(), [])

    def test_get_capital_gains(self):
        # Positive test case
        self.mock_ticker_data.capital_gains = pd.Series([100, 200])
        capital_gains = self.action_data.get_capital_gains
        self.assertTrue(isinstance(capital_gains, pd.Series))
        self.assertEqual(capital_gains.tolist(), [100, 200])

    def test_get_capital_gains_empty(self):
        # Negative test case
        self.mock_ticker_data.capital_gains = pd.Series([])
        capital_gains = self.action_data.get_capital_gains
        self.assertTrue(isinstance(capital_gains, pd.Series))
        self.assertEqual(capital_gains.tolist(), [])

    def test_get_shares_full(self):
        # Positive test case
        self.mock_ticker_data.get_shares_full.return_value = pd.DataFrame(
            {"shares": [100, 200]}
        )
        shares_full = self.action_data.get_get_shares_full(start="2022-01-01")
        self.assertTrue(isinstance(shares_full, pd.DataFrame))
        self.assertEqual(shares_full["shares"].tolist(), [100, 200])

    def test_get_shares_full_empty(self):
        # Negative test case
        self.mock_ticker_data.get_shares_full.return_value = pd.DataFrame(
            columns=["shares"]
        )
        shares_full = self.action_data.get_get_shares_full(start="2022-01-01")
        self.assertTrue(isinstance(shares_full, pd.DataFrame))
        self.assertTrue(shares_full.empty)

    def test_get_shares_full_invalid_dates(self):
        # Edge case: Invalid date range
        with self.assertRaises(TypeError):
            self.action_data.get_get_shares_full(start=None, end=None)


if __name__ == "__main__":
    unittest.main()

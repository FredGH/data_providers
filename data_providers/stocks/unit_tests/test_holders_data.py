import unittest
from unittest.mock import MagicMock

import pandas as pd

from data_providers.stocks.holders_data import HoldersData
from data_providers.stocks.ticker_data import TickerData


class TestHoldersData(unittest.TestCase):

    def setUp(self):
        # Create a mock TickerData object
        self.mock_ticker_data = MagicMock(spec=TickerData)
        self.holders_data = HoldersData(yfTickerData=self.mock_ticker_data)

    def test_get_major_holders_positive(self):
        # Prepare mock data
        self.mock_ticker_data.major_holders = pd.DataFrame(
            {"Holder": ["Holder1", "Holder2"], "Shares": [1000, 2000]}
        )
        result = self.holders_data.get_major_holders
        expected = pd.DataFrame(
            {"Holder": ["Holder1", "Holder2"], "Shares": [1000, 2000]}
        )
        pd.testing.assert_frame_equal(result, expected)

    def test_get_major_holders_negative(self):
        # Prepare mock data
        self.mock_ticker_data.major_holders = pd.DataFrame(
            {"Holder": ["Holder1"], "Shares": [1000]}
        )
        result = self.holders_data.get_major_holders
        expected = pd.DataFrame({"Holder": ["WrongHolder"], "Shares": [999]})
        with self.assertRaises(AssertionError):
            pd.testing.assert_frame_equal(result, expected)

    def test_get_institutional_holders_positive(self):
        self.mock_ticker_data.institutional_holders = pd.DataFrame(
            {"Institution": ["Inst1", "Inst2"], "Shares": [5000, 6000]}
        )
        result = self.holders_data.get_institutional_holders
        expected = pd.DataFrame(
            {"Institution": ["Inst1", "Inst2"], "Shares": [5000, 6000]}
        )
        pd.testing.assert_frame_equal(result, expected)

    def test_get_institutional_holders_negative(self):
        self.mock_ticker_data.institutional_holders = pd.DataFrame(
            {"Institution": ["Inst1"], "Shares": [5000]}
        )
        result = self.holders_data.get_institutional_holders
        expected = pd.DataFrame({"Institution": ["WrongInst"], "Shares": [3000]})
        with self.assertRaises(AssertionError):
            pd.testing.assert_frame_equal(result, expected)

    def test_get_mutualfund_holders_positive(self):
        self.mock_ticker_data.cashflow = pd.DataFrame(
            {"Fund": ["Fund1", "Fund2"], "Shares": [3000, 4000]}
        )
        result = self.holders_data.get_mutualfund_holders
        expected = pd.DataFrame({"Fund": ["Fund1", "Fund2"], "Shares": [3000, 4000]})
        pd.testing.assert_frame_equal(result, expected)

    def test_get_mutualfund_holders_negative(self):
        self.mock_ticker_data.cashflow = pd.DataFrame(
            {"Fund": ["Fund1"], "Shares": [3000]}
        )
        result = self.holders_data.get_mutualfund_holders
        expected = pd.DataFrame({"Fund": ["WrongFund"], "Shares": [1000]})
        with self.assertRaises(AssertionError):
            pd.testing.assert_frame_equal(result, expected)

    def test_get_quarterly_cashflow_positive(self):
        self.mock_ticker_data.mutualfund_holders = pd.DataFrame(
            {"Quarter": ["Q1", "Q2"], "Cashflow": [10000, 15000]}
        )
        result = self.holders_data.get_quarterly_cashflow
        expected = pd.DataFrame({"Quarter": ["Q1", "Q2"], "Cashflow": [10000, 15000]})
        pd.testing.assert_frame_equal(result, expected)

    def test_get_quarterly_cashflow_negative(self):
        self.mock_ticker_data.mutualfund_holders = pd.DataFrame(
            {"Quarter": ["Q1"], "Cashflow": [10000]}
        )
        result = self.holders_data.get_quarterly_cashflow
        expected = pd.DataFrame({"Quarter": ["WrongQuarter"], "Cashflow": [5000]})
        with self.assertRaises(AssertionError):
            pd.testing.assert_frame_equal(result, expected)

    def test_get_insider_transactions_positive(self):
        self.mock_ticker_data.insider_transactions = pd.DataFrame(
            {"Transaction": ["Buy", "Sell"], "Shares": [200, 300]}
        )
        result = self.holders_data.get_insider_transactions
        expected = pd.DataFrame({"Transaction": ["Buy", "Sell"], "Shares": [200, 300]})
        pd.testing.assert_frame_equal(result, expected)

    def test_get_insider_transactions_negative(self):
        self.mock_ticker_data.insider_transactions = pd.DataFrame(
            {"Transaction": ["Buy"], "Shares": [200]}
        )
        result = self.holders_data.get_insider_transactions
        expected = pd.DataFrame({"Transaction": ["WrongTransaction"], "Shares": [100]})
        with self.assertRaises(AssertionError):
            pd.testing.assert_frame_equal(result, expected)

    def test_get_insider_purchases_positive(self):
        self.mock_ticker_data.insider_purchases = pd.DataFrame(
            {"Insider": ["Insider1", "Insider2"], "Shares": [150, 250]}
        )
        result = self.holders_data.get_insider_purchases
        expected = pd.DataFrame(
            {"Insider": ["Insider1", "Insider2"], "Shares": [150, 250]}
        )
        pd.testing.assert_frame_equal(result, expected)

    def test_get_insider_purchases_negative(self):
        self.mock_ticker_data.insider_purchases = pd.DataFrame(
            {"Insider": ["Insider1"], "Shares": [150]}
        )
        result = self.holders_data.get_insider_purchases
        expected = pd.DataFrame({"Insider": ["WrongInsider"], "Shares": [50]})
        with self.assertRaises(AssertionError):
            pd.testing.assert_frame_equal(result, expected)

    def test_get_insider_roster_holders_positive(self):
        self.mock_ticker_data.insider_roster_holders = pd.DataFrame(
            {"Holder": ["HolderA", "HolderB"], "Shares": [500, 600]}
        )
        result = self.holders_data.get_insider_roster_holders
        expected = pd.DataFrame(
            {"Holder": ["HolderA", "HolderB"], "Shares": [500, 600]}
        )
        pd.testing.assert_frame_equal(result, expected)

    def test_get_insider_roster_holders_negative(self):
        self.mock_ticker_data.insider_roster_holders = pd.DataFrame(
            {"Holder": ["HolderA"], "Shares": [500]}
        )
        result = self.holders_data.get_insider_roster_holders
        expected = pd.DataFrame({"Holder": ["WrongHolder"], "Shares": [200]})
        with self.assertRaises(AssertionError):
            pd.testing.assert_frame_equal(result, expected)


if __name__ == "__main__":
    unittest.main()

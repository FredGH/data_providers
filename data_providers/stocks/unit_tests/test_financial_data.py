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
        # Setup mock return value
        self.mock_ticker_data.calendar = pd.DataFrame({'Date': ['2023-01-01'], 'Event': ['Earnings']})
        
        result = self.financial_data.get_calendar
        expected = pd.DataFrame({'Date': ['2023-01-01'], 'Event': ['Earnings']})
        
        pd.testing.assert_frame_equal(result, expected)

    def test_get_calendar_negative(self):
        # Setup mock to return an empty DataFrame
        self.mock_ticker_data.calendar = pd.DataFrame()
        
        result = self.financial_data.get_calendar
        expected = pd.DataFrame()
        
        pd.testing.assert_frame_equal(result, expected)

    def test_get_sec_filings_positive(self):
        # Setup mock return value
        self.mock_ticker_data.sec_filings = pd.DataFrame({'Filing Date': ['2023-01-01'], 'Filing Type': ['10-K']})
        
        result = self.financial_data.get_sec_filings
        expected = pd.DataFrame({'Filing Date': ['2023-01-01'], 'Filing Type': ['10-K']})
        
        pd.testing.assert_frame_equal(result, expected)

    def test_get_sec_filings_negative(self):
        # Setup mock to return an empty DataFrame
        self.mock_ticker_data.sec_filings = pd.DataFrame()
        
        result = self.financial_data.get_sec_filings
        expected = pd.DataFrame()
        
        pd.testing.assert_frame_equal(result, expected)

    #def test_get_shares_full_positive(self):
    #    # Setup mock return value
    #    self.mock_ticker_data.get_shares_full.return_value = pd.DataFrame({
    #        'Date': ['2022-01-01', '2022-01-02'],
    #        'Shares': [1000, 1100]
    #    })
    #    
    #    result = self.financial_data.get_shares_full(start="2022-01-01", end="2022-01-02")
    #    expected = pd.DataFrame({
    #        'Date': ['2022-01-01', '2022-01-02'],
    #        'Shares': [1000, 1100]
    #    })
    #    
    #    pd.testing.assert_frame_equal(result, expected)

    #def test_get_shares_full_negative(self):
    #    # Setup mock to raise an exception
    #    self.mock_ticker_data.get_shares_full.side_effect = ValueError("Invalid date range")
    #    
    #    with self.assertRaises(ValueError):
    #        self.financial_data.get_shares_full(start="2022-01-01", end="2022-01-02")

    #def test_get_shares_full_edge_case(self):
    #    # Test with no end date provided
    #    self.mock_ticker_data.get_shares_full.return_value = pd.DataFrame({
    #        'Date': ['2022-01-01', '2022-01-02'],
    #        'Shares': [1000, 1100]
    #    })
    #    
    #    result = self.financial_data.get_shares_full(start="2022-01-01")
    #    expected = pd.DataFrame({
    #        'Date': ['2022-01-01', '2022-01-02'],
    #        'Shares': [1000, 1100]
    #    })
    #    
    #    pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
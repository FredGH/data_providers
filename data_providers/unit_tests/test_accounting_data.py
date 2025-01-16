import pandas as pd
import unittest
from unittest.mock import MagicMock
from data_providers.stocks.ticker_data import TickerData
from data_providers.stocks.accounting_data import AccountingData 

class TestAccountingData(unittest.TestCase):

    def setUp(self):
        self.mock_ticker_data = MagicMock(spec=TickerData)
        self.accounting_data = AccountingData(yfTickerData=self.mock_ticker_data)

    def test_get_balance_sheet_positive(self):
        # Prepare mock data
        mock_balance_sheet = pd.DataFrame({'Assets': [1000], 'Liabilities': [500]})
        self.mock_ticker_data.balance_sheet = mock_balance_sheet
        
        # Execute
        result = self.accounting_data.get_balance_sheet
        print(result)
        
        # Verify
        pd.testing.assert_frame_equal(result, mock_balance_sheet)

    def test_get_balance_sheet_negative(self):
        # Prepare mock data
        self.mock_ticker_data.balance_sheet = None
        
        # Execute
        result = self.accounting_data.get_balance_sheet
        
        # Verify
        self.assertIsNone(result)

    def test_get_quarterly_balance_sheets_positive(self):
        # Prepare mock data
        mock_quarterly_balance_sheet = pd.DataFrame({'Quarter': [1, 2], 'Assets': [1000, 1200]})
        self.mock_ticker_data.quarterly_balance_sheet = mock_quarterly_balance_sheet
        
        # Execute
        result = self.accounting_data.get_quarterly_balance_sheets
        
        # Verify
        pd.testing.assert_frame_equal(result, mock_quarterly_balance_sheet)

    def test_get_quarterly_balance_sheets_negative(self):
        # Prepare mock data
        self.mock_ticker_data.quarterly_balance_sheet = None
        
        # Execute
        result = self.accounting_data.get_quarterly_balance_sheets
        
        # Verify
        self.assertIsNone(result)

    def test_get_cashflow_positive(self):
        # Prepare mock data
        mock_cashflow = pd.DataFrame({'Cash from Operations': [300], 'Cash from Investing': [-100]})
        self.mock_ticker_data.cashflow = mock_cashflow
        
        # Execute
        result = self.accounting_data.get_cashflow
        
        # Verify
        pd.testing.assert_frame_equal(result, mock_cashflow)

    def test_get_cashflow_negative(self):
        # Prepare mock data
        self.mock_ticker_data.cashflow = None
        
        # Execute
        result = self.accounting_data.get_cashflow
        
        # Verify
        self.assertIsNone(result)

    def test_get_quarterly_cashflow_positive(self):
        # Prepare mock data
        mock_quarterly_cashflow = pd.DataFrame({'Quarter': [1, 2], 'Cash from Operations': [150, 200]})
        self.mock_ticker_data.quarterly_cashflow = mock_quarterly_cashflow
        
        # Execute
        result = self.accounting_data.get_quarterly_cashflow
        
        # Verify
        pd.testing.assert_frame_equal(result, mock_quarterly_cashflow)

    def test_get_quarterly_cashflow_negative(self):
        # Prepare mock data
        self.mock_ticker_data.quarterly_cashflow = None
        
        # Execute
        result = self.accounting_data.get_quarterly_cashflow
        
        # Verify
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
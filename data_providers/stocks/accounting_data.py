
import pandas as pd
from ticker_data import TickerData

class AccountingData():
    def __init__(self, yfTickerData:TickerData=None):
        self.yfTickerData = yfTickerData

    @property
    def get_balance_sheet(self)->pd.DataFrame:
        return self.yfTickerData.balance_sheet
    
    @property
    def get_quarterly_balance_sheets(self)->pd.DataFrame:
        return self.yfTickerData.quarterly_balance_sheet
    
    @property
    def get_cashflow(self)->pd.DataFrame:
        return self.yfTickerData.cashflow
    
    @property
    def get_quarterly_cashflow(self)->pd.DataFrame:
        return self.yfTickerData.quarterly_cashflow


import pandas as pd
from data_providers.stocks.ticker_data import TickerData


class FinancialData():
    def __init__(self, yfTickerData:TickerData=None):
        self.yfTickerData = yfTickerData

    @property
    def get_calendar(self)->pd.DataFrame:
        return self.yfTickerData.calendar
    
    @property
    def get_sec_filings(self)->pd.DataFrame:
        return self.yfTickerData.sec_filings
    
    @property
    def get_get_shares_full(self, start:str="2022-01-01", end:str=None)->pd.DataFrame:
        return self.yfTickerData.get_shares_full(start, end)


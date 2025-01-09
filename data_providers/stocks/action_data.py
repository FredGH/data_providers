
import pandas as pd
from data_providers.stocks.ticker_data import TickerData


class ActionData():
    def __init__(self, yfTickerData:TickerData=None):
        self.yfTickerData = yfTickerData

    @property
    def get_actions(self)->pd.DataFrame:
        return self.yfTickerData.actions
    
    @property
    def get_dividends(self)->pd.DataFrame:
        return self.yfTickerData.dividends
    
    @property
    def get_splits(self)->pd.DataFrame:
        return self.yfTickerData.splits
    
    @property
    def get_capital_gains(self)->pd.DataFrame:
        return self.yfTickerData.capital_gains
    
    @property
    def get_get_shares_full(self, start:str="2022-01-01", end:str=None)->pd.DataFrame:
        return self.yfTickerData.get_shares_full(start, end)


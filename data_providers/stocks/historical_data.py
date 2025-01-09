
import pandas as pd
from data_providers.stocks.ticker_data import TickerData


class HistoricalData():
    def __init__(self, yfTickerData:TickerData=None):
        self.yfTickerData = yfTickerData

    def get_historical_data(self, period:str="1mo")->pd.DataFrame:
        return self.yfTickerData.history(period="1mo")
    
    def get_historical_meta_data(self, period)->pd.DataFrame:
        _ = self.yfTickerData.get_historical_data(self, period)
        # show meta information about the history (requires history() to be called first)
        return super.yfTickerData.history_metadata
    

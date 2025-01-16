
import pandas as pd
from data_providers.stocks.ticker_data import TickerData

class InfoData():
    def __init__(self, yfTickerData:TickerData=None):
        self.yfTickerData = yfTickerData

    @property
    def get_info(self)->pd.DataFrame:
        return self.yfTickerData.info

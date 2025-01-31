import pandas as pd

from data_providers.stocks.ticker_data import TickerData


class SustainabilityData:
    def __init__(self, yfTickerData: TickerData = None):
        self.yfTickerData = yfTickerData

    @property
    def get_sustainability(self) -> pd.DataFrame:
        return self.yfTickerData.sustainability

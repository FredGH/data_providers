
import pandas as pd
from data_providers.stocks.ticker_data import TickerData


class RecommendationsData():
    def __init__(self, yfTickerData:TickerData=None):
        self.yfTickerData = yfTickerData

    @property
    def get_recommendations(self)->pd.DataFrame:
        return self.yfTickerData.recommendations
    
    @property
    def get_recommendations_summary(self)->pd.DataFrame:
        return self.yfTickerData.recommendations_summary
    
    @property
    def get_upgrades_downgrades(self)->pd.DataFrame:
        return self.yfTickerData.upgrades_downgrades
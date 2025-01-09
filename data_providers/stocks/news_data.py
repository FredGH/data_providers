
import pandas as pd
from data_providers.stocks.ticker_data import TickerData


class NewsData():
    def __init__(self, yfTickerData:TickerData=None):
        self.yfTickerData = yfTickerData

    @property
    def get_news(self)->list:
        return self.yfTickerData.news


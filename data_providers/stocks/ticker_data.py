
import yfinance as yf
import pandas as pd

class TickerData():
    def __init__(self, name:str=""):
        self.nme = name    
        self.yfTicker = yf.Ticker(name)

    @property
    def get_ticker(self)->yf.Ticker:
        return self.yfTicker

import data_providers.stocks.news_data as nd
td = TickerData(name="MSFT")
ticker = td.get_ticker
ad = nd.NewsData(ticker)
res = ad.get_news
print(res)
#https://www.kdnuggets.com/8-built-in-python-decorators-to-write-elegant-code
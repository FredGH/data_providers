
import pandas as pd
from typing import NamedTuple
from data_providers.stocks.ticker_data import TickerData

class OptionsData():
    def __init__(self, yfTickerData:TickerData=None):
        self.yfTickerData = yfTickerData

    @property
    def get_options_expirations(self)->tuple:
        return self.yfTickerData.options
    
    @property
    def get_option_chain_for_expiration(self, date:str="2022-01-01")->NamedTuple:
        return self.yfTickerData.option_chain(date)
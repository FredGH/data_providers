
import pandas as pd
from data_providers.stocks.ticker_data import TickerData

# This class is named InfoData and likely contains information-related data and methods.
class InfoData():
    def __init__(self, yfTickerData:TickerData=None):
        """
        The function initializes an object with an optional parameter of type TickerData.
        
        :param yfTickerData: The `__init__` method you provided is a constructor for a class, and it
        takes an optional parameter `yfTickerData` of type `TickerData`. This parameter is used to
        initialize the `yfTickerData` attribute of the class instance
        :type yfTickerData: TickerData
        """
        self.yfTickerData = yfTickerData

    @property
    def get_info(self)->pd.DataFrame:
        """
        The function `get_info` returns the information of a Yahoo Finance ticker data as a Pandas
        DataFrame.
        :return: The `get_info` method is returning the information stored in the `info` attribute of
        the `yfTickerData` object as a pandas DataFrame.
        """
        return self.yfTickerData.info

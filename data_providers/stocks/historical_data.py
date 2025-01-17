import pandas as pd

from data_providers.stocks.ticker_data import TickerData


# This class likely represents a data structure or object for storing historical data.
class HistoricalData:
    def __init__(self, yfTickerData: TickerData = None):
        """
        The function initializes an object with optional Yahoo Finance ticker data.

        :param yfTickerData: The `__init__` method you provided is a constructor for a class, and it
        takes an optional parameter `yfTickerData` of type `TickerData`. This parameter is used to
        initialize the `yfTickerData` attribute of the class instance
        :type yfTickerData: TickerData
        """
        self.yfTickerData = yfTickerData

    def get_historical_data(self, period: str = "1mo") -> pd.DataFrame:
        """
        The function `get_historical_data` retrieves historical stock data for a specified period using
        the Yahoo Finance API.

        :param period: The `get_historical_data` function retrieves historical market data for a given
        period. The `period` parameter specifies the time period for which you want to retrieve
        historical data. The default value for the `period` parameter is set to "1mo", which stands for
        1 month, defaults to 1mo
        :type period: str (optional)
        :return: The function `get_historical_data` is returning a pandas DataFrame containing
        historical data for the specified period. The data is retrieved using the `history` method from
        the `yfTickerData` object with the specified period parameter.
        """
        return self.yfTickerData.history(period=period)

    def get_historical_meta_data(self, period) -> pd.DataFrame:
        """
        This function retrieves historical meta data for a given period using Yahoo Finance API.

        :param period: The `period` parameter in the `get_historical_meta_data` method likely refers to
        the time period for which historical data is being requested. This parameter could specify the
        duration or range of time for which historical data should be retrieved, such as "1d" for one
        day, "1mo
        :return: The code is attempting to return the meta information about the historical data
        retrieved for a given period using the Yahoo Finance API. However, there are some issues in the
        code that need to be corrected:
        """
        _ = self.yfTickerData.get_historical_data(self, period)
        # show meta information about the history (requires history() to be called first)
        return super.yfTickerData.history_metadata

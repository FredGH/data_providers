import pandas as pd

from data_providers.stocks.ticker_data import TickerData


# This class is named ActionData and likely contains attributes and methods related to storing and
# manipulating data for actions.
class ActionData:
    def __init__(self, yfTickerData: TickerData = None):
        """
        The function initializes an object with optional Yahoo Finance ticker data.

        :param yfTickerData: The `__init__` method you provided is a constructor for a class, and it
        takes an optional parameter `yfTickerData` of type `TickerData`. This parameter is used to
        initialize the `yfTickerData` attribute of the class instance
        :type yfTickerData: TickerData
        """
        self.yfTickerData = yfTickerData

    @property
    def get_actions(self) -> pd.Series:
        """
        The function `get_actions` returns the actions data from the Yahoo Finance ticker data as a
        Pandas Series.
        :return: The `get_actions` method is returning a Pandas Series containing the actions data from
        the `yfTickerData` attribute of the object.
        """
        return self.yfTickerData.actions

    @property
    def get_dividends(self) -> pd.Series:
        """
        This function returns the dividends data from the Yahoo Finance ticker data.
        :return: A pandas Series containing dividend data is being returned.
        """
        return self.yfTickerData.dividends

    @property
    def get_splits(self) -> pd.Series:
        """
        The function `get_splits` returns the splits data from the `yfTickerData` attribute.
        :return: A pandas Series containing information about stock splits for the given yfTickerData.
        """
        return self.yfTickerData.splits

    @property
    def get_capital_gains(self) -> pd.Series:
        """
        This function returns the capital gains data stored in the `yfTickerData` attribute of the
        object.
        :return: The `get_capital_gains` method is returning the capital gains data stored in the
        `yfTickerData` attribute of the object. It is returning a pandas Series containing the capital
        gains information.
        """
        return self.yfTickerData.capital_gains

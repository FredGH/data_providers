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

    @property
    def get_get_shares_full(
        self, start: str = "2022-01-01", end: str = None
    ) -> pd.DataFrame:
        """
        This function retrieves full share data for a specified date range using the Yahoo Finance API.

        :param start: The `start` parameter in the `get_get_shares_full` method is a string that
        represents the start date for retrieving data. In this case, the default value for `start` is
        set to "2022-01-01", defaults to 2022-01-01
        :type start: str (optional)
        :param end: The `end` parameter in the `get_get_shares_full` function is a string that
        represents the end date for retrieving data. If no `end` date is provided when calling the
        function, it defaults to `None`, which typically means that data will be retrieved up to the
        most recent available
        :type end: str
        :return: The `get_get_shares_full` method is returning a pandas DataFrame containing the shares
        data retrieved using the `get_shares_full` method from the `yfTickerData` object within the
        specified date range.
        """
        return self.yfTickerData.get_shares_full(start, end)

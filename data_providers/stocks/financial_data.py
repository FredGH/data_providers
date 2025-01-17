import pandas as pd

from data_providers.stocks.ticker_data import TickerData


# The `FinancialData` class is a Python class that serves as a wrapper for financial data
# related to a specific stock ticker. It has properties that allow access to different types of
# financial data such as calendar data, SEC filings, and shares information. The class takes an
# instance of `TickerData` as a parameter during initialization, which provides the actual data
# for the properties.
class FinancialData:
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
    def get_calendar(self) -> pd.DataFrame:
        """
        This function returns the calendar data for a given Yahoo Finance ticker.
        :return: The `get_calendar` method is returning the calendar data stored in the `yfTickerData`
        attribute of the object. This data is returned as a pandas DataFrame.
        """
        return self.yfTickerData.calendar

    @property
    def get_sec_filings(self) -> pd.DataFrame:
        """
        This function returns the SEC filings data for a given Yahoo Finance ticker.
        :return: The `get_sec_filings` method is returning the SEC filings data stored in the
        `sec_filings` attribute of the `yfTickerData` object as a pandas DataFrame.
        """
        return self.yfTickerData.sec_filings

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
        function, it defaults to `None`, indicating that data will be retrieved up to the most recent
        available date
        :type end: str
        :return: This function is returning a pandas DataFrame containing the full share data for a
        given date range. The data is retrieved using the `get_shares_full` method from the
        `yfTickerData` object, with the specified start and end dates.
        """
        return self.yfTickerData.get_shares_full(start, end)

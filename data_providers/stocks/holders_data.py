import pandas as pd

from data_providers.stocks.ticker_data import TickerData


# This class likely stores data related to holders or owners of something.
class HoldersData:
    def __init__(self, yfTickerData: TickerData = None):
        """
        The function `__init__` initializes an object with an optional parameter `yfTickerData` of type
        `TickerData`.

        :param yfTickerData: The `__init__` method you provided is a constructor for a class, and it
        takes an optional parameter `yfTickerData` of type `TickerData`. This parameter is used to
        initialize the `yfTickerData` attribute of the class instance
        :type yfTickerData: TickerData
        """
        self.yfTickerData = yfTickerData

    @property
    def get_major_holders(self) -> pd.DataFrame:
        """
        The function `get_major_holders` returns the major holders data of a Yahoo Finance ticker.
        :return: The `get_major_holders` method is returning the major holders data of the
        `yfTickerData` attribute as a pandas DataFrame.
        """
        return self.yfTickerData.major_holders

    @property
    def get_institutional_holders(self) -> pd.DataFrame:
        """
        This function returns the institutional holders data from the Yahoo Finance ticker data.
        :return: The method `get_institutional_holders` is returning the institutional holders data
        stored in the attribute `institutional_holders` of the `yfTickerData` object as a pandas
        DataFrame.
        """
        return self.yfTickerData.institutional_holders

    @property
    def get_mutualfund_holders(self) -> pd.DataFrame:
        """
        This function is intended to return the cashflow data of a mutual fund.
        :return: The `cashflow` data from the `yfTickerData` attribute of the object is being returned
        as a pandas DataFrame.
        """
        return self.yfTickerData.cashflow

    @property
    def get_quarterly_cashflow(self) -> pd.DataFrame:
        """
        The function `get_quarterly_cashflow` returns the mutual fund holders data from the Yahoo
        Finance ticker data.
        :return: The method `get_quarterly_cashflow` is returning the quarterly cash flow data for the
        given `self` object. The data is in the form of a pandas DataFrame and is fetched from the
        `mutualfund_holders` attribute of the `yfTickerData` object associated with the `self` object.
        """
        return self.yfTickerData.mutualfund_holders

    @property
    def get_insider_transactions(self) -> pd.DataFrame:
        """
        This function returns insider transactions data from the Yahoo Finance ticker data.
        :return: A pandas DataFrame containing insider transactions data from the Yahoo Finance ticker
        data.
        """
        return self.yfTickerData.insider_transactions

    @property
    def get_insider_purchases(self) -> pd.DataFrame:
        """
        This function returns insider purchases data from the Yahoo Finance ticker data.
        :return: A pandas DataFrame containing insider purchases data from the Yahoo Finance ticker
        data.
        """
        return self.yfTickerData.insider_purchases

    @property
    def get_insider_roster_holders(self) -> pd.DataFrame:
        """
        The function `get_insider_roster_holders` returns the insider roster holders data from the
        `yfTickerData` attribute.
        :return: The method `get_insider_roster_holders` is returning a pandas DataFrame containing the
        insider roster holders data from the `yfTickerData` attribute of the object.
        """
        return self.yfTickerData.insider_roster_holders

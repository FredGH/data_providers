import pandas as pd

from data_providers.stocks.ticker_data import TickerData


# This class `AccountingData` provides properties to access balance sheet, quarterly balance sheets,
# cashflow, and quarterly cashflow data using a `TickerData` object.
class AccountingData:
    def __init__(self, yfTickerData: TickerData = None):
        self.yfTickerData = yfTickerData

    @property
    def get_balance_sheet(self) -> pd.DataFrame:
        """
        This function returns the balance sheet data for a given stock using the Yahoo Finance API.
        :return: The `balance_sheet` data from the `yfTickerData` attribute of the object is being
        returned as a pandas DataFrame.
        """
        return self.yfTickerData.balance_sheet

    @property
    def get_quarterly_balance_sheets(self) -> pd.DataFrame:
        """
        This function returns the quarterly balance sheets data for a given stock ticker.
        :return: The method `get_quarterly_balance_sheets` is returning a pandas DataFrame that contains
        the quarterly balance sheet data from the `yfTickerData` attribute of the object.
        """
        return self.yfTickerData.quarterly_balance_sheet

    @property
    def get_cashflow(self) -> pd.DataFrame:
        """
        This function returns the cashflow data from the Yahoo Finance ticker data stored in the object.
        :return: A pandas DataFrame containing the cashflow data from the `yfTickerData` attribute of
        the object.
        """
        return self.yfTickerData.cashflow

    @property
    def get_quarterly_cashflow(self) -> pd.DataFrame:
        """
        This function returns the quarterly cashflow data for a given stock using the Yahoo Finance API.
        :return: The method `get_quarterly_cashflow` is returning the quarterly cashflow data stored in
        the attribute `self.yfTickerData.quarterly_cashflow` as a pandas DataFrame.
        """
        return self.yfTickerData.quarterly_cashflow

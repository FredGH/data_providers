import pandas as pd

from data_providers.stocks.ticker_data import TickerData


class AnalystsData:
    def __init__(self, yfTickerData: TickerData = None):
        """
        The function `__init__` initializes an object with an optional parameter `yfTickerData` of type
        `TickerData`.

        :param yfTickerData: The `__init__` method you provided is a constructor for a class, and it
        takes an optional parameter `yfTickerData` of type `TickerData`. This parameter is used to
        initialize the `yfTickerData` attribute of the class instance
        :type yfTickerData: TickerData
        # This class is named AnalystsData and likely contains methods and attributes related to analyzing
        # This class is named AnalystsData and likely contains methods and attributes related to analyzing
        # data.
        # data.
        """
        self.yfTickerData = yfTickerData

    @property
    def get_analyst_price_targets(self) -> pd.DataFrame:
        """
        This function returns the analyst price targets data for a given stock ticker.
        :return: The method `get_analyst_price_targets` is returning a pandas DataFrame containing
        analyst price targets from the `yfTickerData` attribute of the object.
        """
        return self.yfTickerData.analyst_price_targets

    @property
    def get_earnings_estimate(self) -> pd.DataFrame:
        """
        This function returns the earnings estimate data from the Yahoo Finance ticker data.
        :return: A pandas DataFrame containing earnings estimates is being returned.
        """
        return self.yfTickerData.earnings_estimate

    @property
    def get_revenue_estimate(self) -> pd.DataFrame:
        """
        This function returns the revenue estimate data from the Yahoo Finance ticker data.
        :return: The `revenue_estimate` data from the `yfTickerData` attribute of the object.
        """
        return self.yfTickerData.revenue_estimate

    @property
    def get_earnings_history(self) -> pd.DataFrame:
        """
        This function returns the earnings history data stored in the `earnings_history` attribute of
        the `yfTickerData` object.
        :return: The method `get_earnings_history` is returning a pandas DataFrame containing the
        earnings history data from the `yfTickerData` attribute of the object.
        """
        return self.yfTickerData.earnings_history

    @property
    def eps_trend(self) -> pd.DataFrame:
        """
        This function returns the earnings per share (EPS) trend data from the Yahoo Finance ticker
        data.
        :return: The `eps_trend` attribute from the `yfTickerData` object is being returned as a pandas
        DataFrame.
        """
        return self.yfTickerData.eps_trend

    @property
    def eps_revisions(self) -> pd.DataFrame:
        """
        This function returns the EPS revisions data from the yfTickerData attribute.
        :return: A pandas DataFrame containing EPS revisions data from the `yfTickerData` attribute of
        the object.
        """
        return self.yfTickerData.eps_revisions

    @property
    def growth_estimates(self) -> pd.DataFrame:
        """
        This function returns the growth estimates data from the Yahoo Finance ticker data.
        :return: The method `growth_estimates` is being called on the `self.yfTickerData` object, and it
        returns a pandas DataFrame containing growth estimates.
        """
        return self.yfTickerData.growth_estimates

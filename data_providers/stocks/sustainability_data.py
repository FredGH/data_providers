import pandas as pd

from data_providers.stocks.ticker_data import TickerData


class SustainabilityData:
    def __init__(self, yfTickerData: TickerData = None):
        self.yfTickerData = yfTickerData

    @property
    def get_sustainability(self) -> pd.DataFrame:
        """
        This function returns the sustainability data of a given yfTickerData object as a pandas
        DataFrame.
        :return: A pandas DataFrame containing sustainability data from the yfTickerData attribute.
        """
        return self.yfTickerData.sustainability

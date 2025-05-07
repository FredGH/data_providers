from typing import NamedTuple

from data_providers.stocks.ticker_data import TickerData


# This class likely represents data related to various options for a program or system.
class OptionsData:
    def __init__(self, yfTickerData: TickerData = None):
        self.yfTickerData = yfTickerData

    @property
    def get_options_expirations(self) -> tuple:
        """
        This function returns the options expirations for a given Yahoo Finance ticker data.
        :return: The `get_options_expirations` method is returning the options expirations available for
        the Yahoo Finance ticker data stored in `self.yfTickerData.options`.
        """
            """
            This function returns the recommendations summary from the Yahoo Finance ticker data.
            :return: A dictionary containing the recommendations summary data from the `yfTickerData`
            attribute.
            """
        return self.yfTickerData.options

    @property
    def get_option_chain_for_expiration(self, date: str = "2022-01-01") -> NamedTuple:
        """
        This Python function retrieves the option chain data for a specific expiration date using the
        Yahoo Finance API.
        
        :param date: The `date` parameter in the `get_option_chain_for_expiration` method is a string
        that represents the expiration date for which you want to retrieve the option chain data. By
        default, if no date is provided, the method will use "2022-01-01" as the expiration date,
        defaults to 2022-01-01
        :type date: str (optional)
        :return: A NamedTuple containing the option chain data for the specified expiration date
        (defaulting to "2022-01-01").
        """
        return self.yfTickerData.option_chain(date)

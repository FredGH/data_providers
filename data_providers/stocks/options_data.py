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
        return self.yfTickerData.options

    @property
    def get_option_chain_for_expiration(self, date: str = "2022-01-01") -> NamedTuple:
        return self.yfTickerData.option_chain(date)

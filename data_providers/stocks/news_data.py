from data_providers.stocks.ticker_data import TickerData


# This class likely represents data related to news articles or news content.
class NewsData:
    def __init__(self, yfTickerData: TickerData = None):
        """
        The function initializes an object with optional Yahoo Finance ticker data.

        :param yfTickerData: The `__init__` method you provided is a constructor for a class, and it
        takes an optional parameter `yfTickerData` of type `TickerData`. The constructor initializes an
        instance variable `yfTickerData` with the value passed to it
        :type yfTickerData: TickerData
        """
        self.yfTickerData = yfTickerData

    @property
    def get_news(self) -> list:
        """
        This Python function returns a list of news related to a Yahoo Finance ticker data.
        :return: A list of news articles related to the Yahoo Finance ticker data.
        """
        return self.yfTickerData.news

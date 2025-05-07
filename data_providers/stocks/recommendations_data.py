from data_providers.stocks.ticker_data import TickerData


# This class likely contains data related to recommendations.
class RecommendationsData:
    def __init__(self, yfTickerData: TickerData = None):
        self.yfTickerData = yfTickerData

    @property
    def get_recommendations(self) -> dict:
        """
        This Python function returns recommendations from Yahoo Finance ticker data.
        :return: A dictionary containing recommendations from the Yahoo Finance ticker data.
        """
        return self.yfTickerData.recommendations

    @property
    def get_recommendations_summary(self) -> dict:
        """
        This function returns the recommendations summary data from the Yahoo Finance ticker data.
        :return: A dictionary containing the recommendations summary data from the `yfTickerData`
        attribute.
        """
        return self.yfTickerData.recommendations_summary

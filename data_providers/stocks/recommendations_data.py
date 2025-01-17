from data_providers.stocks.ticker_data import TickerData


class RecommendationsData:
    def __init__(self, yfTickerData: TickerData = None):
        self.yfTickerData = yfTickerData

    @property
    def get_recommendations(self) -> dict:
        return self.yfTickerData.recommendations

    @property
    def get_recommendations_summary(self) -> dict:
        return self.yfTickerData.recommendations_summary

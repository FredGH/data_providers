import yfinance as yf

# This class likely represents data related to stock tickers.
class TickerData:
    def __init__(self, name: str = ""):
        self.nme = name
        self.yfTicker = yf.Ticker(name)

    @property
    def get_ticker(self) -> yf.Ticker:
        """
        This function returns the Yahoo Finance Ticker object associated with the class instance.
        :return: An instance of the `yf.Ticker` class is being returned.
        # This class likely contains data and methods related to sustainability metrics or practices.
        """
        return self.yfTicker

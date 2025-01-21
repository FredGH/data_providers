import sys
sys.path.insert(0,".")

import unittest
from unittest.mock import MagicMock, patch

from data_providers.stocks.ticker_data import TickerData

class TestTickerData(unittest.TestCase):
    def setUp(self):
        """Set up method to initialize TickerData with a valid ticker symbol."""
        self.valid_ticker = "MSFT"
        self.invalid_ticker = "INVALID"
        self.ticker_data = TickerData(name=self.valid_ticker)

    @patch("yfinance.Ticker")
    def test_init_with_valid_ticker(self, mock_ticker):
        """Test initialization with a valid ticker symbol."""
        mock_ticker.return_value = MagicMock()
        ticker_data = TickerData(name=self.valid_ticker)
        self.assertEqual(ticker_data.nme, self.valid_ticker)
        self.assertIsNotNone(ticker_data.yfTicker)

    @patch("yfinance.Ticker")
    def test_init_with_invalid_ticker(self, mock_ticker):
        """Test initialization with an invalid ticker symbol."""
        mock_ticker.return_value = MagicMock()
        ticker_data = TickerData(name=self.invalid_ticker)
        self.assertEqual(ticker_data.nme, self.invalid_ticker)
        self.assertIsNotNone(ticker_data.yfTicker)

    @patch("yfinance.Ticker")
    def test_get_ticker_property(self, mock_ticker):
        """Test the get_ticker property returns the yfTicker object."""
        mock_ticker.return_value = MagicMock()
        ticker_data = TickerData(name=self.valid_ticker)
        self.assertEqual(ticker_data.get_ticker, ticker_data.yfTicker)

    #@patch("yfinance.Ticker")
    #def test_get_ticker_with_invalid_ticker(self, mock_ticker):
    #    """Test the get_ticker property with an invalid ticker."""
    #    mock_ticker.side_effect = Exception("Ticker not found")
    #    ticker_data = TickerData(name=self.invalid_ticker)
    #    with self.assertRaises(Exception):
    #        ticker_data.get_ticker

    #@patch("yfinance.Ticker")
    #def test_ticker_data_scalability(self):
    #    """Test the scalability of the TickerData class with multiple tickers."""
    #    tickers = ["AAPL", "GOOGL", "AMZN", "MSFT"]
    #    for ticker in tickers:
    #        with self.subTest(ticker=ticker):
    #            ticker_data = TickerData(name=ticker)
    #            self.assertEqual(ticker_data.nme, ticker)


    def test_ticker_data_performance(self):
        """Test the performance of TickerData initialization."""
        import time

        start_time = time.time()
        for _ in range(1000):  # Simulating a load test
            TickerData(name="MSFT")
        duration = time.time() - start_time
        self.assertLess(duration, 1)  # Should complete in less than 1 second


if __name__ == "__main__":
    unittest.main()

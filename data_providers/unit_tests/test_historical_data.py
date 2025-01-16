
import unittest
from unittest.mock import MagicMock
import pandas as pd
from data_providers.stocks.ticker_data import TickerData
from data_providers.stocks.historical_data import HistoricalData 

class TestHistoricalData(unittest.TestCase):

    def setUp(self):
        # Create a mock TickerData object
        self.mock_ticker_data = MagicMock(spec=TickerData)
        self.historical_data = HistoricalData(yfTickerData=self.mock_ticker_data)

    def test_get_historical_data_positive(self):
        # Arrange
        expected_data = pd.DataFrame({'Close': [100, 101, 102]}, index=pd.date_range(start='2023-01-01', periods=3))
        self.mock_ticker_data.history.return_value = expected_data
        
        # Act
        result = self.historical_data.get_historical_data(period="1mo")
        
        # Assert
        pd.testing.assert_frame_equal(result, expected_data)
        self.mock_ticker_data.history.assert_called_once_with(period="1mo")

    def test_get_historical_data_negative(self):
        # Arrange
        self.mock_ticker_data.history.side_effect = Exception("Data retrieval error")
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            self.historical_data.get_historical_data(period="1mo")
        self.assertEqual(str(context.exception), "Data retrieval error")

    def test_get_historical_meta_data_positive(self):
        # Arrange
        expected_data = pd.DataFrame({'Meta': ['Info1', 'Info2']})
        self.mock_ticker_data.history.return_value = pd.DataFrame({'Close': [100, 101, 102]})
        self.mock_ticker_data.history_metadata = expected_data
        
        # Act
        result = self.historical_data.get_historical_meta_data(period="1mo")
        
        # Assert
        pd.testing.assert_frame_equal(result, expected_data)
        self.mock_ticker_data.history.assert_called_once_with(period="1mo")

    def test_get_historical_meta_data_negative(self):
        # Arrange
        self.mock_ticker_data.get_historical_data.side_effect = Exception("Meta data retrieval error")
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            self.historical_data.get_historical_meta_data(period="1mo")
        self.assertEqual(str(context.exception), "Meta data retrieval error")

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import MagicMock
from data_providers.stocks.ticker_data import TickerData
from data_providers.stocks.recommendations_data import RecommendationsData 

class TestRecommendationsData(unittest.TestCase):
    def setUp(self):
        # Create a mock TickerData object
        self.mock_ticker_data = MagicMock(spec=TickerData)
        self.recommendations_data = RecommendationsData(yfTickerData=self.mock_ticker_data)

    def test_get_recommendations_positive(self):
        # Arrange
        expected_recommendations = {'AAPL': 'Buy', 'GOOGL': 'Hold'}
        self.mock_ticker_data.recommendations = expected_recommendations
        
        # Act
        result = self.recommendations_data.get_recommendations
        
        # Assert
        self.assertEqual(result, expected_recommendations)

    def test_get_recommendations_negative(self):
        # Arrange
        self.mock_ticker_data.recommendations = None
        
        # Act
        result = self.recommendations_data.get_recommendations
        
        # Assert
        self.assertIsNone(result)

    def test_get_recommendations_summary_positive(self):
        # Arrange
        expected_summary = {'AAPL': {'rating': 'Buy', 'target_price': 150}}
        self.mock_ticker_data.recommendations_summary = expected_summary
        
        # Act
        result = self.recommendations_data.get_recommendations_summary
        
        # Assert
        self.assertEqual(result, expected_summary)

    def test_get_recommendations_summary_negative(self):
        # Arrange
        self.mock_ticker_data.recommendations_summary = None
        
        # Act
        result = self.recommendations_data.get_recommendations_summary
        
        # Assert
        self.assertIsNone(result)

    def test_get_recommendations_empty(self):
        # Arrange
        self.mock_ticker_data.recommendations = {}
        
        # Act
        result = self.recommendations_data.get_recommendations
        
        # Assert
        self.assertEqual(result, {})

    def test_get_recommendations_summary_empty(self):
        # Arrange
        self.mock_ticker_data.recommendations_summary = {}
        
        # Act
        result = self.recommendations_data.get_recommendations_summary
        
        # Assert
        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()
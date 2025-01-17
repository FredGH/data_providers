import unittest
from unittest.mock import MagicMock

import pandas as pd

from data_providers.stocks.info_data import InfoData
from data_providers.stocks.ticker_data import TickerData


class TestInfoData(unittest.TestCase):

    def setUp(self):
        # Setup a mock TickerData object
        self.mock_ticker_data = MagicMock(spec=TickerData)
        self.info_data = InfoData(yfTickerData=self.mock_ticker_data)

    def test_get_info_positive(self):
        # Positive test case: When info is available
        expected_info = pd.DataFrame({"key": ["value1", "value2"]})
        self.mock_ticker_data.info = expected_info

        result = self.info_data.get_info

        # Check if the result matches the expected DataFrame
        pd.testing.assert_frame_equal(result, expected_info)

    def test_get_info_negative(self):
        # Negative test case: When info is not available
        self.mock_ticker_data.info = None

        with self.assertRaises(TypeError):
            self.info_data.get_info

    def test_info_data_initialization(self):
        # Test initialization with None
        info_data_none = InfoData()
        self.assertIsNone(info_data_none.yfTickerData)

    def test_info_data_initialization_with_ticker_data(self):
        # Test initialization with a valid TickerData
        info_data_valid = InfoData(yfTickerData=self.mock_ticker_data)
        self.assertEqual(info_data_valid.yfTickerData, self.mock_ticker_data)

    def test_get_info_edge_case(self):
        # Edge case: Empty DataFrame
        empty_info = pd.DataFrame()
        self.mock_ticker_data.info = empty_info

        result = self.info_data.get_info

        # Check if the result is an empty DataFrame
        pd.testing.assert_frame_equal(result, empty_info)

    def test_get_info_performance(self):
        # Performance test: Simulating a large DataFrame
        large_info = pd.DataFrame({"key": ["value"] * 1000000})
        self.mock_ticker_data.info = large_info

        import time

        start_time = time.time()
        result = self.info_data.get_info
        end_time = time.time()

        # Ensure that the performance is acceptable
        self.assertLess(end_time - start_time, 1)  # Adjust the threshold as necessary
        pd.testing.assert_frame_equal(result, large_info)


if __name__ == "__main__":
    unittest.main()

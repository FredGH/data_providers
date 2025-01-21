import unittest
from unittest.mock import MagicMock

from data_providers.stocks.options_data import OptionsData
from data_providers.stocks.ticker_data import TickerData


class TestOptionsData(unittest.TestCase):

    def setUp(self):
        # Create a mock TickerData object
        self.mock_ticker_data = MagicMock(spec=TickerData)
        self.options_data = OptionsData(yfTickerData=self.mock_ticker_data)

    def test_get_options_expirations_positive(self):
        # Set up the mock to return a list of expirations
        self.mock_ticker_data.options = ["2022-01-21", "2022-01-28"]

        # Call the method and check the result
        expirations = self.options_data.get_options_expirations
        self.assertEqual(expirations, ["2022-01-21", "2022-01-28"])

    def test_get_options_expirations_negative(self):
        # Set up the mock to return an empty list
        self.mock_ticker_data.options = []

        # Call the method and check the result
        expirations = self.options_data.get_options_expirations
        self.assertEqual(expirations, [])

    #def test_get_option_chain_for_expiration_positive(self):
    #    # Set up the mock to return a named tuple for a specific date
    #    mock_chain = MagicMock()
    #    self.mock_ticker_data.option_chain.return_value = mock_chain
    #
    #    # Call the method and check the result
    #    result = self.options_data.get_option_chain_for_expiration(date="2022-01-21")
    #    self.assertEqual(result, mock_chain)
    #    self.mock_ticker_data.option_chain.assert_called_once_with("2022-01-21")

    #def test_get_option_chain_for_expiration_negative(self):
    #    # Set up the mock to raise an exception for an invalid date
    #    self.mock_ticker_data.option_chain.side_effect = ValueError("Invalid date")

    #    with self.assertRaises(ValueError):
    #        self.options_data.get_option_chain_for_expiration(date="invalid-date")

    #def test_get_option_chain_for_expiration_default(self):
    #    # Test the default date
    #    mock_chain = MagicMock()
    #    self.mock_ticker_data.option_chain.return_value = mock_chain
    #
    #    result = self.options_data.get_option_chain_for_expiration()
    #    self.assertEqual(result, mock_chain)
    #    self.mock_ticker_data.option_chain.assert_called_once_with("2022-01-01")


if __name__ == "__main__":
    unittest.main()

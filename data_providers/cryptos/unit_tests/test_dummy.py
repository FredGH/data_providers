import sys

sys.path.insert(0, ".")

import unittest

from data_providers.stocks.unit_tests import manual_run as d


class TestDummy(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_get_data_successful(self):
        dummy = d.Dummy()
        actual = dummy.get_data
        expected = [1, 2, 3]
        self.assertEqual(
            expected, actual, "The expected output is in NOT line with the actual"
        )

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()

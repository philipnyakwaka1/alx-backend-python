#!/usr/bin/env python3
"""Module for test cases"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test class"""

    @parameterized.expand([({'a': 1}, ('a', ), 1)])
    def test_access_nested_map(self, nested_map, iterable, expected):
        """Test for access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, iterable), expected)


if __name__ == '__main__':
    unittest.main()

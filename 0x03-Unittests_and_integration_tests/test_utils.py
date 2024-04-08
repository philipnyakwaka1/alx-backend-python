#!/usr/bin/env python3
"""Module for test cases"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """Test class"""

    @parameterized.expand([({"a": 1}, ("a", ), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, iterable, expected):
        """Test for correct output"""
        self.assertEqual(access_nested_map(nested_map, iterable), expected)

    @parameterized.expand([({}, ("a"), KeyError),
                           ({"a": 1}, ("a", "b"), KeyError)])
    def test_access_nested_map_exception(self, nested_map, iterable, expected):
        """Test for KeyError"""
        with self.assertRaises(expected) as e:
            access_nested_map(nested_map, iterable)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
"""Module for test cases"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from unittest.mock import Mock, patch
import requests


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


class TestGetJson(unittest.TestCase):
    """Test class for get_json(url) method"""

    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test for correct json output"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test class"""

    def test_memoize(self):
        """Test for memoize"""

        class TestClass:
            """Test class"""

            def a_method(self, input, expected, mock_get):
                """Tests for correct output"""
                return 42

            @memoize
            def a_property(self):
                """Tests"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_obj:
            obj = TestClass()
            result1 = obj.a_property()
            result2 = obj.a_property()
            mock_obj.assert_called_once()


if __name__ == '__main__':
    unittest.main()

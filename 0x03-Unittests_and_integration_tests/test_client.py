#!/usr/bin/env python3
"""Test module for GithubOrgClient"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class"""

    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get):
        """Test for GithubOrgClient.org"""

        mock_response = {"org_info": "dummy_data"}
        mock_get.return_value = mock_response
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get.assert_called_once_with("https://api.github.com/orgs/"
                                         + org_name)
        self.assertEqual(result, {"org_info": "dummy_data"})


if __name__ == '__main__':
    unittest.main()

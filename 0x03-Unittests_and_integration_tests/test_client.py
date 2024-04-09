#!/usr/bin/env python3
"""Test module for GithubOrgClient"""

import unittest
from unittest.mock import patch, Mock, PropertyMock
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

    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property."""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_obj:
            mock_obj.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo, key, expected):
        """Tests"""
        client = GithubOrgClient("google")
        check_lincense = client.has_license(repo, key)
        self.assertEqual(check_lincense, expected)


if __name__ == '__main__':
    unittest.main()

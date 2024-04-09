#!/usr/bin/env python3
"""Test module for GithubOrgClient"""

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from utils import get_json
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from requests import HTTPError


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


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests class."""
    @classmethod
    def setUpClass(cls):
        """Set up fixture"""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def custom_payload_func(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            else:
                raise HTTPError('Url not present')

        cls.get_patcher = patch("requests.get",
                                side_effect=custom_payload_func)
        cls.get_patcher.start()

    def test_for_repos_with_lincense(self):
        """Tests"""
        result = GithubOrgClient("google").public_repos(license="apache-2.0")
        self.assertEqual(result, self.apache2_repos)

    def test_all_public_repos(self):
        """Tests"""
        result = GithubOrgClient("google").public_repos()
        self.assertEqual(result, self.expected_repos)

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down fixture"""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()

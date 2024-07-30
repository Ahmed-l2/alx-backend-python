#!/usr/bin/env python3
"""Module for Unitttesting client.py"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Class for testing the GithubOrgClient Class"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"key": "value"})
    def test_org(self, org, mock_get_json):
        """Test for GithubOrgClient.org method"""
        client = GithubOrgClient(org)
        result = client.org

        self.assertEqual(result, {"key": "value"})
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """Test for GithubOrgClient._public_repos_url method"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "mocked_url"}
            client = GithubOrgClient("org")
            result = client._public_repos_url
            self.assertEqual(result, "mocked_url")

    @patch('client.get_json', return_value=[{"name": "value1"},
                                            {"name": "value2"}])
    def test_public_repos(self, mocked_get_json):
        """Test for GithubOrgClient._public_repos method"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "mock_url"
            client = GithubOrgClient('org')
            result = client.public_repos()

            self.assertAlmostEqual(result, ['value1', 'value2'])
            mocked_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()


if __name__ == '__main__':
    unittest.main()

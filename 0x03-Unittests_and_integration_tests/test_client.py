#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock, PropertyMock
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
        """test for GithubOrgClient._public_repos_url method"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "mocked_url"}
            client = GithubOrgClient("org")
            result = client._public_repos_url
            self.assertEqual(result, "mocked_url")


if __name__ == '__main__':
    unittest.main()

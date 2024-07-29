#!/usr/bin/env python3
import unittest
from unittest.mock import patch
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


if __name__ == '__main__':
    unittest.main()

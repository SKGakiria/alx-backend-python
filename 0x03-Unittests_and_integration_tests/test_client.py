#!/usr/bin/env python3
"""Module contains tests for the GithubOrgClient.org"""
import unittest
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class that inherits from unittest.TestCase"""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Method tests that GithubOrgClient.org returns the correct value"""
        client_class = GithubOrgClient(input)
        client_class.org()
        mock.called_with_once(client_class.ORG_URL.format(org=input))

    def test_public_repos_url(self):
        """Method tests that the result of _public_repos_url
        return the correct value based on the given payload"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "Hello World"}
            mock.return_value = payload
            client_class = GithubOrgClient('client')
            result = client_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Method tests that the list of repos is what you expect from
        the chosen payload.
        Method also tests that the mocked property and the mocked
        get_json was called once.
        """
        payload = [{"name": "Google"}, {"name": "Facebook"}]
        mock_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello world"
            client_class = GithubOrgClient('client')
            result = client_class.public_repos()

            expected = [item["name"] for item in payload]
            self.assertEqual(result, expected)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Method tests GithubOrgClient.has_license """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient class that inherits from
    unittest.TestCase"""
    @classmethod
    def setUpClass(cls):
        """Method called before tests in the class are executed"""
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """Integration test method for the public repos"""
        client_class = GithubOrgClient("google")

        self.assertEqual(client_class.org, self.org_payload)
        self.assertEqual(client_class.repos_payload, self.repos_payload)
        self.assertEqual(client_class.public_repos(), self.expected_repos)
        self.assertEqual(client_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """Integration test method for public repos with License"""
        client_class = GithubOrgClient("google")

        self.assertEqual(client_class.public_repos(), self.expected_repos)
        self.assertEqual(client_class.public_repos("XLICENSE"), [])
        self.assertEqual(client_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Method called after tests in the class are executed"""
        cls.get_patcher.stop()

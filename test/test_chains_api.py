# coding: utf-8

"""
    Harmony Connect

    An easy to use API that helps you access the Factom blockchain.  # noqa: E501

    OpenAPI spec version: 1.0.17
    Contact: harmony-support@factom.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import harmony_connect_client
from harmony_connect_client.api.chains_api import ChainsApi  # noqa: E501
from harmony_connect_client.rest import ApiException


class TestChainsApi(unittest.TestCase):
    """ChainsApi unit test stubs"""

    def setUp(self):
        self.api = harmony_connect_client.api.chains_api.ChainsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_chain_by_id(self):
        """Test case for get_chain_by_id

        Get Chain Info  # noqa: E501
        """
        pass

    def test_get_chains(self):
        """Test case for get_chains

        Get All Chains  # noqa: E501
        """
        pass

    def test_post_chain(self):
        """Test case for post_chain

        Create a Chain  # noqa: E501
        """
        pass

    def test_post_chain_search(self):
        """Test case for post_chain_search

        Search Chains  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

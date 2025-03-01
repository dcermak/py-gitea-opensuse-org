# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.23.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_gitea_opensuse_org.models.merge_upstream_request import MergeUpstreamRequest

class TestMergeUpstreamRequest(unittest.TestCase):
    """MergeUpstreamRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MergeUpstreamRequest:
        """Test MergeUpstreamRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MergeUpstreamRequest`
        """
        model = MergeUpstreamRequest()
        if include_optional:
            return MergeUpstreamRequest(
                branch = ''
            )
        else:
            return MergeUpstreamRequest(
        )
        """

    def testMergeUpstreamRequest(self):
        """Test MergeUpstreamRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

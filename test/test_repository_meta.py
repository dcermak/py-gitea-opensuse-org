# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import py_gitea_opensuse_org
from py_gitea_opensuse_org.models.repository_meta import RepositoryMeta  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException

class TestRepositoryMeta(unittest.TestCase):
    """RepositoryMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RepositoryMeta
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositoryMeta`
        """
        model = py_gitea_opensuse_org.models.repository_meta.RepositoryMeta()  # noqa: E501
        if include_optional :
            return RepositoryMeta(
                full_name = '', 
                id = 56, 
                name = '', 
                owner = ''
            )
        else :
            return RepositoryMeta(
        )
        """

    def testRepositoryMeta(self):
        """Test RepositoryMeta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

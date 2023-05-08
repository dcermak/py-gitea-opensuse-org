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
from py_gitea_opensuse_org.models.create_org_option import CreateOrgOption  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException

class TestCreateOrgOption(unittest.TestCase):
    """CreateOrgOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateOrgOption
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateOrgOption`
        """
        model = py_gitea_opensuse_org.models.create_org_option.CreateOrgOption()  # noqa: E501
        if include_optional :
            return CreateOrgOption(
                description = '', 
                full_name = '', 
                location = '', 
                repo_admin_change_team_access = True, 
                username = '', 
                visibility = 'public', 
                website = ''
            )
        else :
            return CreateOrgOption(
                username = '',
        )
        """

    def testCreateOrgOption(self):
        """Test CreateOrgOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

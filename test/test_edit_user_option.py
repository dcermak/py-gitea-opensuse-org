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
from py_gitea_opensuse_org.models.edit_user_option import EditUserOption  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException

class TestEditUserOption(unittest.TestCase):
    """EditUserOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EditUserOption
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditUserOption`
        """
        model = py_gitea_opensuse_org.models.edit_user_option.EditUserOption()  # noqa: E501
        if include_optional :
            return EditUserOption(
                active = True, 
                admin = True, 
                allow_create_organization = True, 
                allow_git_hook = True, 
                allow_import_local = True, 
                description = '', 
                email = '', 
                full_name = '', 
                location = '', 
                login_name = '', 
                max_repo_creation = 56, 
                must_change_password = True, 
                password = '', 
                prohibit_login = True, 
                restricted = True, 
                source_id = 56, 
                visibility = '', 
                website = ''
            )
        else :
            return EditUserOption(
                login_name = '',
                source_id = 56,
        )
        """

    def testEditUserOption(self):
        """Test EditUserOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

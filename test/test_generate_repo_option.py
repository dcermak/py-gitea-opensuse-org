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
from py_gitea_opensuse_org.models.generate_repo_option import GenerateRepoOption  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException

class TestGenerateRepoOption(unittest.TestCase):
    """GenerateRepoOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GenerateRepoOption
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenerateRepoOption`
        """
        model = py_gitea_opensuse_org.models.generate_repo_option.GenerateRepoOption()  # noqa: E501
        if include_optional :
            return GenerateRepoOption(
                avatar = True, 
                default_branch = '', 
                description = '', 
                git_content = True, 
                git_hooks = True, 
                labels = True, 
                name = '', 
                owner = '', 
                private = True, 
                topics = True, 
                webhooks = True
            )
        else :
            return GenerateRepoOption(
                name = '',
                owner = '',
        )
        """

    def testGenerateRepoOption(self):
        """Test GenerateRepoOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

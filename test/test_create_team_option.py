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
from py_gitea_opensuse_org.models.create_team_option import (
    CreateTeamOption,
)  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException


class TestCreateTeamOption(unittest.TestCase):
    """CreateTeamOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateTeamOption
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CreateTeamOption`
        """
        model = py_gitea_opensuse_org.models.create_team_option.CreateTeamOption()  # noqa: E501
        if include_optional :
            return CreateTeamOption(
                can_create_org_repo = True, 
                description = '', 
                includes_all_repositories = True, 
                name = '', 
                permission = 'read', 
                units = [repo.code, repo.issues, repo.ext_issues, repo.wiki, repo.pulls, repo.releases, repo.projects, repo.ext_wiki], 
                units_map = {"repo.code":"read","repo.ext_issues":"none","repo.ext_wiki":"none","repo.issues":"write","repo.projects":"none","repo.pulls":"owner","repo.releases":"none","repo.wiki":"admin"}
            )
        else :
            return CreateTeamOption(
                name = '',
        )
        """

    def testCreateTeamOption(self):
        """Test CreateTeamOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

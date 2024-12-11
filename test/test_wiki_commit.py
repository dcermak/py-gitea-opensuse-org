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
from py_gitea_opensuse_org.models.wiki_commit import WikiCommit  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException


class TestWikiCommit(unittest.TestCase):
    """WikiCommit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WikiCommit
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `WikiCommit`
        """
        model = py_gitea_opensuse_org.models.wiki_commit.WikiCommit()  # noqa: E501
        if include_optional :
            return WikiCommit(
                author = py_gitea_opensuse_org.models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit/.CommitUser contains information of a user in the context of a commit.(
                    date = '', 
                    email = '', 
                    name = '', ), 
                commiter = py_gitea_opensuse_org.models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit/.CommitUser contains information of a user in the context of a commit.(
                    date = '', 
                    email = '', 
                    name = '', ), 
                message = '', 
                sha = ''
            )
        else :
            return WikiCommit(
        )
        """

    def testWikiCommit(self):
        """Test WikiCommit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

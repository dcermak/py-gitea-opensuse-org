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
from py_gitea_opensuse_org.models.contents_response import (
    ContentsResponse,
)  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException


class TestContentsResponse(unittest.TestCase):
    """ContentsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContentsResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ContentsResponse`
        """
        model = py_gitea_opensuse_org.models.contents_response.ContentsResponse()  # noqa: E501
        if include_optional :
            return ContentsResponse(
                links = py_gitea_opensuse_org.models.file_links_response.FileLinksResponse(
                    git = '', 
                    html = '', 
                    self = '', ), 
                content = '', 
                download_url = '', 
                encoding = '', 
                git_url = '', 
                html_url = '', 
                last_commit_sha = '', 
                name = '', 
                path = '', 
                sha = '', 
                size = 56, 
                submodule_git_url = '', 
                target = '', 
                type = '', 
                url = ''
            )
        else :
            return ContentsResponse(
        )
        """

    def testContentsResponse(self):
        """Test ContentsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

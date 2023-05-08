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
from py_gitea_opensuse_org.models.commit_date_options import CommitDateOptions  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException

class TestCommitDateOptions(unittest.TestCase):
    """CommitDateOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CommitDateOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommitDateOptions`
        """
        model = py_gitea_opensuse_org.models.commit_date_options.CommitDateOptions()  # noqa: E501
        if include_optional :
            return CommitDateOptions(
                author = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                committer = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return CommitDateOptions(
        )
        """

    def testCommitDateOptions(self):
        """Test CommitDateOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

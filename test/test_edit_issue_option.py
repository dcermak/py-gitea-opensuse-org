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
from py_gitea_opensuse_org.models.edit_issue_option import EditIssueOption  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException


class TestEditIssueOption(unittest.TestCase):
    """EditIssueOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EditIssueOption
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EditIssueOption`
        """
        model = py_gitea_opensuse_org.models.edit_issue_option.EditIssueOption()  # noqa: E501
        if include_optional :
            return EditIssueOption(
                assignee = '', 
                assignees = [
                    ''
                    ], 
                body = '', 
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                milestone = 56, 
                ref = '', 
                state = '', 
                title = '', 
                unset_due_date = True
            )
        else :
            return EditIssueOption(
        )
        """

    def testEditIssueOption(self):
        """Test EditIssueOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

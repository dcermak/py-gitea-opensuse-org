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
from py_gitea_opensuse_org.models.email import Email  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException


class TestEmail(unittest.TestCase):
    """Email unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Email
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Email`
        """
        model = py_gitea_opensuse_org.models.email.Email()  # noqa: E501
        if include_optional :
            return Email(
                email = '', 
                primary = True, 
                verified = True
            )
        else :
            return Email(
        )
        """

    def testEmail(self):
        """Test Email"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

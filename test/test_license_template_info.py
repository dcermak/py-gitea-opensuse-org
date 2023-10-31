# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.21.0-rc1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from py_gitea_opensuse_org.models.license_template_info import LicenseTemplateInfo

class TestLicenseTemplateInfo(unittest.TestCase):
    """LicenseTemplateInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LicenseTemplateInfo:
        """Test LicenseTemplateInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LicenseTemplateInfo`
        """
        model = LicenseTemplateInfo()
        if include_optional:
            return LicenseTemplateInfo(
                body = '',
                implementation = '',
                key = '',
                name = '',
                url = ''
            )
        else:
            return LicenseTemplateInfo(
        )
        """

    def testLicenseTemplateInfo(self):
        """Test LicenseTemplateInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

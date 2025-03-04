# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import py_gitea_opensuse_org
from py_gitea_opensuse_org.api.settings_api import SettingsApi  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self):
        self.api = py_gitea_opensuse_org.api.settings_api.SettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_general_api_settings(self):
        """Test case for get_general_api_settings

        Get instance's global settings for api  # noqa: E501
        """
        pass

    def test_get_general_attachment_settings(self):
        """Test case for get_general_attachment_settings

        Get instance's global settings for Attachment  # noqa: E501
        """
        pass

    def test_get_general_repository_settings(self):
        """Test case for get_general_repository_settings

        Get instance's global settings for repositories  # noqa: E501
        """
        pass

    def test_get_general_ui_settings(self):
        """Test case for get_general_ui_settings

        Get instance's global settings for ui  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()

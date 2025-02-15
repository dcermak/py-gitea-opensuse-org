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
from py_gitea_opensuse_org.api.package_api import PackageApi  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException


class TestPackageApi(unittest.TestCase):
    """PackageApi unit test stubs"""

    def setUp(self):
        self.api = py_gitea_opensuse_org.api.package_api.PackageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_package(self):
        """Test case for delete_package

        Delete a package  # noqa: E501
        """
        pass

    def test_get_package(self):
        """Test case for get_package

        Gets a package  # noqa: E501
        """
        pass

    def test_list_package_files(self):
        """Test case for list_package_files

        Gets all files of a package  # noqa: E501
        """
        pass

    def test_list_packages(self):
        """Test case for list_packages

        Gets all packages of an owner  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()

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

from py_gitea_opensuse_org.models.update_user_avatar_option import (
    UpdateUserAvatarOption,
)


class TestUpdateUserAvatarOption(unittest.TestCase):
    """UpdateUserAvatarOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateUserAvatarOption:
        """Test UpdateUserAvatarOption
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `UpdateUserAvatarOption`
        """
        model = UpdateUserAvatarOption()
        if include_optional:
            return UpdateUserAvatarOption(
                image = ''
            )
        else:
            return UpdateUserAvatarOption(
        )
        """

    def testUpdateUserAvatarOption(self):
        """Test UpdateUserAvatarOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

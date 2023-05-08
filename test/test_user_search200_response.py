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
from py_gitea_opensuse_org.models.user_search200_response import UserSearch200Response  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException

class TestUserSearch200Response(unittest.TestCase):
    """UserSearch200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserSearch200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSearch200Response`
        """
        model = py_gitea_opensuse_org.models.user_search200_response.UserSearch200Response()  # noqa: E501
        if include_optional :
            return UserSearch200Response(
                data = [
                    py_gitea_opensuse_org.models.user.User(
                        active = True, 
                        avatar_url = '', 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = '', 
                        email = '', 
                        followers_count = 56, 
                        following_count = 56, 
                        full_name = '', 
                        id = 56, 
                        is_admin = True, 
                        language = '', 
                        last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        location = '', 
                        login = '', 
                        login_name = 'empty', 
                        prohibit_login = True, 
                        restricted = True, 
                        starred_repos_count = 56, 
                        visibility = '', 
                        website = '', )
                    ], 
                ok = True
            )
        else :
            return UserSearch200Response(
        )
        """

    def testUserSearch200Response(self):
        """Test UserSearch200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

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
from py_gitea_opensuse_org.models.o_auth2_application import OAuth2Application  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException

class TestOAuth2Application(unittest.TestCase):
    """OAuth2Application unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OAuth2Application
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OAuth2Application`
        """
        model = py_gitea_opensuse_org.models.o_auth2_application.OAuth2Application()  # noqa: E501
        if include_optional :
            return OAuth2Application(
                client_id = '', 
                client_secret = '', 
                confidential_client = True, 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                id = 56, 
                name = '', 
                redirect_uris = [
                    ''
                    ]
            )
        else :
            return OAuth2Application(
        )
        """

    def testOAuth2Application(self):
        """Test OAuth2Application"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

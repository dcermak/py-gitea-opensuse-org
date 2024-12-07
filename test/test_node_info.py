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
from py_gitea_opensuse_org.models.node_info import NodeInfo  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException


class TestNodeInfo(unittest.TestCase):
    """NodeInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NodeInfo
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `NodeInfo`
        """
        model = py_gitea_opensuse_org.models.node_info.NodeInfo()  # noqa: E501
        if include_optional :
            return NodeInfo(
                metadata = None, 
                open_registrations = True, 
                protocols = [
                    ''
                    ], 
                services = py_gitea_opensuse_org.models.node_info_services.NodeInfoServices(
                    inbound = [
                        ''
                        ], 
                    outbound = [
                        ''
                        ], ), 
                software = py_gitea_opensuse_org.models.node_info_software.NodeInfoSoftware(
                    homepage = '', 
                    name = '', 
                    repository = '', 
                    version = '', ), 
                usage = py_gitea_opensuse_org.models.node_info_usage.NodeInfoUsage(
                    local_comments = 56, 
                    local_posts = 56, 
                    users = py_gitea_opensuse_org.models.node_info_usage_users.NodeInfoUsageUsers(
                        active_halfyear = 56, 
                        active_month = 56, 
                        total = 56, ), ), 
                version = ''
            )
        else :
            return NodeInfo(
        )
        """

    def testNodeInfo(self):
        """Test NodeInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

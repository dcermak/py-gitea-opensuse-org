# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_gitea_opensuse_org.models.badge import Badge

class TestBadge(unittest.TestCase):
    """Badge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Badge:
        """Test Badge
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Badge`
        """
        model = Badge()
        if include_optional:
            return Badge(
                description = '',
                id = 56,
                image_url = '',
                slug = ''
            )
        else:
            return Badge(
        )
        """

    def testBadge(self):
        """Test Badge"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

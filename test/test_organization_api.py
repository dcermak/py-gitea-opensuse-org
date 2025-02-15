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
from py_gitea_opensuse_org.api.organization_api import OrganizationApi  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException


class TestOrganizationApi(unittest.TestCase):
    """OrganizationApi unit test stubs"""

    def setUp(self):
        self.api = (
            py_gitea_opensuse_org.api.organization_api.OrganizationApi()
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_create_org_repo(self):
        """Test case for create_org_repo

        Create a repository in an organization  # noqa: E501
        """
        pass

    def test_create_org_repo_deprecated(self):
        """Test case for create_org_repo_deprecated

        Create a repository in an organization  # noqa: E501
        """
        pass

    def test_org_add_team_member(self):
        """Test case for org_add_team_member

        Add a team member  # noqa: E501
        """
        pass

    def test_org_add_team_repository(self):
        """Test case for org_add_team_repository

        Add a repository to a team  # noqa: E501
        """
        pass

    def test_org_conceal_member(self):
        """Test case for org_conceal_member

        Conceal a user's membership  # noqa: E501
        """
        pass

    def test_org_create(self):
        """Test case for org_create

        Create an organization  # noqa: E501
        """
        pass

    def test_org_create_hook(self):
        """Test case for org_create_hook

        Create a hook  # noqa: E501
        """
        pass

    def test_org_create_label(self):
        """Test case for org_create_label

        Create a label for an organization  # noqa: E501
        """
        pass

    def test_org_create_team(self):
        """Test case for org_create_team

        Create a team  # noqa: E501
        """
        pass

    def test_org_delete(self):
        """Test case for org_delete

        Delete an organization  # noqa: E501
        """
        pass

    def test_org_delete_hook(self):
        """Test case for org_delete_hook

        Delete a hook  # noqa: E501
        """
        pass

    def test_org_delete_label(self):
        """Test case for org_delete_label

        Delete a label  # noqa: E501
        """
        pass

    def test_org_delete_member(self):
        """Test case for org_delete_member

        Remove a member from an organization  # noqa: E501
        """
        pass

    def test_org_delete_team(self):
        """Test case for org_delete_team

        Delete a team  # noqa: E501
        """
        pass

    def test_org_edit(self):
        """Test case for org_edit

        Edit an organization  # noqa: E501
        """
        pass

    def test_org_edit_hook(self):
        """Test case for org_edit_hook

        Update a hook  # noqa: E501
        """
        pass

    def test_org_edit_label(self):
        """Test case for org_edit_label

        Update a label  # noqa: E501
        """
        pass

    def test_org_edit_team(self):
        """Test case for org_edit_team

        Edit a team  # noqa: E501
        """
        pass

    def test_org_get(self):
        """Test case for org_get

        Get an organization  # noqa: E501
        """
        pass

    def test_org_get_all(self):
        """Test case for org_get_all

        Get list of organizations  # noqa: E501
        """
        pass

    def test_org_get_hook(self):
        """Test case for org_get_hook

        Get a hook  # noqa: E501
        """
        pass

    def test_org_get_label(self):
        """Test case for org_get_label

        Get a single label  # noqa: E501
        """
        pass

    def test_org_get_team(self):
        """Test case for org_get_team

        Get a team  # noqa: E501
        """
        pass

    def test_org_get_user_permissions(self):
        """Test case for org_get_user_permissions

        Get user permissions in organization  # noqa: E501
        """
        pass

    def test_org_is_member(self):
        """Test case for org_is_member

        Check if a user is a member of an organization  # noqa: E501
        """
        pass

    def test_org_is_public_member(self):
        """Test case for org_is_public_member

        Check if a user is a public member of an organization  # noqa: E501
        """
        pass

    def test_org_list_current_user_orgs(self):
        """Test case for org_list_current_user_orgs

        List the current user's organizations  # noqa: E501
        """
        pass

    def test_org_list_hooks(self):
        """Test case for org_list_hooks

        List an organization's webhooks  # noqa: E501
        """
        pass

    def test_org_list_labels(self):
        """Test case for org_list_labels

        List an organization's labels  # noqa: E501
        """
        pass

    def test_org_list_members(self):
        """Test case for org_list_members

        List an organization's members  # noqa: E501
        """
        pass

    def test_org_list_public_members(self):
        """Test case for org_list_public_members

        List an organization's public members  # noqa: E501
        """
        pass

    def test_org_list_repos(self):
        """Test case for org_list_repos

        List an organization's repos  # noqa: E501
        """
        pass

    def test_org_list_team_member(self):
        """Test case for org_list_team_member

        List a particular member of team  # noqa: E501
        """
        pass

    def test_org_list_team_members(self):
        """Test case for org_list_team_members

        List a team's members  # noqa: E501
        """
        pass

    def test_org_list_team_repo(self):
        """Test case for org_list_team_repo

        List a particular repo of team  # noqa: E501
        """
        pass

    def test_org_list_team_repos(self):
        """Test case for org_list_team_repos

        List a team's repos  # noqa: E501
        """
        pass

    def test_org_list_teams(self):
        """Test case for org_list_teams

        List an organization's teams  # noqa: E501
        """
        pass

    def test_org_list_user_orgs(self):
        """Test case for org_list_user_orgs

        List a user's organizations  # noqa: E501
        """
        pass

    def test_org_publicize_member(self):
        """Test case for org_publicize_member

        Publicize a user's membership  # noqa: E501
        """
        pass

    def test_org_remove_team_member(self):
        """Test case for org_remove_team_member

        Remove a team member  # noqa: E501
        """
        pass

    def test_org_remove_team_repository(self):
        """Test case for org_remove_team_repository

        Remove a repository from a team  # noqa: E501
        """
        pass

    def test_team_search(self):
        """Test case for team_search

        Search for teams within an organization  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()

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
from py_gitea_opensuse_org.api.user_api import UserApi  # noqa: E501
from py_gitea_opensuse_org.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = py_gitea_opensuse_org.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_current_user_repo(self):
        """Test case for create_current_user_repo

        Create a repository  # noqa: E501
        """
        pass

    def test_get_user_settings(self):
        """Test case for get_user_settings

        Get user settings  # noqa: E501
        """
        pass

    def test_get_verification_token(self):
        """Test case for get_verification_token

        Get a Token to verify  # noqa: E501
        """
        pass

    def test_update_user_settings(self):
        """Test case for update_user_settings

        Update user settings  # noqa: E501
        """
        pass

    def test_user_add_email(self):
        """Test case for user_add_email

        Add email addresses  # noqa: E501
        """
        pass

    def test_user_check_following(self):
        """Test case for user_check_following

        Check if one user is following another user  # noqa: E501
        """
        pass

    def test_user_create_o_auth2_application(self):
        """Test case for user_create_o_auth2_application

        creates a new OAuth2 application  # noqa: E501
        """
        pass

    def test_user_create_token(self):
        """Test case for user_create_token

        Create an access token  # noqa: E501
        """
        pass

    def test_user_current_check_following(self):
        """Test case for user_current_check_following

        Check whether a user is followed by the authenticated user  # noqa: E501
        """
        pass

    def test_user_current_check_starring(self):
        """Test case for user_current_check_starring

        Whether the authenticated is starring the repo  # noqa: E501
        """
        pass

    def test_user_current_delete_follow(self):
        """Test case for user_current_delete_follow

        Unfollow a user  # noqa: E501
        """
        pass

    def test_user_current_delete_gpg_key(self):
        """Test case for user_current_delete_gpg_key

        Remove a GPG key  # noqa: E501
        """
        pass

    def test_user_current_delete_key(self):
        """Test case for user_current_delete_key

        Delete a public key  # noqa: E501
        """
        pass

    def test_user_current_delete_star(self):
        """Test case for user_current_delete_star

        Unstar the given repo  # noqa: E501
        """
        pass

    def test_user_current_get_gpg_key(self):
        """Test case for user_current_get_gpg_key

        Get a GPG key  # noqa: E501
        """
        pass

    def test_user_current_get_key(self):
        """Test case for user_current_get_key

        Get a public key  # noqa: E501
        """
        pass

    def test_user_current_list_followers(self):
        """Test case for user_current_list_followers

        List the authenticated user's followers  # noqa: E501
        """
        pass

    def test_user_current_list_following(self):
        """Test case for user_current_list_following

        List the users that the authenticated user is following  # noqa: E501
        """
        pass

    def test_user_current_list_gpg_keys(self):
        """Test case for user_current_list_gpg_keys

        List the authenticated user's GPG keys  # noqa: E501
        """
        pass

    def test_user_current_list_keys(self):
        """Test case for user_current_list_keys

        List the authenticated user's public keys  # noqa: E501
        """
        pass

    def test_user_current_list_repos(self):
        """Test case for user_current_list_repos

        List the repos that the authenticated user owns  # noqa: E501
        """
        pass

    def test_user_current_list_starred(self):
        """Test case for user_current_list_starred

        The repos that the authenticated user has starred  # noqa: E501
        """
        pass

    def test_user_current_list_subscriptions(self):
        """Test case for user_current_list_subscriptions

        List repositories watched by the authenticated user  # noqa: E501
        """
        pass

    def test_user_current_post_gpg_key(self):
        """Test case for user_current_post_gpg_key

        Create a GPG key  # noqa: E501
        """
        pass

    def test_user_current_post_key(self):
        """Test case for user_current_post_key

        Create a public key  # noqa: E501
        """
        pass

    def test_user_current_put_follow(self):
        """Test case for user_current_put_follow

        Follow a user  # noqa: E501
        """
        pass

    def test_user_current_put_star(self):
        """Test case for user_current_put_star

        Star the given repo  # noqa: E501
        """
        pass

    def test_user_current_tracked_times(self):
        """Test case for user_current_tracked_times

        List the current user's tracked times  # noqa: E501
        """
        pass

    def test_user_delete_access_token(self):
        """Test case for user_delete_access_token

        delete an access token  # noqa: E501
        """
        pass

    def test_user_delete_email(self):
        """Test case for user_delete_email

        Delete email addresses  # noqa: E501
        """
        pass

    def test_user_delete_o_auth2_application(self):
        """Test case for user_delete_o_auth2_application

        delete an OAuth2 Application  # noqa: E501
        """
        pass

    def test_user_get(self):
        """Test case for user_get

        Get a user  # noqa: E501
        """
        pass

    def test_user_get_current(self):
        """Test case for user_get_current

        Get the authenticated user  # noqa: E501
        """
        pass

    def test_user_get_heatmap_data(self):
        """Test case for user_get_heatmap_data

        Get a user's heatmap  # noqa: E501
        """
        pass

    def test_user_get_o_auth2_application(self):
        """Test case for user_get_o_auth2_application

        get an OAuth2 Application  # noqa: E501
        """
        pass

    def test_user_get_oauth2_application(self):
        """Test case for user_get_oauth2_application

        List the authenticated user's oauth2 applications  # noqa: E501
        """
        pass

    def test_user_get_stop_watches(self):
        """Test case for user_get_stop_watches

        Get list of all existing stopwatches  # noqa: E501
        """
        pass

    def test_user_get_tokens(self):
        """Test case for user_get_tokens

        List the authenticated user's access tokens  # noqa: E501
        """
        pass

    def test_user_list_emails(self):
        """Test case for user_list_emails

        List the authenticated user's email addresses  # noqa: E501
        """
        pass

    def test_user_list_followers(self):
        """Test case for user_list_followers

        List the given user's followers  # noqa: E501
        """
        pass

    def test_user_list_following(self):
        """Test case for user_list_following

        List the users that the given user is following  # noqa: E501
        """
        pass

    def test_user_list_gpg_keys(self):
        """Test case for user_list_gpg_keys

        List the given user's GPG keys  # noqa: E501
        """
        pass

    def test_user_list_keys(self):
        """Test case for user_list_keys

        List the given user's public keys  # noqa: E501
        """
        pass

    def test_user_list_repos(self):
        """Test case for user_list_repos

        List the repos owned by the given user  # noqa: E501
        """
        pass

    def test_user_list_starred(self):
        """Test case for user_list_starred

        The repos that the given user has starred  # noqa: E501
        """
        pass

    def test_user_list_subscriptions(self):
        """Test case for user_list_subscriptions

        List the repositories watched by a user  # noqa: E501
        """
        pass

    def test_user_list_teams(self):
        """Test case for user_list_teams

        List all the teams a user belongs to  # noqa: E501
        """
        pass

    def test_user_search(self):
        """Test case for user_search

        Search for users  # noqa: E501
        """
        pass

    def test_user_update_o_auth2_application(self):
        """Test case for user_update_o_auth2_application

        update an OAuth2 Application, this includes regenerating the client secret  # noqa: E501
        """
        pass

    def test_user_verify_gpg_key(self):
        """Test case for user_verify_gpg_key

        Verify a GPG key  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

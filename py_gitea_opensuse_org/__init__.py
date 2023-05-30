# coding: utf-8

# flake8: noqa

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


__version__ = "1.0.0"

# import apis into sdk package
from py_gitea_opensuse_org.api.activitypub_api import ActivitypubApi
from py_gitea_opensuse_org.api.admin_api import AdminApi
from py_gitea_opensuse_org.api.issue_api import IssueApi
from py_gitea_opensuse_org.api.miscellaneous_api import MiscellaneousApi
from py_gitea_opensuse_org.api.notification_api import NotificationApi
from py_gitea_opensuse_org.api.organization_api import OrganizationApi
from py_gitea_opensuse_org.api.package_api import PackageApi
from py_gitea_opensuse_org.api.repository_api import RepositoryApi
from py_gitea_opensuse_org.api.settings_api import SettingsApi
from py_gitea_opensuse_org.api.user_api import UserApi

# import ApiClient
from py_gitea_opensuse_org.api_response import ApiResponse
from py_gitea_opensuse_org.api_client import ApiClient
from py_gitea_opensuse_org.configuration import Configuration
from py_gitea_opensuse_org.exceptions import OpenApiException
from py_gitea_opensuse_org.exceptions import ApiTypeError
from py_gitea_opensuse_org.exceptions import ApiValueError
from py_gitea_opensuse_org.exceptions import ApiKeyError
from py_gitea_opensuse_org.exceptions import ApiAttributeError
from py_gitea_opensuse_org.exceptions import ApiException

# import models into sdk package
from py_gitea_opensuse_org.models.api_error import APIError
from py_gitea_opensuse_org.models.access_token import AccessToken
from py_gitea_opensuse_org.models.activity_pub import ActivityPub
from py_gitea_opensuse_org.models.add_collaborator_option import AddCollaboratorOption
from py_gitea_opensuse_org.models.add_time_option import AddTimeOption
from py_gitea_opensuse_org.models.annotated_tag import AnnotatedTag
from py_gitea_opensuse_org.models.annotated_tag_object import AnnotatedTagObject
from py_gitea_opensuse_org.models.attachment import Attachment
from py_gitea_opensuse_org.models.branch import Branch
from py_gitea_opensuse_org.models.branch_protection import BranchProtection
from py_gitea_opensuse_org.models.changed_file import ChangedFile
from py_gitea_opensuse_org.models.combined_status import CombinedStatus
from py_gitea_opensuse_org.models.comment import Comment
from py_gitea_opensuse_org.models.commit import Commit
from py_gitea_opensuse_org.models.commit_affected_files import CommitAffectedFiles
from py_gitea_opensuse_org.models.commit_date_options import CommitDateOptions
from py_gitea_opensuse_org.models.commit_meta import CommitMeta
from py_gitea_opensuse_org.models.commit_stats import CommitStats
from py_gitea_opensuse_org.models.commit_status import CommitStatus
from py_gitea_opensuse_org.models.commit_user import CommitUser
from py_gitea_opensuse_org.models.contents_response import ContentsResponse
from py_gitea_opensuse_org.models.create_access_token_option import CreateAccessTokenOption
from py_gitea_opensuse_org.models.create_branch_protection_option import CreateBranchProtectionOption
from py_gitea_opensuse_org.models.create_branch_repo_option import CreateBranchRepoOption
from py_gitea_opensuse_org.models.create_email_option import CreateEmailOption
from py_gitea_opensuse_org.models.create_file_options import CreateFileOptions
from py_gitea_opensuse_org.models.create_fork_option import CreateForkOption
from py_gitea_opensuse_org.models.create_gpg_key_option import CreateGPGKeyOption
from py_gitea_opensuse_org.models.create_hook_option import CreateHookOption
from py_gitea_opensuse_org.models.create_issue_comment_option import CreateIssueCommentOption
from py_gitea_opensuse_org.models.create_issue_option import CreateIssueOption
from py_gitea_opensuse_org.models.create_key_option import CreateKeyOption
from py_gitea_opensuse_org.models.create_label_option import CreateLabelOption
from py_gitea_opensuse_org.models.create_milestone_option import CreateMilestoneOption
from py_gitea_opensuse_org.models.create_o_auth2_application_options import CreateOAuth2ApplicationOptions
from py_gitea_opensuse_org.models.create_org_option import CreateOrgOption
from py_gitea_opensuse_org.models.create_pull_request_option import CreatePullRequestOption
from py_gitea_opensuse_org.models.create_pull_review_comment import CreatePullReviewComment
from py_gitea_opensuse_org.models.create_pull_review_options import CreatePullReviewOptions
from py_gitea_opensuse_org.models.create_push_mirror_option import CreatePushMirrorOption
from py_gitea_opensuse_org.models.create_release_option import CreateReleaseOption
from py_gitea_opensuse_org.models.create_repo_option import CreateRepoOption
from py_gitea_opensuse_org.models.create_status_option import CreateStatusOption
from py_gitea_opensuse_org.models.create_tag_option import CreateTagOption
from py_gitea_opensuse_org.models.create_team_option import CreateTeamOption
from py_gitea_opensuse_org.models.create_user_option import CreateUserOption
from py_gitea_opensuse_org.models.create_wiki_page_options import CreateWikiPageOptions
from py_gitea_opensuse_org.models.cron import Cron
from py_gitea_opensuse_org.models.delete_email_option import DeleteEmailOption
from py_gitea_opensuse_org.models.delete_file_options import DeleteFileOptions
from py_gitea_opensuse_org.models.deploy_key import DeployKey
from py_gitea_opensuse_org.models.dismiss_pull_review_options import DismissPullReviewOptions
from py_gitea_opensuse_org.models.edit_attachment_options import EditAttachmentOptions
from py_gitea_opensuse_org.models.edit_branch_protection_option import EditBranchProtectionOption
from py_gitea_opensuse_org.models.edit_deadline_option import EditDeadlineOption
from py_gitea_opensuse_org.models.edit_git_hook_option import EditGitHookOption
from py_gitea_opensuse_org.models.edit_hook_option import EditHookOption
from py_gitea_opensuse_org.models.edit_issue_comment_option import EditIssueCommentOption
from py_gitea_opensuse_org.models.edit_issue_option import EditIssueOption
from py_gitea_opensuse_org.models.edit_label_option import EditLabelOption
from py_gitea_opensuse_org.models.edit_milestone_option import EditMilestoneOption
from py_gitea_opensuse_org.models.edit_org_option import EditOrgOption
from py_gitea_opensuse_org.models.edit_pull_request_option import EditPullRequestOption
from py_gitea_opensuse_org.models.edit_reaction_option import EditReactionOption
from py_gitea_opensuse_org.models.edit_release_option import EditReleaseOption
from py_gitea_opensuse_org.models.edit_repo_option import EditRepoOption
from py_gitea_opensuse_org.models.edit_team_option import EditTeamOption
from py_gitea_opensuse_org.models.edit_user_option import EditUserOption
from py_gitea_opensuse_org.models.email import Email
from py_gitea_opensuse_org.models.external_tracker import ExternalTracker
from py_gitea_opensuse_org.models.external_wiki import ExternalWiki
from py_gitea_opensuse_org.models.file_commit_response import FileCommitResponse
from py_gitea_opensuse_org.models.file_delete_response import FileDeleteResponse
from py_gitea_opensuse_org.models.file_links_response import FileLinksResponse
from py_gitea_opensuse_org.models.file_response import FileResponse
from py_gitea_opensuse_org.models.gpg_key import GPGKey
from py_gitea_opensuse_org.models.gpg_key_email import GPGKeyEmail
from py_gitea_opensuse_org.models.general_api_settings import GeneralAPISettings
from py_gitea_opensuse_org.models.general_attachment_settings import GeneralAttachmentSettings
from py_gitea_opensuse_org.models.general_repo_settings import GeneralRepoSettings
from py_gitea_opensuse_org.models.general_ui_settings import GeneralUISettings
from py_gitea_opensuse_org.models.generate_repo_option import GenerateRepoOption
from py_gitea_opensuse_org.models.git_blob_response import GitBlobResponse
from py_gitea_opensuse_org.models.git_entry import GitEntry
from py_gitea_opensuse_org.models.git_hook import GitHook
from py_gitea_opensuse_org.models.git_object import GitObject
from py_gitea_opensuse_org.models.git_tree_response import GitTreeResponse
from py_gitea_opensuse_org.models.hook import Hook
from py_gitea_opensuse_org.models.identity import Identity
from py_gitea_opensuse_org.models.internal_tracker import InternalTracker
from py_gitea_opensuse_org.models.issue import Issue
from py_gitea_opensuse_org.models.issue_deadline import IssueDeadline
from py_gitea_opensuse_org.models.issue_form_field import IssueFormField
from py_gitea_opensuse_org.models.issue_labels_option import IssueLabelsOption
from py_gitea_opensuse_org.models.issue_template import IssueTemplate
from py_gitea_opensuse_org.models.label import Label
from py_gitea_opensuse_org.models.markdown_option import MarkdownOption
from py_gitea_opensuse_org.models.merge_pull_request_option import MergePullRequestOption
from py_gitea_opensuse_org.models.migrate_repo_options import MigrateRepoOptions
from py_gitea_opensuse_org.models.milestone import Milestone
from py_gitea_opensuse_org.models.node_info import NodeInfo
from py_gitea_opensuse_org.models.node_info_services import NodeInfoServices
from py_gitea_opensuse_org.models.node_info_software import NodeInfoSoftware
from py_gitea_opensuse_org.models.node_info_usage import NodeInfoUsage
from py_gitea_opensuse_org.models.node_info_usage_users import NodeInfoUsageUsers
from py_gitea_opensuse_org.models.note import Note
from py_gitea_opensuse_org.models.notification_count import NotificationCount
from py_gitea_opensuse_org.models.notification_subject import NotificationSubject
from py_gitea_opensuse_org.models.notification_thread import NotificationThread
from py_gitea_opensuse_org.models.o_auth2_application import OAuth2Application
from py_gitea_opensuse_org.models.organization import Organization
from py_gitea_opensuse_org.models.organization_permissions import OrganizationPermissions
from py_gitea_opensuse_org.models.pr_branch_info import PRBranchInfo
from py_gitea_opensuse_org.models.package import Package
from py_gitea_opensuse_org.models.package_file import PackageFile
from py_gitea_opensuse_org.models.payload_commit import PayloadCommit
from py_gitea_opensuse_org.models.payload_commit_verification import PayloadCommitVerification
from py_gitea_opensuse_org.models.payload_user import PayloadUser
from py_gitea_opensuse_org.models.permission import Permission
from py_gitea_opensuse_org.models.public_key import PublicKey
from py_gitea_opensuse_org.models.pull_request import PullRequest
from py_gitea_opensuse_org.models.pull_request_meta import PullRequestMeta
from py_gitea_opensuse_org.models.pull_review import PullReview
from py_gitea_opensuse_org.models.pull_review_comment import PullReviewComment
from py_gitea_opensuse_org.models.pull_review_request_options import PullReviewRequestOptions
from py_gitea_opensuse_org.models.push_mirror import PushMirror
from py_gitea_opensuse_org.models.reaction import Reaction
from py_gitea_opensuse_org.models.reference import Reference
from py_gitea_opensuse_org.models.release import Release
from py_gitea_opensuse_org.models.repo_collaborator_permission import RepoCollaboratorPermission
from py_gitea_opensuse_org.models.repo_commit import RepoCommit
from py_gitea_opensuse_org.models.repo_topic_options import RepoTopicOptions
from py_gitea_opensuse_org.models.repo_transfer import RepoTransfer
from py_gitea_opensuse_org.models.repository import Repository
from py_gitea_opensuse_org.models.repository_meta import RepositoryMeta
from py_gitea_opensuse_org.models.search_results import SearchResults
from py_gitea_opensuse_org.models.server_version import ServerVersion
from py_gitea_opensuse_org.models.stop_watch import StopWatch
from py_gitea_opensuse_org.models.submit_pull_review_options import SubmitPullReviewOptions
from py_gitea_opensuse_org.models.tag import Tag
from py_gitea_opensuse_org.models.team import Team
from py_gitea_opensuse_org.models.team_search200_response import TeamSearch200Response
from py_gitea_opensuse_org.models.timeline_comment import TimelineComment
from py_gitea_opensuse_org.models.topic_name import TopicName
from py_gitea_opensuse_org.models.topic_response import TopicResponse
from py_gitea_opensuse_org.models.tracked_time import TrackedTime
from py_gitea_opensuse_org.models.transfer_repo_option import TransferRepoOption
from py_gitea_opensuse_org.models.update_file_options import UpdateFileOptions
from py_gitea_opensuse_org.models.user import User
from py_gitea_opensuse_org.models.user_heatmap_data import UserHeatmapData
from py_gitea_opensuse_org.models.user_search200_response import UserSearch200Response
from py_gitea_opensuse_org.models.user_settings import UserSettings
from py_gitea_opensuse_org.models.user_settings_options import UserSettingsOptions
from py_gitea_opensuse_org.models.watch_info import WatchInfo
from py_gitea_opensuse_org.models.wiki_commit import WikiCommit
from py_gitea_opensuse_org.models.wiki_commit_list import WikiCommitList
from py_gitea_opensuse_org.models.wiki_page import WikiPage
from py_gitea_opensuse_org.models.wiki_page_meta_data import WikiPageMetaData

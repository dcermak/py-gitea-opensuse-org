# PullRequest

PullRequest represents a pull request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additions** | **int** | The number of lines added in the pull request | [optional] 
**allow_maintainer_edit** | **bool** | Whether maintainers can edit the pull request | [optional] 
**assignee** | [**User**](User.md) |  | [optional] 
**assignees** | [**List[User]**](User.md) | The list of users assigned to the pull request | [optional] 
**base** | [**PRBranchInfo**](PRBranchInfo.md) |  | [optional] 
**body** | **str** | The description body of the pull request | [optional] 
**changed_files** | **int** | The number of files changed in the pull request | [optional] 
**closed_at** | **datetime** |  | [optional] 
**comments** | **int** | The number of comments on the pull request | [optional] 
**created_at** | **datetime** |  | [optional] 
**deletions** | **int** | The number of lines deleted in the pull request | [optional] 
**diff_url** | **str** | The URL to download the diff patch | [optional] 
**draft** | **bool** | Whether the pull request is a draft | [optional] 
**due_date** | **datetime** |  | [optional] 
**head** | [**PRBranchInfo**](PRBranchInfo.md) |  | [optional] 
**html_url** | **str** | The HTML URL to view the pull request | [optional] 
**id** | **int** | The unique identifier of the pull request | [optional] 
**is_locked** | **bool** | Whether the pull request conversation is locked | [optional] 
**labels** | [**List[Label]**](Label.md) | The labels attached to the pull request | [optional] 
**merge_base** | **str** | The merge base commit SHA | [optional] 
**merge_commit_sha** | **str** | The SHA of the merge commit | [optional] 
**mergeable** | **bool** | Whether the pull request can be merged | [optional] 
**merged** | **bool** | Whether the pull request has been merged | [optional] 
**merged_at** | **datetime** |  | [optional] 
**merged_by** | [**User**](User.md) |  | [optional] 
**milestone** | [**Milestone**](Milestone.md) |  | [optional] 
**number** | **int** | The pull request number | [optional] 
**patch_url** | **str** | The URL to download the patch file | [optional] 
**pin_order** | **int** | The pin order for the pull request | [optional] 
**requested_reviewers** | [**List[User]**](User.md) | The users requested to review the pull request | [optional] 
**requested_reviewers_teams** | [**List[Team]**](Team.md) | The teams requested to review the pull request | [optional] 
**review_comments** | **int** | number of review comments made on the diff of a PR review (not including comments on commits or issues in a PR) | [optional] 
**state** | **str** | StateType issue state type | [optional] 
**title** | **str** | The title of the pull request | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** | The API URL of the pull request | [optional] 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.pull_request import PullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequest from a JSON string
pull_request_instance = PullRequest.from_json(json)
# print the JSON string representation of the object
print(PullRequest.to_json())

# convert the object into a dict
pull_request_dict = pull_request_instance.to_dict()
# create an instance of PullRequest from a dict
pull_request_from_dict = PullRequest.from_dict(pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



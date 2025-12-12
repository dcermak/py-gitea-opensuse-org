# TimelineComment

TimelineComment represents a timeline comment (comment of any type) on a commit or issue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | [**User**](User.md) |  | [optional] 
**assignee_team** | [**Team**](Team.md) |  | [optional] 
**body** | **str** | Body contains the timeline event content | [optional] 
**created_at** | **datetime** |  | [optional] 
**dependent_issue** | [**Issue**](Issue.md) |  | [optional] 
**html_url** | **str** | HTMLURL is the web URL for viewing the comment | [optional] 
**id** | **int** | ID is the unique identifier for the timeline comment | [optional] 
**issue_url** | **str** | IssueURL is the API URL for the issue | [optional] 
**label** | [**Label**](Label.md) |  | [optional] 
**milestone** | [**Milestone**](Milestone.md) |  | [optional] 
**new_ref** | **str** |  | [optional] 
**new_title** | **str** |  | [optional] 
**old_milestone** | [**Milestone**](Milestone.md) |  | [optional] 
**old_project_id** | **int** |  | [optional] 
**old_ref** | **str** |  | [optional] 
**old_title** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**pull_request_url** | **str** | PRURL is the API URL for the pull request (if applicable) | [optional] 
**ref_action** | **str** |  | [optional] 
**ref_comment** | [**Comment**](Comment.md) |  | [optional] 
**ref_commit_sha** | **str** | commit SHA where issue/PR was referenced | [optional] 
**ref_issue** | [**Issue**](Issue.md) |  | [optional] 
**removed_assignee** | **bool** | whether the assignees were removed or added | [optional] 
**resolve_doer** | [**User**](User.md) |  | [optional] 
**review_id** | **int** |  | [optional] 
**tracked_time** | [**TrackedTime**](TrackedTime.md) |  | [optional] 
**type** | **str** | Type indicates the type of timeline event | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.timeline_comment import TimelineComment

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineComment from a JSON string
timeline_comment_instance = TimelineComment.from_json(json)
# print the JSON string representation of the object
print(TimelineComment.to_json())

# convert the object into a dict
timeline_comment_dict = timeline_comment_instance.to_dict()
# create an instance of TimelineComment from a dict
timeline_comment_from_dict = TimelineComment.from_dict(timeline_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



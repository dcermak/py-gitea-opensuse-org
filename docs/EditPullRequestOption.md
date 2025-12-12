# EditPullRequestOption

EditPullRequestOption options when modify pull request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_maintainer_edit** | **bool** | Whether to allow maintainer edits | [optional] 
**assignee** | **str** | The new primary assignee username | [optional] 
**assignees** | **List[str]** | The new list of assignee usernames | [optional] 
**base** | **str** | The new base branch for the pull request | [optional] 
**body** | **str** | The new description body for the pull request | [optional] 
**due_date** | **datetime** |  | [optional] 
**labels** | **List[int]** | The new list of label IDs for the pull request | [optional] 
**milestone** | **int** | The new milestone ID for the pull request | [optional] 
**state** | **str** | The new state for the pull request | [optional] 
**title** | **str** | The new title for the pull request | [optional] 
**unset_due_date** | **bool** | Whether to remove the current deadline | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.edit_pull_request_option import EditPullRequestOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditPullRequestOption from a JSON string
edit_pull_request_option_instance = EditPullRequestOption.from_json(json)
# print the JSON string representation of the object
print(EditPullRequestOption.to_json())

# convert the object into a dict
edit_pull_request_option_dict = edit_pull_request_option_instance.to_dict()
# create an instance of EditPullRequestOption from a dict
edit_pull_request_option_from_dict = EditPullRequestOption.from_dict(edit_pull_request_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



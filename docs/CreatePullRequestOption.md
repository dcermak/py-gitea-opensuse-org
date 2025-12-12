# CreatePullRequestOption

CreatePullRequestOption options when creating a pull request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | **str** | The primary assignee username | [optional] 
**assignees** | **List[str]** | The list of assignee usernames | [optional] 
**base** | **str** | The base branch for the pull request | [optional] 
**body** | **str** | The description body of the pull request | [optional] 
**due_date** | **datetime** |  | [optional] 
**head** | **str** | The head branch for the pull request, it could be a branch name on the base repository or a form like &#x60;&lt;username&gt;:&lt;branch&gt;&#x60; which refers to the user&#39;s fork repository&#39;s branch. | [optional] 
**labels** | **List[int]** | The list of label IDs to assign to the pull request | [optional] 
**milestone** | **int** | The milestone ID to assign to the pull request | [optional] 
**reviewers** | **List[str]** | The list of reviewer usernames | [optional] 
**team_reviewers** | **List[str]** | The list of team reviewer names | [optional] 
**title** | **str** | The title of the pull request | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.create_pull_request_option import CreatePullRequestOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePullRequestOption from a JSON string
create_pull_request_option_instance = CreatePullRequestOption.from_json(json)
# print the JSON string representation of the object
print(CreatePullRequestOption.to_json())

# convert the object into a dict
create_pull_request_option_dict = create_pull_request_option_instance.to_dict()
# create an instance of CreatePullRequestOption from a dict
create_pull_request_option_from_dict = CreatePullRequestOption.from_dict(create_pull_request_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



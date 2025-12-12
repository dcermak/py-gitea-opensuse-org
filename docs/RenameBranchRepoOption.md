# RenameBranchRepoOption

RenameBranchRepoOption options when renaming a branch in a repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New branch name | 

## Example

```python
from py_gitea_opensuse_org.models.rename_branch_repo_option import RenameBranchRepoOption

# TODO update the JSON string below
json = "{}"
# create an instance of RenameBranchRepoOption from a JSON string
rename_branch_repo_option_instance = RenameBranchRepoOption.from_json(json)
# print the JSON string representation of the object
print(RenameBranchRepoOption.to_json())

# convert the object into a dict
rename_branch_repo_option_dict = rename_branch_repo_option_instance.to_dict()
# create an instance of RenameBranchRepoOption from a dict
rename_branch_repo_option_from_dict = RenameBranchRepoOption.from_dict(rename_branch_repo_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ReparentRepoOption

ReparentRepoOption options when reparenting a repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_owner** | **str** | name of the organization or user that owns the fork to be promoted | 

## Example

```python
from py_gitea_opensuse_org.models.reparent_repo_option import ReparentRepoOption

# TODO update the JSON string below
json = "{}"
# create an instance of ReparentRepoOption from a JSON string
reparent_repo_option_instance = ReparentRepoOption.from_json(json)
# print the JSON string representation of the object
print(ReparentRepoOption.to_json())

# convert the object into a dict
reparent_repo_option_dict = reparent_repo_option_instance.to_dict()
# create an instance of ReparentRepoOption from a dict
reparent_repo_option_from_dict = ReparentRepoOption.from_dict(reparent_repo_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



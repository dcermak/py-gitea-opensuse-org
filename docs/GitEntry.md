# GitEntry

GitEntry represents a git tree

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.git_entry import GitEntry

# TODO update the JSON string below
json = "{}"
# create an instance of GitEntry from a JSON string
git_entry_instance = GitEntry.from_json(json)
# print the JSON string representation of the object
print(GitEntry.to_json())

# convert the object into a dict
git_entry_dict = git_entry_instance.to_dict()
# create an instance of GitEntry from a dict
git_entry_from_dict = GitEntry.from_dict(git_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



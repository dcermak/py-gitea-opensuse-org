# GitEntry

GitEntry represents a git tree

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Mode is the file mode (permissions) | [optional] 
**path** | **str** | Path is the file or directory path | [optional] 
**sha** | **str** | SHA is the Git object SHA | [optional] 
**size** | **int** | Size is the file size in bytes | [optional] 
**type** | **str** | Type indicates if this is a file, directory, or symlink | [optional] 
**url** | **str** | URL is the API URL for this tree entry | [optional] 

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



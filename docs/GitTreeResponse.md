# GitTreeResponse

GitTreeResponse returns a git tree

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Page is the current page number for pagination | [optional] 
**sha** | **str** | SHA is the tree object SHA | [optional] 
**total_count** | **int** | TotalCount is the total number of entries in the tree | [optional] 
**tree** | [**List[GitEntry]**](GitEntry.md) | Entries contains the tree entries (files and directories) | [optional] 
**truncated** | **bool** | Truncated indicates if the response was truncated due to size | [optional] 
**url** | **str** | URL is the API URL for this tree | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.git_tree_response import GitTreeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitTreeResponse from a JSON string
git_tree_response_instance = GitTreeResponse.from_json(json)
# print the JSON string representation of the object
print(GitTreeResponse.to_json())

# convert the object into a dict
git_tree_response_dict = git_tree_response_instance.to_dict()
# create an instance of GitTreeResponse from a dict
git_tree_response_from_dict = GitTreeResponse.from_dict(git_tree_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



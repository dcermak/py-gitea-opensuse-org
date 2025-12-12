# GitObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** | The SHA hash of the Git object | [optional] 
**type** | **str** | The type of the Git object (e.g., commit, tag, tree, blob) | [optional] 
**url** | **str** | The URL to access this Git object | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.git_object import GitObject

# TODO update the JSON string below
json = "{}"
# create an instance of GitObject from a JSON string
git_object_instance = GitObject.from_json(json)
# print the JSON string representation of the object
print(GitObject.to_json())

# convert the object into a dict
git_object_dict = git_object_instance.to_dict()
# create an instance of GitObject from a dict
git_object_from_dict = GitObject.from_dict(git_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



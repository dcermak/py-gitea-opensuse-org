# GitHook

GitHook represents a Git repository hook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Content contains the script content of the hook | [optional] 
**is_active** | **bool** | IsActive indicates if the hook is active | [optional] 
**name** | **str** | Name is the name of the Git hook | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.git_hook import GitHook

# TODO update the JSON string below
json = "{}"
# create an instance of GitHook from a JSON string
git_hook_instance = GitHook.from_json(json)
# print the JSON string representation of the object
print(GitHook.to_json())

# convert the object into a dict
git_hook_dict = git_hook_instance.to_dict()
# create an instance of GitHook from a dict
git_hook_from_dict = GitHook.from_dict(git_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



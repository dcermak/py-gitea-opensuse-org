# ChangeFilesOptions

ChangeFilesOptions options for creating, updating or deleting multiple files Note: `author` and `committer` are optional (if only one is given, it will be used for the other, otherwise the authenticated user will be used)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**Identity**](Identity.md) |  | [optional] 
**branch** | **str** | branch (optional) is the base branch for the changes. If not supplied, the default branch is used | [optional] 
**committer** | [**Identity**](Identity.md) |  | [optional] 
**dates** | [**CommitDateOptions**](CommitDateOptions.md) |  | [optional] 
**files** | [**List[ChangeFileOperation]**](ChangeFileOperation.md) | list of file operations | 
**force_push** | **bool** | force_push (optional) will do a force-push if the new branch already exists | [optional] 
**message** | **str** | message (optional) is the commit message of the changes. If not supplied, a default message will be used | [optional] 
**new_branch** | **str** | new_branch (optional) will make a new branch from base branch for the changes. If not supplied, the changes will be committed to the base branch | [optional] 
**signoff** | **bool** | Add a Signed-off-by trailer by the committer at the end of the commit log message. | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.change_files_options import ChangeFilesOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeFilesOptions from a JSON string
change_files_options_instance = ChangeFilesOptions.from_json(json)
# print the JSON string representation of the object
print(ChangeFilesOptions.to_json())

# convert the object into a dict
change_files_options_dict = change_files_options_instance.to_dict()
# create an instance of ChangeFilesOptions from a dict
change_files_options_from_dict = ChangeFilesOptions.from_dict(change_files_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



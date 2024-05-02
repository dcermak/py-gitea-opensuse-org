# UpdateFileOptions

UpdateFileOptions options for updating files Note: `author` and `committer` are optional (if only one is given, it will be used for the other, otherwise the authenticated user will be used)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**Identity**](Identity.md) |  | [optional] 
**branch** | **str** | branch (optional) to base this file from. if not given, the default branch is used | [optional] 
**committer** | [**Identity**](Identity.md) |  | [optional] 
**content** | **str** | content must be base64 encoded | 
**dates** | [**CommitDateOptions**](CommitDateOptions.md) |  | [optional] 
**from_path** | **str** | from_path (optional) is the path of the original file which will be moved/renamed to the path in the URL | [optional] 
**message** | **str** | message (optional) for the commit of this file. if not supplied, a default message will be used | [optional] 
**new_branch** | **str** | new_branch (optional) will make a new branch from &#x60;branch&#x60; before creating the file | [optional] 
**sha** | **str** | sha is the SHA for the file that already exists | 
**signoff** | **bool** | Add a Signed-off-by trailer by the committer at the end of the commit log message. | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.update_file_options import UpdateFileOptions

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFileOptions from a JSON string
update_file_options_instance = UpdateFileOptions.from_json(json)
# print the JSON string representation of the object
print(UpdateFileOptions.to_json())

# convert the object into a dict
update_file_options_dict = update_file_options_instance.to_dict()
# create an instance of UpdateFileOptions from a dict
update_file_options_from_dict = UpdateFileOptions.from_dict(update_file_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



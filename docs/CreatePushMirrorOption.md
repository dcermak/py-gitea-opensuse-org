# CreatePushMirrorOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** | The sync interval for automatic updates | [optional] 
**remote_address** | **str** | The remote repository URL to push to | [optional] 
**remote_password** | **str** | The password for authentication with the remote repository | [optional] 
**remote_username** | **str** | The username for authentication with the remote repository | [optional] 
**sync_on_commit** | **bool** | Whether to sync on every commit | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.create_push_mirror_option import CreatePushMirrorOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePushMirrorOption from a JSON string
create_push_mirror_option_instance = CreatePushMirrorOption.from_json(json)
# print the JSON string representation of the object
print(CreatePushMirrorOption.to_json())

# convert the object into a dict
create_push_mirror_option_dict = create_push_mirror_option_instance.to_dict()
# create an instance of CreatePushMirrorOption from a dict
create_push_mirror_option_from_dict = CreatePushMirrorOption.from_dict(create_push_mirror_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# WatchInfo

WatchInfo represents an API watch status of one repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The timestamp when the watch status was created | [optional] 
**ignored** | **bool** | Whether notifications for the repository are ignored | [optional] 
**reason** | **object** | The reason for the current watch status | [optional] 
**repository_url** | **str** | The URL of the repository being watched | [optional] 
**subscribed** | **bool** | Whether the repository is being watched for notifications | [optional] 
**url** | **str** | The URL for managing the watch status | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.watch_info import WatchInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WatchInfo from a JSON string
watch_info_instance = WatchInfo.from_json(json)
# print the JSON string representation of the object
print(WatchInfo.to_json())

# convert the object into a dict
watch_info_dict = watch_info_instance.to_dict()
# create an instance of WatchInfo from a dict
watch_info_from_dict = WatchInfo.from_dict(watch_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# NotificationThread

NotificationThread expose Notification on API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID is the unique identifier for the notification thread | [optional] 
**pinned** | **bool** | Pinned indicates if the notification is pinned | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**subject** | [**NotificationSubject**](NotificationSubject.md) |  | [optional] 
**unread** | **bool** | Unread indicates if the notification has been read | [optional] 
**updated_at** | **datetime** | UpdatedAt is the time when the notification was last updated | [optional] 
**url** | **str** | URL is the API URL for this notification thread | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.notification_thread import NotificationThread

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationThread from a JSON string
notification_thread_instance = NotificationThread.from_json(json)
# print the JSON string representation of the object
print(NotificationThread.to_json())

# convert the object into a dict
notification_thread_dict = notification_thread_instance.to_dict()
# create an instance of NotificationThread from a dict
notification_thread_from_dict = NotificationThread.from_dict(notification_thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



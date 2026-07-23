# NotificationSubject

NotificationSubject contains the notification subject (Issue/Pull/Commit)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html_url** | **str** | HTMLURL is the web URL for the notification subject | [optional] 
**latest_comment_html_url** | **str** | LatestCommentHTMLURL is the web URL for the latest comment | [optional] 
**latest_comment_url** | **str** | LatestCommentURL is the API URL for the latest comment | [optional] 
**state** | **str** | State indicates the current state of the notification subject open NotifySubjectStateOpen  NotifySubjectStateOpen is an open subject closed NotifySubjectStateClosed  NotifySubjectStateClosed is a closed subject merged NotifySubjectStateMerged  NotifySubjectStateMerged is a merged pull request | [optional] 
**title** | **str** | Title is the title of the notification subject | [optional] 
**type** | **str** | Type indicates the type of the notification subject Issue NotifySubjectIssue  NotifySubjectIssue an issue is subject of an notification Pull NotifySubjectPull  NotifySubjectPull an pull is subject of an notification Commit NotifySubjectCommit  NotifySubjectCommit an commit is subject of an notification Repository NotifySubjectRepository  NotifySubjectRepository an repository is subject of an notification | [optional] 
**url** | **str** | URL is the API URL for the notification subject | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.notification_subject import NotificationSubject

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSubject from a JSON string
notification_subject_instance = NotificationSubject.from_json(json)
# print the JSON string representation of the object
print(NotificationSubject.to_json())

# convert the object into a dict
notification_subject_dict = notification_subject_instance.to_dict()
# create an instance of NotificationSubject from a dict
notification_subject_from_dict = NotificationSubject.from_dict(notification_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



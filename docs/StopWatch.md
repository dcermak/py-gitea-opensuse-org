# StopWatch

StopWatch represent a running stopwatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**duration** | **str** | Duration is a human-readable duration string | [optional] 
**issue_index** | **int** | IssueIndex is the index number of the associated issue | [optional] 
**issue_title** | **str** | IssueTitle is the title of the associated issue | [optional] 
**repo_name** | **str** | RepoName is the name of the repository | [optional] 
**repo_owner_name** | **str** | RepoOwnerName is the name of the repository owner | [optional] 
**seconds** | **int** | Seconds is the total elapsed time in seconds | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.stop_watch import StopWatch

# TODO update the JSON string below
json = "{}"
# create an instance of StopWatch from a JSON string
stop_watch_instance = StopWatch.from_json(json)
# print the JSON string representation of the object
print(StopWatch.to_json())

# convert the object into a dict
stop_watch_dict = stop_watch_instance.to_dict()
# create an instance of StopWatch from a dict
stop_watch_from_dict = StopWatch.from_dict(stop_watch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



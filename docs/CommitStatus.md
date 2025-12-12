# CommitStatus

CommitStatus holds a single status of a single Commit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | Context is the unique context identifier for the status | [optional] 
**created_at** | **datetime** |  | [optional] 
**creator** | [**User**](User.md) |  | [optional] 
**description** | **str** | Description provides a brief description of the status | [optional] 
**id** | **int** | ID is the unique identifier for the commit status | [optional] 
**status** | **str** | State represents the status state (pending, success, error, failure) pending CommitStatusPending  CommitStatusPending is for when the CommitStatus is Pending success CommitStatusSuccess  CommitStatusSuccess is for when the CommitStatus is Success error CommitStatusError  CommitStatusError is for when the CommitStatus is Error failure CommitStatusFailure  CommitStatusFailure is for when the CommitStatus is Failure warning CommitStatusWarning  CommitStatusWarning is for when the CommitStatus is Warning skipped CommitStatusSkipped  CommitStatusSkipped is for when CommitStatus is Skipped | [optional] 
**target_url** | **str** | TargetURL is the URL to link to for more details | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** | URL is the API URL for this status | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.commit_status import CommitStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CommitStatus from a JSON string
commit_status_instance = CommitStatus.from_json(json)
# print the JSON string representation of the object
print(CommitStatus.to_json())

# convert the object into a dict
commit_status_dict = commit_status_instance.to_dict()
# create an instance of CommitStatus from a dict
commit_status_from_dict = CommitStatus.from_dict(commit_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



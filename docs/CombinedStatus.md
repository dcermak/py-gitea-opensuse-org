# CombinedStatus

CombinedStatus holds the combined state of several statuses for a single commit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_url** | **str** | CommitURL is the API URL for the commit | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**sha** | **str** | SHA is the commit SHA this status applies to | [optional] 
**state** | **str** | State is the overall combined status state pending CommitStatusPending  CommitStatusPending is for when the CommitStatus is Pending success CommitStatusSuccess  CommitStatusSuccess is for when the CommitStatus is Success error CommitStatusError  CommitStatusError is for when the CommitStatus is Error failure CommitStatusFailure  CommitStatusFailure is for when the CommitStatus is Failure warning CommitStatusWarning  CommitStatusWarning is for when the CommitStatus is Warning skipped CommitStatusSkipped  CommitStatusSkipped is for when CommitStatus is Skipped | [optional] 
**statuses** | [**List[CommitStatus]**](CommitStatus.md) | Statuses contains all individual commit statuses | [optional] 
**total_count** | **int** | TotalCount is the total number of statuses | [optional] 
**url** | **str** | URL is the API URL for this combined status | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.combined_status import CombinedStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CombinedStatus from a JSON string
combined_status_instance = CombinedStatus.from_json(json)
# print the JSON string representation of the object
print(CombinedStatus.to_json())

# convert the object into a dict
combined_status_dict = combined_status_instance.to_dict()
# create an instance of CombinedStatus from a dict
combined_status_from_dict = CombinedStatus.from_dict(combined_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



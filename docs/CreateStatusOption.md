# CreateStatusOption

CreateStatusOption holds the information needed to create a new CommitStatus for a Commit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | Context is the unique context identifier for the status | [optional] 
**description** | **str** | Description provides a brief description of the status | [optional] 
**state** | **str** | State represents the status state to set (pending, success, error, failure) pending CommitStatusPending  CommitStatusPending is for when the CommitStatus is Pending success CommitStatusSuccess  CommitStatusSuccess is for when the CommitStatus is Success error CommitStatusError  CommitStatusError is for when the CommitStatus is Error failure CommitStatusFailure  CommitStatusFailure is for when the CommitStatus is Failure warning CommitStatusWarning  CommitStatusWarning is for when the CommitStatus is Warning skipped CommitStatusSkipped  CommitStatusSkipped is for when CommitStatus is Skipped | [optional] 
**target_url** | **str** | TargetURL is the URL to link to for more details | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.create_status_option import CreateStatusOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStatusOption from a JSON string
create_status_option_instance = CreateStatusOption.from_json(json)
# print the JSON string representation of the object
print(CreateStatusOption.to_json())

# convert the object into a dict
create_status_option_dict = create_status_option_instance.to_dict()
# create an instance of CreateStatusOption from a dict
create_status_option_from_dict = CreateStatusOption.from_dict(create_status_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ActionWorkflowJobsResponse

ActionWorkflowJobsResponse returns ActionWorkflowJobs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[ActionWorkflowJob]**](ActionWorkflowJob.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.action_workflow_jobs_response import ActionWorkflowJobsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActionWorkflowJobsResponse from a JSON string
action_workflow_jobs_response_instance = ActionWorkflowJobsResponse.from_json(json)
# print the JSON string representation of the object
print(ActionWorkflowJobsResponse.to_json())

# convert the object into a dict
action_workflow_jobs_response_dict = action_workflow_jobs_response_instance.to_dict()
# create an instance of ActionWorkflowJobsResponse from a dict
action_workflow_jobs_response_from_dict = ActionWorkflowJobsResponse.from_dict(action_workflow_jobs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



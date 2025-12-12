# ActionWorkflowRunsResponse

ActionWorkflowRunsResponse returns ActionWorkflowRuns

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**workflow_runs** | [**List[ActionWorkflowRun]**](ActionWorkflowRun.md) |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.action_workflow_runs_response import ActionWorkflowRunsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActionWorkflowRunsResponse from a JSON string
action_workflow_runs_response_instance = ActionWorkflowRunsResponse.from_json(json)
# print the JSON string representation of the object
print(ActionWorkflowRunsResponse.to_json())

# convert the object into a dict
action_workflow_runs_response_dict = action_workflow_runs_response_instance.to_dict()
# create an instance of ActionWorkflowRunsResponse from a dict
action_workflow_runs_response_from_dict = ActionWorkflowRunsResponse.from_dict(action_workflow_runs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



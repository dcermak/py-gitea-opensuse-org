# ActionWorkflowRun

ActionWorkflowRun represents a WorkflowRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head_sha** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**repository_id** | **int** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.action_workflow_run import ActionWorkflowRun

# TODO update the JSON string below
json = "{}"
# create an instance of ActionWorkflowRun from a JSON string
action_workflow_run_instance = ActionWorkflowRun.from_json(json)
# print the JSON string representation of the object
print(ActionWorkflowRun.to_json())

# convert the object into a dict
action_workflow_run_dict = action_workflow_run_instance.to_dict()
# create an instance of ActionWorkflowRun from a dict
action_workflow_run_from_dict = ActionWorkflowRun.from_dict(action_workflow_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



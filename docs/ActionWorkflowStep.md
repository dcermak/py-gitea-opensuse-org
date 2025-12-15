# ActionWorkflowStep

ActionWorkflowStep represents a step of a WorkflowJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **datetime** |  | [optional] 
**conclusion** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.action_workflow_step import ActionWorkflowStep

# TODO update the JSON string below
json = "{}"
# create an instance of ActionWorkflowStep from a JSON string
action_workflow_step_instance = ActionWorkflowStep.from_json(json)
# print the JSON string representation of the object
print(ActionWorkflowStep.to_json())

# convert the object into a dict
action_workflow_step_dict = action_workflow_step_instance.to_dict()
# create an instance of ActionWorkflowStep from a dict
action_workflow_step_from_dict = ActionWorkflowStep.from_dict(action_workflow_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



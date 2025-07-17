# ActionWorkflowResponse

ActionWorkflowResponse returns a ActionWorkflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**workflows** | [**List[ActionWorkflow]**](ActionWorkflow.md) |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.action_workflow_response import ActionWorkflowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActionWorkflowResponse from a JSON string
action_workflow_response_instance = ActionWorkflowResponse.from_json(json)
# print the JSON string representation of the object
print(ActionWorkflowResponse.to_json())

# convert the object into a dict
action_workflow_response_dict = action_workflow_response_instance.to_dict()
# create an instance of ActionWorkflowResponse from a dict
action_workflow_response_from_dict = ActionWorkflowResponse.from_dict(action_workflow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



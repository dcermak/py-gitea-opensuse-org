# CreateActionWorkflowDispatch

CreateActionWorkflowDispatch represents the payload for triggering a workflow dispatch event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | **Dict[str, str]** |  | [optional] 
**ref** | **str** |  | 

## Example

```python
from py_gitea_opensuse_org.models.create_action_workflow_dispatch import CreateActionWorkflowDispatch

# TODO update the JSON string below
json = "{}"
# create an instance of CreateActionWorkflowDispatch from a JSON string
create_action_workflow_dispatch_instance = CreateActionWorkflowDispatch.from_json(json)
# print the JSON string representation of the object
print(CreateActionWorkflowDispatch.to_json())

# convert the object into a dict
create_action_workflow_dispatch_dict = create_action_workflow_dispatch_instance.to_dict()
# create an instance of CreateActionWorkflowDispatch from a dict
create_action_workflow_dispatch_from_dict = CreateActionWorkflowDispatch.from_dict(create_action_workflow_dispatch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



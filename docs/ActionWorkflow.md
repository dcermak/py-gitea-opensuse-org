# ActionWorkflow

ActionWorkflow represents a ActionWorkflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.action_workflow import ActionWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of ActionWorkflow from a JSON string
action_workflow_instance = ActionWorkflow.from_json(json)
# print the JSON string representation of the object
print(ActionWorkflow.to_json())

# convert the object into a dict
action_workflow_dict = action_workflow_instance.to_dict()
# create an instance of ActionWorkflow from a dict
action_workflow_from_dict = ActionWorkflow.from_dict(action_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



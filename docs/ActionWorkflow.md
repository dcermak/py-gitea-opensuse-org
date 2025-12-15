# ActionWorkflow

ActionWorkflow represents a ActionWorkflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge_url** | **str** | BadgeURL is the URL for the workflow badge | [optional] 
**created_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**html_url** | **str** | HTMLURL is the web URL for viewing the workflow | [optional] 
**id** | **str** | ID is the unique identifier for the workflow | [optional] 
**name** | **str** | Name is the name of the workflow | [optional] 
**path** | **str** | Path is the file path of the workflow | [optional] 
**state** | **str** | State indicates if the workflow is active or disabled | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** | URL is the API URL for this workflow | [optional] 

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



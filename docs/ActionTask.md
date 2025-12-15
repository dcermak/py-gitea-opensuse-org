# ActionTask

ActionTask represents a ActionTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**display_title** | **str** | DisplayTitle is the display title for the workflow run | [optional] 
**event** | **str** | Event is the type of event that triggered the workflow | [optional] 
**head_branch** | **str** | HeadBranch is the branch that triggered the workflow | [optional] 
**head_sha** | **str** | HeadSHA is the commit SHA that triggered the workflow | [optional] 
**id** | **int** | ID is the unique identifier for the action task | [optional] 
**name** | **str** | Name is the name of the workflow | [optional] 
**run_number** | **int** | RunNumber is the sequential number of the workflow run | [optional] 
**run_started_at** | **datetime** |  | [optional] 
**status** | **str** | Status indicates the current status of the workflow run | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** | URL is the API URL for this workflow run | [optional] 
**workflow_id** | **str** | WorkflowID is the identifier of the workflow | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.action_task import ActionTask

# TODO update the JSON string below
json = "{}"
# create an instance of ActionTask from a JSON string
action_task_instance = ActionTask.from_json(json)
# print the JSON string representation of the object
print(ActionTask.to_json())

# convert the object into a dict
action_task_dict = action_task_instance.to_dict()
# create an instance of ActionTask from a dict
action_task_from_dict = ActionTask.from_dict(action_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



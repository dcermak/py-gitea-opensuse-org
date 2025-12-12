# ActionWorkflowJob

ActionWorkflowJob represents a WorkflowJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **datetime** |  | [optional] 
**conclusion** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**head_branch** | **str** |  | [optional] 
**head_sha** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**run_attempt** | **int** |  | [optional] 
**run_id** | **int** |  | [optional] 
**run_url** | **str** |  | [optional] 
**runner_id** | **int** |  | [optional] 
**runner_name** | **str** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**steps** | [**List[ActionWorkflowStep]**](ActionWorkflowStep.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.action_workflow_job import ActionWorkflowJob

# TODO update the JSON string below
json = "{}"
# create an instance of ActionWorkflowJob from a JSON string
action_workflow_job_instance = ActionWorkflowJob.from_json(json)
# print the JSON string representation of the object
print(ActionWorkflowJob.to_json())

# convert the object into a dict
action_workflow_job_dict = action_workflow_job_instance.to_dict()
# create an instance of ActionWorkflowJob from a dict
action_workflow_job_from_dict = ActionWorkflowJob.from_dict(action_workflow_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



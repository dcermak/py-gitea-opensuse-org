# ActionArtifact

ActionArtifact represents a ActionArtifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_download_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**expired** | **bool** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**size_in_bytes** | **int** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 
**workflow_run** | [**ActionWorkflowRun**](ActionWorkflowRun.md) |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.action_artifact import ActionArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of ActionArtifact from a JSON string
action_artifact_instance = ActionArtifact.from_json(json)
# print the JSON string representation of the object
print(ActionArtifact.to_json())

# convert the object into a dict
action_artifact_dict = action_artifact_instance.to_dict()
# create an instance of ActionArtifact from a dict
action_artifact_from_dict = ActionArtifact.from_dict(action_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



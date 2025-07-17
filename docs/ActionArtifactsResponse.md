# ActionArtifactsResponse

ActionArtifactsResponse returns ActionArtifacts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifacts** | [**List[ActionArtifact]**](ActionArtifact.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.action_artifacts_response import ActionArtifactsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActionArtifactsResponse from a JSON string
action_artifacts_response_instance = ActionArtifactsResponse.from_json(json)
# print the JSON string representation of the object
print(ActionArtifactsResponse.to_json())

# convert the object into a dict
action_artifacts_response_dict = action_artifacts_response_instance.to_dict()
# create an instance of ActionArtifactsResponse from a dict
action_artifacts_response_from_dict = ActionArtifactsResponse.from_dict(action_artifacts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



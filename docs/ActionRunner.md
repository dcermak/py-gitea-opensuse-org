# ActionRunner

ActionRunner represents a Runner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**busy** | **bool** |  | [optional] 
**ephemeral** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**labels** | [**List[ActionRunnerLabel]**](ActionRunnerLabel.md) |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.action_runner import ActionRunner

# TODO update the JSON string below
json = "{}"
# create an instance of ActionRunner from a JSON string
action_runner_instance = ActionRunner.from_json(json)
# print the JSON string representation of the object
print(ActionRunner.to_json())

# convert the object into a dict
action_runner_dict = action_runner_instance.to_dict()
# create an instance of ActionRunner from a dict
action_runner_from_dict = ActionRunner.from_dict(action_runner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ActionRunnerLabel

ActionRunnerLabel represents a Runner Label

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.action_runner_label import ActionRunnerLabel

# TODO update the JSON string below
json = "{}"
# create an instance of ActionRunnerLabel from a JSON string
action_runner_label_instance = ActionRunnerLabel.from_json(json)
# print the JSON string representation of the object
print(ActionRunnerLabel.to_json())

# convert the object into a dict
action_runner_label_dict = action_runner_label_instance.to_dict()
# create an instance of ActionRunnerLabel from a dict
action_runner_label_from_dict = ActionRunnerLabel.from_dict(action_runner_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ActionRunnersResponse

ActionRunnersResponse returns Runners

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runners** | [**List[ActionRunner]**](ActionRunner.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.action_runners_response import ActionRunnersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActionRunnersResponse from a JSON string
action_runners_response_instance = ActionRunnersResponse.from_json(json)
# print the JSON string representation of the object
print(ActionRunnersResponse.to_json())

# convert the object into a dict
action_runners_response_dict = action_runners_response_instance.to_dict()
# create an instance of ActionRunnersResponse from a dict
action_runners_response_from_dict = ActionRunnersResponse.from_dict(action_runners_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



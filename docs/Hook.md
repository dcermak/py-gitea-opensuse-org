# Hook

Hook a hook is a web hook when one repository changed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the webhook is active and will be triggered | [optional] 
**authorization_header** | **str** | Authorization header to include in webhook requests | [optional] 
**branch_filter** | **str** | Branch filter pattern to determine which branches trigger the webhook | [optional] 
**config** | **Dict[str, str]** | Configuration settings for the webhook | [optional] 
**created_at** | **datetime** |  | [optional] 
**events** | **List[str]** | List of events that trigger this webhook | [optional] 
**id** | **int** | The unique identifier of the webhook | [optional] 
**type** | **str** | The type of the webhook (e.g., gitea, slack, discord) | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.hook import Hook

# TODO update the JSON string below
json = "{}"
# create an instance of Hook from a JSON string
hook_instance = Hook.from_json(json)
# print the JSON string representation of the object
print(Hook.to_json())

# convert the object into a dict
hook_dict = hook_instance.to_dict()
# create an instance of Hook from a dict
hook_from_dict = Hook.from_dict(hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



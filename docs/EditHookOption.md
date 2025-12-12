# EditHookOption

EditHookOption options when modify one hook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the webhook is active and will be triggered | [optional] 
**authorization_header** | **str** | Authorization header to include in webhook requests | [optional] 
**branch_filter** | **str** | Branch filter pattern to determine which branches trigger the webhook | [optional] 
**config** | **Dict[str, str]** | Configuration settings for the webhook | [optional] 
**events** | **List[str]** | List of events that trigger this webhook | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.edit_hook_option import EditHookOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditHookOption from a JSON string
edit_hook_option_instance = EditHookOption.from_json(json)
# print the JSON string representation of the object
print(EditHookOption.to_json())

# convert the object into a dict
edit_hook_option_dict = edit_hook_option_instance.to_dict()
# create an instance of EditHookOption from a dict
edit_hook_option_from_dict = EditHookOption.from_dict(edit_hook_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



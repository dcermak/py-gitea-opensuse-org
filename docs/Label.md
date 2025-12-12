# Label

Label a label to an issue or a pr

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**description** | **str** | Description provides additional context about the label&#39;s purpose | [optional] 
**exclusive** | **bool** |  | [optional] 
**id** | **int** | ID is the unique identifier for the label | [optional] 
**is_archived** | **bool** |  | [optional] 
**name** | **str** | Name is the display name of the label | [optional] 
**url** | **str** | URL is the API endpoint for accessing this label | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.label import Label

# TODO update the JSON string below
json = "{}"
# create an instance of Label from a JSON string
label_instance = Label.from_json(json)
# print the JSON string representation of the object
print(Label.to_json())

# convert the object into a dict
label_dict = label_instance.to_dict()
# create an instance of Label from a dict
label_from_dict = Label.from_dict(label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# LabelTemplate

LabelTemplate info of a Label template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**description** | **str** | Description provides additional context about the label template&#39;s purpose | [optional] 
**exclusive** | **bool** |  | [optional] 
**name** | **str** | Name is the display name of the label template | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.label_template import LabelTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of LabelTemplate from a JSON string
label_template_instance = LabelTemplate.from_json(json)
# print the JSON string representation of the object
print(LabelTemplate.to_json())

# convert the object into a dict
label_template_dict = label_template_instance.to_dict()
# create an instance of LabelTemplate from a dict
label_template_from_dict = LabelTemplate.from_dict(label_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



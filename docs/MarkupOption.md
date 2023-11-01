# MarkupOption

MarkupOption markup options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | Context to render  in: body | [optional] 
**file_path** | **str** | File path for detecting extension in file mode  in: body | [optional] 
**mode** | **str** | Mode to render (comment, gfm, markdown, file)  in: body | [optional] 
**text** | **str** | Text markup to render  in: body | [optional] 
**wiki** | **bool** | Is it a wiki page ?  in: body | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.markup_option import MarkupOption

# TODO update the JSON string below
json = "{}"
# create an instance of MarkupOption from a JSON string
markup_option_instance = MarkupOption.from_json(json)
# print the JSON string representation of the object
print MarkupOption.to_json()

# convert the object into a dict
markup_option_dict = markup_option_instance.to_dict()
# create an instance of MarkupOption from a dict
markup_option_form_dict = markup_option.from_dict(markup_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



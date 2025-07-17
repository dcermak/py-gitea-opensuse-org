# MarkupOption

MarkupOption markup options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | URL path for rendering issue, media and file links Expected format: /subpath/{user}/{repo}/src/{branch, commit, tag}/{identifier/path}/{file/dir}  in: body | [optional] 
**file_path** | **str** | File path for detecting extension in file mode  in: body | [optional] 
**mode** | **str** | Mode to render (markdown, comment, wiki, file)  in: body | [optional] 
**text** | **str** | Text markup to render  in: body | [optional] 
**wiki** | **bool** | Is it a wiki page? (use mode&#x3D;wiki instead)  Deprecated: true in: body | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.markup_option import MarkupOption

# TODO update the JSON string below
json = "{}"
# create an instance of MarkupOption from a JSON string
markup_option_instance = MarkupOption.from_json(json)
# print the JSON string representation of the object
print(MarkupOption.to_json())

# convert the object into a dict
markup_option_dict = markup_option_instance.to_dict()
# create an instance of MarkupOption from a dict
markup_option_from_dict = MarkupOption.from_dict(markup_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



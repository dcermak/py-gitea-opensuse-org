# MarkdownOption

MarkdownOption markdown options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | URL path for rendering issue, media and file links Expected format: /subpath/{user}/{repo}/src/{branch, commit, tag}/{identifier/path}/{file/dir}  in: body | [optional] 
**mode** | **str** | Mode to render (markdown, comment, wiki, file)  in: body | [optional] 
**text** | **str** | Text markdown to render  in: body | [optional] 
**wiki** | **bool** | Is it a wiki page? (use mode&#x3D;wiki instead)  Deprecated: true in: body | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.markdown_option import MarkdownOption

# TODO update the JSON string below
json = "{}"
# create an instance of MarkdownOption from a JSON string
markdown_option_instance = MarkdownOption.from_json(json)
# print the JSON string representation of the object
print(MarkdownOption.to_json())

# convert the object into a dict
markdown_option_dict = markdown_option_instance.to_dict()
# create an instance of MarkdownOption from a dict
markdown_option_from_dict = MarkdownOption.from_dict(markdown_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



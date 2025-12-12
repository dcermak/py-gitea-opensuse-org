# FileLinksResponse

FileLinksResponse contains the links for a repo's file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git** | **str** | GitURL is the Git API URL for this file | [optional] 
**html** | **str** | HTMLURL is the web URL for this file | [optional] 
**var_self** | **str** | Self is the API URL for this file | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.file_links_response import FileLinksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileLinksResponse from a JSON string
file_links_response_instance = FileLinksResponse.from_json(json)
# print the JSON string representation of the object
print(FileLinksResponse.to_json())

# convert the object into a dict
file_links_response_dict = file_links_response_instance.to_dict()
# create an instance of FileLinksResponse from a dict
file_links_response_from_dict = FileLinksResponse.from_dict(file_links_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



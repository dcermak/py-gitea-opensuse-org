# ContentsExtResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dir_contents** | [**List[ContentsResponse]**](ContentsResponse.md) | DirContents contains directory listing when the path represents a directory | [optional] 
**file_contents** | [**ContentsResponse**](ContentsResponse.md) |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.contents_ext_response import ContentsExtResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentsExtResponse from a JSON string
contents_ext_response_instance = ContentsExtResponse.from_json(json)
# print the JSON string representation of the object
print(ContentsExtResponse.to_json())

# convert the object into a dict
contents_ext_response_dict = contents_ext_response_instance.to_dict()
# create an instance of ContentsExtResponse from a dict
contents_ext_response_from_dict = ContentsExtResponse.from_dict(contents_ext_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



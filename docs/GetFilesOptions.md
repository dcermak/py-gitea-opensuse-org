# GetFilesOptions

GetFilesOptions options for retrieving metadate and content of multiple files

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **List[str]** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.get_files_options import GetFilesOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetFilesOptions from a JSON string
get_files_options_instance = GetFilesOptions.from_json(json)
# print the JSON string representation of the object
print(GetFilesOptions.to_json())

# convert the object into a dict
get_files_options_dict = get_files_options_instance.to_dict()
# create an instance of GetFilesOptions from a dict
get_files_options_from_dict = GetFilesOptions.from_dict(get_files_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GeneralAPISettings

GeneralAPISettings contains global api settings exposed by it

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_git_trees_per_page** | **int** | DefaultGitTreesPerPage is the default number of Git tree items per page | [optional] 
**default_max_blob_size** | **int** | DefaultMaxBlobSize is the default maximum blob size for API responses | [optional] 
**default_max_response_size** | **int** | DefaultMaxResponseSize is the default maximum response size | [optional] 
**default_paging_num** | **int** | DefaultPagingNum is the default number of items per page | [optional] 
**max_response_items** | **int** | MaxResponseItems is the maximum number of items returned in API responses | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.general_api_settings import GeneralAPISettings

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralAPISettings from a JSON string
general_api_settings_instance = GeneralAPISettings.from_json(json)
# print the JSON string representation of the object
print(GeneralAPISettings.to_json())

# convert the object into a dict
general_api_settings_dict = general_api_settings_instance.to_dict()
# create an instance of GeneralAPISettings from a dict
general_api_settings_from_dict = GeneralAPISettings.from_dict(general_api_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



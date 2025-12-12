# ChangedFile

ChangedFile store information about files affected by the pull request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additions** | **int** | The number of lines added to the file | [optional] 
**changes** | **int** | The total number of changes to the file | [optional] 
**contents_url** | **str** | The API URL to get the file contents | [optional] 
**deletions** | **int** | The number of lines deleted from the file | [optional] 
**filename** | **str** | The name of the changed file | [optional] 
**html_url** | **str** | The HTML URL to view the file changes | [optional] 
**previous_filename** | **str** | The previous filename if the file was renamed | [optional] 
**raw_url** | **str** | The raw URL to download the file | [optional] 
**status** | **str** | The status of the file change (added, modified, deleted, etc.) | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.changed_file import ChangedFile

# TODO update the JSON string below
json = "{}"
# create an instance of ChangedFile from a JSON string
changed_file_instance = ChangedFile.from_json(json)
# print the JSON string representation of the object
print(ChangedFile.to_json())

# convert the object into a dict
changed_file_dict = changed_file_instance.to_dict()
# create an instance of ChangedFile from a dict
changed_file_from_dict = ChangedFile.from_dict(changed_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



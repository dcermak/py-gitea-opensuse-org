# SearchResults

SearchResults results of a successful search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Repository]**](Repository.md) | Data contains the repository search results | [optional] 
**ok** | **bool** | OK indicates if the search was successful | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.search_results import SearchResults

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResults from a JSON string
search_results_instance = SearchResults.from_json(json)
# print the JSON string representation of the object
print(SearchResults.to_json())

# convert the object into a dict
search_results_dict = search_results_instance.to_dict()
# create an instance of SearchResults from a dict
search_results_from_dict = SearchResults.from_dict(search_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



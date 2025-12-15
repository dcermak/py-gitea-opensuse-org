# WikiPageMetaData

WikiPageMetaData wiki page meta information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html_url** | **str** | The HTML URL to view the wiki page | [optional] 
**last_commit** | [**WikiCommit**](WikiCommit.md) |  | [optional] 
**sub_url** | **str** | The sub URL path for the wiki page | [optional] 
**title** | **str** | The title of the wiki page | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.wiki_page_meta_data import WikiPageMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of WikiPageMetaData from a JSON string
wiki_page_meta_data_instance = WikiPageMetaData.from_json(json)
# print the JSON string representation of the object
print(WikiPageMetaData.to_json())

# convert the object into a dict
wiki_page_meta_data_dict = wiki_page_meta_data_instance.to_dict()
# create an instance of WikiPageMetaData from a dict
wiki_page_meta_data_from_dict = WikiPageMetaData.from_dict(wiki_page_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



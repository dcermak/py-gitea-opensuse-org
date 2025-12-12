# WikiPage

WikiPage a wiki page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_count** | **int** | The number of commits that modified this page | [optional] 
**content_base64** | **str** | Page content, base64 encoded | [optional] 
**footer** | **str** | The footer content for the wiki page | [optional] 
**html_url** | **str** | The HTML URL to view the wiki page | [optional] 
**last_commit** | [**WikiCommit**](WikiCommit.md) |  | [optional] 
**sidebar** | **str** | The sidebar content for the wiki page | [optional] 
**sub_url** | **str** | The sub URL path for the wiki page | [optional] 
**title** | **str** | The title of the wiki page | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.wiki_page import WikiPage

# TODO update the JSON string below
json = "{}"
# create an instance of WikiPage from a JSON string
wiki_page_instance = WikiPage.from_json(json)
# print the JSON string representation of the object
print(WikiPage.to_json())

# convert the object into a dict
wiki_page_dict = wiki_page_instance.to_dict()
# create an instance of WikiPage from a dict
wiki_page_from_dict = WikiPage.from_dict(wiki_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



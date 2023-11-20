# Tag

Tag represents a repository tag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | [**CommitMeta**](CommitMeta.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**tarball_url** | **str** |  | [optional] 
**zipball_url** | **str** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.tag import Tag

# TODO update the JSON string below
json = "{}"
# create an instance of Tag from a JSON string
tag_instance = Tag.from_json(json)
# print the JSON string representation of the object
print Tag.to_json()

# convert the object into a dict
tag_dict = tag_instance.to_dict()
# create an instance of Tag from a dict
tag_form_dict = tag.from_dict(tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



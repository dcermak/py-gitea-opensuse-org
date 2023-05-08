# Attachment

Attachment a generic attachment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser_download_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**download_count** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.attachment import Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of Attachment from a JSON string
attachment_instance = Attachment.from_json(json)
# print the JSON string representation of the object
print Attachment.to_json()

# convert the object into a dict
attachment_dict = attachment_instance.to_dict()
# create an instance of Attachment from a dict
attachment_form_dict = attachment.from_dict(attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Attachment

Attachment a generic attachment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser_download_url** | **str** | DownloadURL is the URL to download the attachment | [optional] 
**created_at** | **datetime** |  | [optional] 
**download_count** | **int** | DownloadCount is the number of times the attachment has been downloaded | [optional] 
**id** | **int** | ID is the unique identifier for the attachment | [optional] 
**name** | **str** | Name is the filename of the attachment | [optional] 
**size** | **int** | Size is the file size in bytes | [optional] 
**uuid** | **str** | UUID is the unique identifier for the attachment file | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.attachment import Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of Attachment from a JSON string
attachment_instance = Attachment.from_json(json)
# print the JSON string representation of the object
print(Attachment.to_json())

# convert the object into a dict
attachment_dict = attachment_instance.to_dict()
# create an instance of Attachment from a dict
attachment_from_dict = Attachment.from_dict(attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



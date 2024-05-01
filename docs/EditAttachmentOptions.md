# EditAttachmentOptions

EditAttachmentOptions options for editing attachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.edit_attachment_options import EditAttachmentOptions

# TODO update the JSON string below
json = "{}"
# create an instance of EditAttachmentOptions from a JSON string
edit_attachment_options_instance = EditAttachmentOptions.from_json(json)
# print the JSON string representation of the object
print(EditAttachmentOptions.to_json())

# convert the object into a dict
edit_attachment_options_dict = edit_attachment_options_instance.to_dict()
# create an instance of EditAttachmentOptions from a dict
edit_attachment_options_from_dict = EditAttachmentOptions.from_dict(edit_attachment_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



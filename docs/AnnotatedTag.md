# AnnotatedTag

AnnotatedTag represents an annotated tag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The message associated with the annotated tag | [optional] 
**object** | [**AnnotatedTagObject**](AnnotatedTagObject.md) |  | [optional] 
**sha** | **str** | The SHA hash of the annotated tag | [optional] 
**tag** | **str** | The name of the annotated tag | [optional] 
**tagger** | [**CommitUser**](CommitUser.md) |  | [optional] 
**url** | **str** | The URL to access the annotated tag | [optional] 
**verification** | [**PayloadCommitVerification**](PayloadCommitVerification.md) |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.annotated_tag import AnnotatedTag

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotatedTag from a JSON string
annotated_tag_instance = AnnotatedTag.from_json(json)
# print the JSON string representation of the object
print(AnnotatedTag.to_json())

# convert the object into a dict
annotated_tag_dict = annotated_tag_instance.to_dict()
# create an instance of AnnotatedTag from a dict
annotated_tag_from_dict = AnnotatedTag.from_dict(annotated_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



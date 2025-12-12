# Comment

Comment represents a comment on a commit or issue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[Attachment]**](Attachment.md) | Attachments contains files attached to the comment | [optional] 
**body** | **str** | Body contains the comment text content | [optional] 
**created_at** | **datetime** |  | [optional] 
**html_url** | **str** | HTMLURL is the web URL for viewing the comment | [optional] 
**id** | **int** | ID is the unique identifier for the comment | [optional] 
**issue_url** | **str** | IssueURL is the API URL for the issue | [optional] 
**original_author** | **str** | OriginalAuthor is the original author name (for imported comments) | [optional] 
**original_author_id** | **int** | OriginalAuthorID is the original author ID (for imported comments) | [optional] 
**pull_request_url** | **str** | PRURL is the API URL for the pull request (if applicable) | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.comment import Comment

# TODO update the JSON string below
json = "{}"
# create an instance of Comment from a JSON string
comment_instance = Comment.from_json(json)
# print the JSON string representation of the object
print(Comment.to_json())

# convert the object into a dict
comment_dict = comment_instance.to_dict()
# create an instance of Comment from a dict
comment_from_dict = Comment.from_dict(comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



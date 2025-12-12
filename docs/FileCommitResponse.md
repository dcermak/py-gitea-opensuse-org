# FileCommitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**CommitUser**](CommitUser.md) |  | [optional] 
**committer** | [**CommitUser**](CommitUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**html_url** | **str** | HTMLURL is the web URL for viewing this commit | [optional] 
**message** | **str** | Message is the commit message | [optional] 
**parents** | [**List[CommitMeta]**](CommitMeta.md) | Parents contains parent commit metadata | [optional] 
**sha** | **str** | SHA is the commit SHA hash | [optional] 
**tree** | [**CommitMeta**](CommitMeta.md) |  | [optional] 
**url** | **str** | URL is the API URL for the commit | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.file_commit_response import FileCommitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileCommitResponse from a JSON string
file_commit_response_instance = FileCommitResponse.from_json(json)
# print the JSON string representation of the object
print(FileCommitResponse.to_json())

# convert the object into a dict
file_commit_response_dict = file_commit_response_instance.to_dict()
# create an instance of FileCommitResponse from a dict
file_commit_response_from_dict = FileCommitResponse.from_dict(file_commit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GitBlobResponse

GitBlobResponse represents a git blob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The content of the git blob (may be base64 encoded) | [optional] 
**encoding** | **str** | The encoding used for the content (e.g., \&quot;base64\&quot;) | [optional] 
**lfs_oid** | **str** | The LFS object ID if this blob is stored in LFS | [optional] 
**lfs_size** | **int** | The size of the LFS object if this blob is stored in LFS | [optional] 
**sha** | **str** | The SHA hash of the git blob | [optional] 
**size** | **int** | The size of the git blob in bytes | [optional] 
**url** | **str** | The URL to access this git blob | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.git_blob_response import GitBlobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitBlobResponse from a JSON string
git_blob_response_instance = GitBlobResponse.from_json(json)
# print the JSON string representation of the object
print(GitBlobResponse.to_json())

# convert the object into a dict
git_blob_response_dict = git_blob_response_instance.to_dict()
# create an instance of GitBlobResponse from a dict
git_blob_response_from_dict = GitBlobResponse.from_dict(git_blob_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



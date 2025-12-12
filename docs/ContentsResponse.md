# ContentsResponse

ContentsResponse contains information about a repo's entry's (dir, file, symlink, submodule) metadata and content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**FileLinksResponse**](FileLinksResponse.md) |  | [optional] 
**content** | **str** | &#x60;content&#x60; is populated when &#x60;type&#x60; is &#x60;file&#x60;, otherwise null | [optional] 
**download_url** | **str** | DownloadURL is the direct download URL for this file | [optional] 
**encoding** | **str** | &#x60;encoding&#x60; is populated when &#x60;type&#x60; is &#x60;file&#x60;, otherwise null | [optional] 
**git_url** | **str** | GitURL is the Git API URL for this blob or tree | [optional] 
**html_url** | **str** | HTMLURL is the web URL for this file or directory | [optional] 
**last_author_date** | **datetime** |  | [optional] 
**last_commit_message** | **str** | LastCommitMessage is the message of the last commit that affected this file | [optional] 
**last_commit_sha** | **str** | LastCommitSHA is the SHA of the last commit that affected this file | [optional] 
**last_committer_date** | **datetime** |  | [optional] 
**lfs_oid** | **str** | LfsOid is the Git LFS object ID if this file is stored in LFS | [optional] 
**lfs_size** | **int** | LfsSize is the file size if this file is stored in LFS | [optional] 
**name** | **str** | Name is the file or directory name | [optional] 
**path** | **str** | Path is the full path to the file or directory | [optional] 
**sha** | **str** | SHA is the Git blob or tree SHA | [optional] 
**size** | **int** | Size is the file size in bytes | [optional] 
**submodule_git_url** | **str** | &#x60;submodule_git_url&#x60; is populated when &#x60;type&#x60; is &#x60;submodule&#x60;, otherwise null | [optional] 
**target** | **str** | &#x60;target&#x60; is populated when &#x60;type&#x60; is &#x60;symlink&#x60;, otherwise null | [optional] 
**type** | **str** | &#x60;type&#x60; will be &#x60;file&#x60;, &#x60;dir&#x60;, &#x60;symlink&#x60;, or &#x60;submodule&#x60; | [optional] 
**url** | **str** | URL is the API URL for this file or directory | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.contents_response import ContentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentsResponse from a JSON string
contents_response_instance = ContentsResponse.from_json(json)
# print the JSON string representation of the object
print(ContentsResponse.to_json())

# convert the object into a dict
contents_response_dict = contents_response_instance.to_dict()
# create an instance of ContentsResponse from a dict
contents_response_from_dict = ContentsResponse.from_dict(contents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



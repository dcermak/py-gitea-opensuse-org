# Commit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**User**](User.md) |  | [optional] 
**commit** | [**RepoCommit**](RepoCommit.md) |  | [optional] 
**committer** | [**User**](User.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**files** | [**List[CommitAffectedFiles]**](CommitAffectedFiles.md) | Files contains information about files affected by the commit | [optional] 
**html_url** | **str** | HTMLURL is the web URL for viewing the commit | [optional] 
**parents** | [**List[CommitMeta]**](CommitMeta.md) | Parents contains the parent commit information | [optional] 
**sha** | **str** | SHA is the commit SHA hash | [optional] 
**stats** | [**CommitStats**](CommitStats.md) |  | [optional] 
**url** | **str** | URL is the API URL for the commit | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.commit import Commit

# TODO update the JSON string below
json = "{}"
# create an instance of Commit from a JSON string
commit_instance = Commit.from_json(json)
# print the JSON string representation of the object
print(Commit.to_json())

# convert the object into a dict
commit_dict = commit_instance.to_dict()
# create an instance of Commit from a dict
commit_from_dict = Commit.from_dict(commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



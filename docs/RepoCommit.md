# RepoCommit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**CommitUser**](CommitUser.md) |  | [optional] 
**committer** | [**CommitUser**](CommitUser.md) |  | [optional] 
**message** | **str** |  | [optional] 
**tree** | [**CommitMeta**](CommitMeta.md) |  | [optional] 
**url** | **str** |  | [optional] 
**verification** | [**PayloadCommitVerification**](PayloadCommitVerification.md) |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.repo_commit import RepoCommit

# TODO update the JSON string below
json = "{}"
# create an instance of RepoCommit from a JSON string
repo_commit_instance = RepoCommit.from_json(json)
# print the JSON string representation of the object
print RepoCommit.to_json()

# convert the object into a dict
repo_commit_dict = repo_commit_instance.to_dict()
# create an instance of RepoCommit from a dict
repo_commit_form_dict = repo_commit.from_dict(repo_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



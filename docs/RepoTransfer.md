# RepoTransfer

RepoTransfer represents a pending repo transfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doer** | [**User**](User.md) |  | [optional] 
**recipient** | [**User**](User.md) |  | [optional] 
**teams** | [**List[Team]**](Team.md) |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.repo_transfer import RepoTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of RepoTransfer from a JSON string
repo_transfer_instance = RepoTransfer.from_json(json)
# print the JSON string representation of the object
print RepoTransfer.to_json()

# convert the object into a dict
repo_transfer_dict = repo_transfer_instance.to_dict()
# create an instance of RepoTransfer from a dict
repo_transfer_form_dict = repo_transfer.from_dict(repo_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



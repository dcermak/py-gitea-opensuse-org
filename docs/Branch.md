# Branch

Branch represents a repository branch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | [**PayloadCommit**](PayloadCommit.md) |  | [optional] 
**effective_branch_protection_name** | **str** | EffectiveBranchProtectionName is the name of the effective branch protection rule | [optional] 
**enable_status_check** | **bool** | EnableStatusCheck indicates if status checks are enabled | [optional] 
**name** | **str** | Name is the branch name | [optional] 
**protected** | **bool** | Protected indicates if the branch is protected | [optional] 
**required_approvals** | **int** | RequiredApprovals is the number of required approvals for pull requests | [optional] 
**status_check_contexts** | **List[str]** | StatusCheckContexts contains the list of required status check contexts | [optional] 
**user_can_merge** | **bool** | UserCanMerge indicates if the current user can merge to this branch | [optional] 
**user_can_push** | **bool** | UserCanPush indicates if the current user can push to this branch | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.branch import Branch

# TODO update the JSON string below
json = "{}"
# create an instance of Branch from a JSON string
branch_instance = Branch.from_json(json)
# print the JSON string representation of the object
print(Branch.to_json())

# convert the object into a dict
branch_dict = branch_instance.to_dict()
# create an instance of Branch from a dict
branch_from_dict = Branch.from_dict(branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



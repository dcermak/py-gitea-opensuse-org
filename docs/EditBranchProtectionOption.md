# EditBranchProtectionOption

EditBranchProtectionOption options for editing a branch protection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvals_whitelist_teams** | **List[str]** |  | [optional] 
**approvals_whitelist_username** | **List[str]** |  | [optional] 
**block_admin_merge_override** | **bool** |  | [optional] 
**block_on_official_review_requests** | **bool** |  | [optional] 
**block_on_outdated_branch** | **bool** |  | [optional] 
**block_on_rejected_reviews** | **bool** |  | [optional] 
**dismiss_stale_approvals** | **bool** |  | [optional] 
**enable_approvals_whitelist** | **bool** |  | [optional] 
**enable_force_push** | **bool** |  | [optional] 
**enable_force_push_allowlist** | **bool** |  | [optional] 
**enable_merge_whitelist** | **bool** |  | [optional] 
**enable_push** | **bool** |  | [optional] 
**enable_push_whitelist** | **bool** |  | [optional] 
**enable_status_check** | **bool** |  | [optional] 
**force_push_allowlist_deploy_keys** | **bool** |  | [optional] 
**force_push_allowlist_teams** | **List[str]** |  | [optional] 
**force_push_allowlist_usernames** | **List[str]** |  | [optional] 
**ignore_stale_approvals** | **bool** |  | [optional] 
**merge_whitelist_teams** | **List[str]** |  | [optional] 
**merge_whitelist_usernames** | **List[str]** |  | [optional] 
**priority** | **int** |  | [optional] 
**protected_file_patterns** | **str** |  | [optional] 
**push_whitelist_deploy_keys** | **bool** |  | [optional] 
**push_whitelist_teams** | **List[str]** |  | [optional] 
**push_whitelist_usernames** | **List[str]** |  | [optional] 
**require_signed_commits** | **bool** |  | [optional] 
**required_approvals** | **int** |  | [optional] 
**status_check_contexts** | **List[str]** |  | [optional] 
**unprotected_file_patterns** | **str** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.edit_branch_protection_option import EditBranchProtectionOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditBranchProtectionOption from a JSON string
edit_branch_protection_option_instance = EditBranchProtectionOption.from_json(json)
# print the JSON string representation of the object
print(EditBranchProtectionOption.to_json())

# convert the object into a dict
edit_branch_protection_option_dict = edit_branch_protection_option_instance.to_dict()
# create an instance of EditBranchProtectionOption from a dict
edit_branch_protection_option_from_dict = EditBranchProtectionOption.from_dict(edit_branch_protection_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



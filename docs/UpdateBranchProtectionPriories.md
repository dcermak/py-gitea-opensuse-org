# UpdateBranchProtectionPriories

UpdateBranchProtectionPriories a list to update the branch protection rule priorities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.update_branch_protection_priories import UpdateBranchProtectionPriories

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBranchProtectionPriories from a JSON string
update_branch_protection_priories_instance = UpdateBranchProtectionPriories.from_json(json)
# print the JSON string representation of the object
print(UpdateBranchProtectionPriories.to_json())

# convert the object into a dict
update_branch_protection_priories_dict = update_branch_protection_priories_instance.to_dict()
# create an instance of UpdateBranchProtectionPriories from a dict
update_branch_protection_priories_from_dict = UpdateBranchProtectionPriories.from_dict(update_branch_protection_priories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



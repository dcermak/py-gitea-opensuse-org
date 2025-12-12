# OrganizationPermissions

OrganizationPermissions list different users permissions on an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_create_repository** | **bool** | Whether the user can create repositories in the organization | [optional] 
**can_read** | **bool** | Whether the user can read the organization | [optional] 
**can_write** | **bool** | Whether the user can write to the organization | [optional] 
**is_admin** | **bool** | Whether the user is an admin of the organization | [optional] 
**is_owner** | **bool** | Whether the user is an owner of the organization | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.organization_permissions import OrganizationPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationPermissions from a JSON string
organization_permissions_instance = OrganizationPermissions.from_json(json)
# print the JSON string representation of the object
print(OrganizationPermissions.to_json())

# convert the object into a dict
organization_permissions_dict = organization_permissions_instance.to_dict()
# create an instance of OrganizationPermissions from a dict
organization_permissions_from_dict = OrganizationPermissions.from_dict(organization_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



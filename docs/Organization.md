# Organization

Organization represents an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** | The URL of the organization&#39;s avatar | [optional] 
**description** | **str** | The description of the organization | [optional] 
**email** | **str** | The email address of the organization | [optional] 
**full_name** | **str** | The full display name of the organization | [optional] 
**id** | **int** | The unique identifier of the organization | [optional] 
**location** | **str** | The location of the organization | [optional] 
**name** | **str** | The name of the organization | [optional] 
**repo_admin_change_team_access** | **bool** | Whether repository administrators can change team access | [optional] 
**username** | **str** | username of the organization deprecated | [optional] 
**visibility** | **str** | The visibility level of the organization (public, limited, private) | [optional] 
**website** | **str** | The website URL of the organization | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print(Organization.to_json())

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_from_dict = Organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



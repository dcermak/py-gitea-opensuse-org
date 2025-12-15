# CreateOrgOption

CreateOrgOption options for creating an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the organization | [optional] 
**email** | **str** | The email address of the organization | [optional] 
**full_name** | **str** | The full display name of the organization | [optional] 
**location** | **str** | The location of the organization | [optional] 
**repo_admin_change_team_access** | **bool** | Whether repository administrators can change team access | [optional] 
**username** | **str** | username of the organization | 
**visibility** | **str** | possible values are &#x60;public&#x60; (default), &#x60;limited&#x60; or &#x60;private&#x60; | [optional] 
**website** | **str** | The website URL of the organization | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.create_org_option import CreateOrgOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrgOption from a JSON string
create_org_option_instance = CreateOrgOption.from_json(json)
# print the JSON string representation of the object
print(CreateOrgOption.to_json())

# convert the object into a dict
create_org_option_dict = create_org_option_instance.to_dict()
# create an instance of CreateOrgOption from a dict
create_org_option_from_dict = CreateOrgOption.from_dict(create_org_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



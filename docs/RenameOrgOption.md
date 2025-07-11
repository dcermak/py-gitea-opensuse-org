# RenameOrgOption

RenameOrgOption options when renaming an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_name** | **str** | New username for this org. This name cannot be in use yet by any other user. | 

## Example

```python
from py_gitea_opensuse_org.models.rename_org_option import RenameOrgOption

# TODO update the JSON string below
json = "{}"
# create an instance of RenameOrgOption from a JSON string
rename_org_option_instance = RenameOrgOption.from_json(json)
# print the JSON string representation of the object
print(RenameOrgOption.to_json())

# convert the object into a dict
rename_org_option_dict = rename_org_option_instance.to_dict()
# create an instance of RenameOrgOption from a dict
rename_org_option_from_dict = RenameOrgOption.from_dict(rename_org_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



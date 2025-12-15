# EditUserOption

EditUserOption edit user options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the user account is active | [optional] 
**admin** | **bool** | Whether the user has administrator privileges | [optional] 
**allow_create_organization** | **bool** | Whether the user can create organizations | [optional] 
**allow_git_hook** | **bool** | Whether the user can use Git hooks | [optional] 
**allow_import_local** | **bool** | Whether the user can import local repositories | [optional] 
**description** | **str** | The user&#39;s personal description or bio | [optional] 
**email** | **str** |  | [optional] 
**full_name** | **str** | The full display name of the user | [optional] 
**location** | **str** | The user&#39;s location or address | [optional] 
**login_name** | **str** | identifier of the user, provided by the external authenticator (if configured) | [default to 'empty']
**max_repo_creation** | **int** | Maximum number of repositories the user can create | [optional] 
**must_change_password** | **bool** | Whether the user must change password on next login | [optional] 
**password** | **str** | The plain text password for the user | [optional] 
**prohibit_login** | **bool** | Whether the user is prohibited from logging in | [optional] 
**restricted** | **bool** | Whether the user has restricted access privileges | [optional] 
**source_id** | **int** |  | 
**visibility** | **str** | User visibility level: public, limited, or private | [optional] 
**website** | **str** | The user&#39;s personal website URL | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.edit_user_option import EditUserOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditUserOption from a JSON string
edit_user_option_instance = EditUserOption.from_json(json)
# print the JSON string representation of the object
print(EditUserOption.to_json())

# convert the object into a dict
edit_user_option_dict = edit_user_option_instance.to_dict()
# create an instance of EditUserOption from a dict
edit_user_option_from_dict = EditUserOption.from_dict(edit_user_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



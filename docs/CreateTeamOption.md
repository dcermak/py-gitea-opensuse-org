# CreateTeamOption

CreateTeamOption options for creating a team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_create_org_repo** | **bool** | Whether the team can create repositories in the organization | [optional] 
**description** | **str** | The description of the team | [optional] 
**includes_all_repositories** | **bool** | Whether the team has access to all repositories in the organization | [optional] 
**name** | **str** |  | 
**permission** | **str** |  | [optional] 
**units** | **List[str]** |  | [optional] 
**units_map** | **Dict[str, str]** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.create_team_option import CreateTeamOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeamOption from a JSON string
create_team_option_instance = CreateTeamOption.from_json(json)
# print the JSON string representation of the object
print(CreateTeamOption.to_json())

# convert the object into a dict
create_team_option_dict = create_team_option_instance.to_dict()
# create an instance of CreateTeamOption from a dict
create_team_option_from_dict = CreateTeamOption.from_dict(create_team_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



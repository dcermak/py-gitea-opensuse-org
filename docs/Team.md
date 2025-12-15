# Team

Team represents a team in an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_create_org_repo** | **bool** | Whether the team can create repositories in the organization | [optional] 
**description** | **str** | The description of the team | [optional] 
**id** | **int** | The unique identifier of the team | [optional] 
**includes_all_repositories** | **bool** | Whether the team has access to all repositories in the organization | [optional] 
**name** | **str** | The name of the team | [optional] 
**organization** | [**Organization**](Organization.md) |  | [optional] 
**permission** | **str** |  | [optional] 
**units** | **List[str]** |  | [optional] 
**units_map** | **Dict[str, str]** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print(Team.to_json())

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_from_dict = Team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



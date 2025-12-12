# Milestone

Milestone milestone is a collection of issues on one repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_at** | **datetime** |  | [optional] 
**closed_issues** | **int** | ClosedIssues is the number of closed issues in this milestone | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** | Description provides details about the milestone | [optional] 
**due_on** | **datetime** |  | [optional] 
**id** | **int** | ID is the unique identifier for the milestone | [optional] 
**open_issues** | **int** | OpenIssues is the number of open issues in this milestone | [optional] 
**state** | **str** | StateType issue state type | [optional] 
**title** | **str** | Title is the title of the milestone | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.milestone import Milestone

# TODO update the JSON string below
json = "{}"
# create an instance of Milestone from a JSON string
milestone_instance = Milestone.from_json(json)
# print the JSON string representation of the object
print(Milestone.to_json())

# convert the object into a dict
milestone_dict = milestone_instance.to_dict()
# create an instance of Milestone from a dict
milestone_from_dict = Milestone.from_dict(milestone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



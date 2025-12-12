# EditMilestoneOption

EditMilestoneOption options for editing a milestone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description provides updated details about the milestone | [optional] 
**due_on** | **datetime** | Deadline is the updated due date for the milestone | [optional] 
**state** | **str** | State indicates the updated state of the milestone | [optional] 
**title** | **str** | Title is the updated title of the milestone | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.edit_milestone_option import EditMilestoneOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditMilestoneOption from a JSON string
edit_milestone_option_instance = EditMilestoneOption.from_json(json)
# print the JSON string representation of the object
print(EditMilestoneOption.to_json())

# convert the object into a dict
edit_milestone_option_dict = edit_milestone_option_instance.to_dict()
# create an instance of EditMilestoneOption from a dict
edit_milestone_option_from_dict = EditMilestoneOption.from_dict(edit_milestone_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



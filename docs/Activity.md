# Activity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**act_user** | [**User**](User.md) |  | [optional] 
**act_user_id** | **int** | The ID of the user who performed the action | [optional] 
**comment** | [**Comment**](Comment.md) |  | [optional] 
**comment_id** | **int** | The ID of the comment associated with the activity (if applicable) | [optional] 
**content** | **str** | Additional content or details about the activity | [optional] 
**created** | **datetime** | The date and time when the activity occurred | [optional] 
**id** | **int** | The unique identifier of the activity | [optional] 
**is_private** | **bool** | Whether this activity is from a private repository | [optional] 
**op_type** | **str** | the type of action | [optional] 
**ref_name** | **str** | The name of the git reference (branch/tag) associated with the activity | [optional] 
**repo** | [**Repository**](Repository.md) |  | [optional] 
**repo_id** | **int** | The ID of the repository associated with the activity | [optional] 
**user_id** | **int** | The ID of the user who receives/sees this activity | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.activity import Activity

# TODO update the JSON string below
json = "{}"
# create an instance of Activity from a JSON string
activity_instance = Activity.from_json(json)
# print the JSON string representation of the object
print(Activity.to_json())

# convert the object into a dict
activity_dict = activity_instance.to_dict()
# create an instance of Activity from a dict
activity_from_dict = Activity.from_dict(activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



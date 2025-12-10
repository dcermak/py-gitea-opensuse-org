# CreateForkOption

CreateForkOption options for creating a fork

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the forked repository | [optional] 
**organization** | **str** | organization name, if forking into an organization | [optional] 
**reparent** | **bool** | set the target fork as the parent of the source repository | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.create_fork_option import CreateForkOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateForkOption from a JSON string
create_fork_option_instance = CreateForkOption.from_json(json)
# print the JSON string representation of the object
print(CreateForkOption.to_json())

# convert the object into a dict
create_fork_option_dict = create_fork_option_instance.to_dict()
# create an instance of CreateForkOption from a dict
create_fork_option_from_dict = CreateForkOption.from_dict(create_fork_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



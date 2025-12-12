# NodeInfoUsageUsers

NodeInfoUsageUsers contains statistics about the users of this server

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_halfyear** | **int** | ActiveHalfyear is the amount of users that signed in at least once in the last 180 days | [optional] 
**active_month** | **int** | ActiveMonth is the amount of users that signed in at least once in the last 30 days | [optional] 
**total** | **int** | Total is the total amount of users on this server | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.node_info_usage_users import NodeInfoUsageUsers

# TODO update the JSON string below
json = "{}"
# create an instance of NodeInfoUsageUsers from a JSON string
node_info_usage_users_instance = NodeInfoUsageUsers.from_json(json)
# print the JSON string representation of the object
print(NodeInfoUsageUsers.to_json())

# convert the object into a dict
node_info_usage_users_dict = node_info_usage_users_instance.to_dict()
# create an instance of NodeInfoUsageUsers from a dict
node_info_usage_users_from_dict = NodeInfoUsageUsers.from_dict(node_info_usage_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# NodeInfo

NodeInfo contains standardized way of exposing metadata about a server running one of the distributed social networks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** | Metadata contains free form key value pairs for software specific values | [optional] 
**open_registrations** | **bool** | OpenRegistrations indicates if new user registrations are accepted | [optional] 
**protocols** | **List[str]** | Protocols lists the protocols supported by this server | [optional] 
**services** | [**NodeInfoServices**](NodeInfoServices.md) |  | [optional] 
**software** | [**NodeInfoSoftware**](NodeInfoSoftware.md) |  | [optional] 
**usage** | [**NodeInfoUsage**](NodeInfoUsage.md) |  | [optional] 
**version** | **str** | Version specifies the schema version | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.node_info import NodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NodeInfo from a JSON string
node_info_instance = NodeInfo.from_json(json)
# print the JSON string representation of the object
print(NodeInfo.to_json())

# convert the object into a dict
node_info_dict = node_info_instance.to_dict()
# create an instance of NodeInfo from a dict
node_info_from_dict = NodeInfo.from_dict(node_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



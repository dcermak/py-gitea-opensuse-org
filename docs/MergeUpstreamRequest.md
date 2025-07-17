# MergeUpstreamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.merge_upstream_request import MergeUpstreamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MergeUpstreamRequest from a JSON string
merge_upstream_request_instance = MergeUpstreamRequest.from_json(json)
# print the JSON string representation of the object
print(MergeUpstreamRequest.to_json())

# convert the object into a dict
merge_upstream_request_dict = merge_upstream_request_instance.to_dict()
# create an instance of MergeUpstreamRequest from a dict
merge_upstream_request_from_dict = MergeUpstreamRequest.from_dict(merge_upstream_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



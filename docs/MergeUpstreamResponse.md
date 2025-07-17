# MergeUpstreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merge_type** | **str** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.merge_upstream_response import MergeUpstreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MergeUpstreamResponse from a JSON string
merge_upstream_response_instance = MergeUpstreamResponse.from_json(json)
# print the JSON string representation of the object
print(MergeUpstreamResponse.to_json())

# convert the object into a dict
merge_upstream_response_dict = merge_upstream_response_instance.to_dict()
# create an instance of MergeUpstreamResponse from a dict
merge_upstream_response_from_dict = MergeUpstreamResponse.from_dict(merge_upstream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



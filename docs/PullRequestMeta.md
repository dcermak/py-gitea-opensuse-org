# PullRequestMeta

PullRequestMeta PR info if an issue is a PR

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merged** | **bool** |  | [optional] 
**merged_at** | **datetime** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.pull_request_meta import PullRequestMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestMeta from a JSON string
pull_request_meta_instance = PullRequestMeta.from_json(json)
# print the JSON string representation of the object
print PullRequestMeta.to_json()

# convert the object into a dict
pull_request_meta_dict = pull_request_meta_instance.to_dict()
# create an instance of PullRequestMeta from a dict
pull_request_meta_form_dict = pull_request_meta.from_dict(pull_request_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



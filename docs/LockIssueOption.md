# LockIssueOption

LockIssueOption options to lock an issue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lock_reason** | **str** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.lock_issue_option import LockIssueOption

# TODO update the JSON string below
json = "{}"
# create an instance of LockIssueOption from a JSON string
lock_issue_option_instance = LockIssueOption.from_json(json)
# print the JSON string representation of the object
print(LockIssueOption.to_json())

# convert the object into a dict
lock_issue_option_dict = lock_issue_option_instance.to_dict()
# create an instance of LockIssueOption from a dict
lock_issue_option_from_dict = LockIssueOption.from_dict(lock_issue_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



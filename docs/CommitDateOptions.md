# CommitDateOptions

CommitDateOptions store dates for GIT_AUTHOR_DATE and GIT_COMMITTER_DATE

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **datetime** |  | [optional] 
**committer** | **datetime** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.commit_date_options import CommitDateOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CommitDateOptions from a JSON string
commit_date_options_instance = CommitDateOptions.from_json(json)
# print the JSON string representation of the object
print(CommitDateOptions.to_json())

# convert the object into a dict
commit_date_options_dict = commit_date_options_instance.to_dict()
# create an instance of CommitDateOptions from a dict
commit_date_options_from_dict = CommitDateOptions.from_dict(commit_date_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



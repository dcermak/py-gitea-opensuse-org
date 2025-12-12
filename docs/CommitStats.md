# CommitStats

CommitStats is statistics for a RepoCommit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additions** | **int** | Additions is the number of lines added | [optional] 
**deletions** | **int** | Deletions is the number of lines deleted | [optional] 
**total** | **int** | Total is the total number of lines changed | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.commit_stats import CommitStats

# TODO update the JSON string below
json = "{}"
# create an instance of CommitStats from a JSON string
commit_stats_instance = CommitStats.from_json(json)
# print the JSON string representation of the object
print(CommitStats.to_json())

# convert the object into a dict
commit_stats_dict = commit_stats_instance.to_dict()
# create an instance of CommitStats from a dict
commit_stats_from_dict = CommitStats.from_dict(commit_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



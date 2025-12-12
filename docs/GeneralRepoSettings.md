# GeneralRepoSettings

GeneralRepoSettings contains global repository settings exposed by API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_git_disabled** | **bool** | HTTPGitDisabled indicates if HTTP Git operations are disabled | [optional] 
**lfs_disabled** | **bool** | LFSDisabled indicates if Git LFS support is disabled | [optional] 
**migrations_disabled** | **bool** | MigrationsDisabled indicates if repository migrations are disabled | [optional] 
**mirrors_disabled** | **bool** | MirrorsDisabled indicates if repository mirroring is disabled | [optional] 
**stars_disabled** | **bool** | StarsDisabled indicates if repository starring is disabled | [optional] 
**time_tracking_disabled** | **bool** | TimeTrackingDisabled indicates if time tracking is disabled | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.general_repo_settings import GeneralRepoSettings

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralRepoSettings from a JSON string
general_repo_settings_instance = GeneralRepoSettings.from_json(json)
# print the JSON string representation of the object
print(GeneralRepoSettings.to_json())

# convert the object into a dict
general_repo_settings_dict = general_repo_settings_instance.to_dict()
# create an instance of GeneralRepoSettings from a dict
general_repo_settings_from_dict = GeneralRepoSettings.from_dict(general_repo_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



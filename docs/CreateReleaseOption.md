# CreateReleaseOption

CreateReleaseOption options when creating a release

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The release notes or description | [optional] 
**draft** | **bool** | Whether to create the release as a draft | [optional] 
**name** | **str** | The display title of the release | [optional] 
**prerelease** | **bool** | Whether to mark the release as a prerelease | [optional] 
**tag_message** | **str** | The message for the git tag | [optional] 
**tag_name** | **str** |  | 
**target_commitish** | **str** | The target commitish for the release | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.create_release_option import CreateReleaseOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReleaseOption from a JSON string
create_release_option_instance = CreateReleaseOption.from_json(json)
# print the JSON string representation of the object
print(CreateReleaseOption.to_json())

# convert the object into a dict
create_release_option_dict = create_release_option_instance.to_dict()
# create an instance of CreateReleaseOption from a dict
create_release_option_from_dict = CreateReleaseOption.from_dict(create_release_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



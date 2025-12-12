# EditReleaseOption

EditReleaseOption options when editing a release

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The new release notes or description | [optional] 
**draft** | **bool** | Whether to change the draft status | [optional] 
**name** | **str** | The new display title of the release | [optional] 
**prerelease** | **bool** | Whether to change the prerelease status | [optional] 
**tag_name** | **str** | The new name of the git tag | [optional] 
**target_commitish** | **str** | The new target commitish for the release | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.edit_release_option import EditReleaseOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditReleaseOption from a JSON string
edit_release_option_instance = EditReleaseOption.from_json(json)
# print the JSON string representation of the object
print(EditReleaseOption.to_json())

# convert the object into a dict
edit_release_option_dict = edit_release_option_instance.to_dict()
# create an instance of EditReleaseOption from a dict
edit_release_option_from_dict = EditReleaseOption.from_dict(edit_release_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApplyDiffPatchFileOptions

ApplyDiffPatchFileOptions options for applying a diff patch Note: `author` and `committer` are optional (if only one is given, it will be used for the other, otherwise the authenticated user will be used)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**Identity**](Identity.md) |  | [optional] 
**branch** | **str** | branch (optional) is the base branch for the changes. If not supplied, the default branch is used | [optional] 
**committer** | [**Identity**](Identity.md) |  | [optional] 
**content** | **str** |  | 
**dates** | [**CommitDateOptions**](CommitDateOptions.md) |  | [optional] 
**force_push** | **bool** | force_push (optional) will do a force-push if the new branch already exists | [optional] 
**message** | **str** | message (optional) is the commit message of the changes. If not supplied, a default message will be used | [optional] 
**new_branch** | **str** | new_branch (optional) will make a new branch from base branch for the changes. If not supplied, the changes will be committed to the base branch | [optional] 
**signoff** | **bool** | Add a Signed-off-by trailer by the committer at the end of the commit log message. | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.apply_diff_patch_file_options import ApplyDiffPatchFileOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyDiffPatchFileOptions from a JSON string
apply_diff_patch_file_options_instance = ApplyDiffPatchFileOptions.from_json(json)
# print the JSON string representation of the object
print(ApplyDiffPatchFileOptions.to_json())

# convert the object into a dict
apply_diff_patch_file_options_dict = apply_diff_patch_file_options_instance.to_dict()
# create an instance of ApplyDiffPatchFileOptions from a dict
apply_diff_patch_file_options_from_dict = ApplyDiffPatchFileOptions.from_dict(apply_diff_patch_file_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



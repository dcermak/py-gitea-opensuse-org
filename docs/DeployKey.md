# DeployKey

DeployKey a deploy key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**fingerprint** | **str** | Fingerprint is the key&#39;s fingerprint | [optional] 
**id** | **int** | ID is the unique identifier for the deploy key | [optional] 
**key** | **str** | Key contains the actual SSH key content | [optional] 
**key_id** | **int** | KeyID is the associated public key ID | [optional] 
**read_only** | **bool** | ReadOnly indicates if the key has read-only access | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**title** | **str** | Title is the human-readable name for the key | [optional] 
**url** | **str** | URL is the API URL for this deploy key | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.deploy_key import DeployKey

# TODO update the JSON string below
json = "{}"
# create an instance of DeployKey from a JSON string
deploy_key_instance = DeployKey.from_json(json)
# print the JSON string representation of the object
print(DeployKey.to_json())

# convert the object into a dict
deploy_key_dict = deploy_key_instance.to_dict()
# create an instance of DeployKey from a dict
deploy_key_from_dict = DeployKey.from_dict(deploy_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



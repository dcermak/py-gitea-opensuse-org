# PublicKey

PublicKey publickey is a user key to push code to repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**fingerprint** | **str** | Fingerprint is the key&#39;s fingerprint | [optional] 
**id** | **int** | ID is the unique identifier for the public key | [optional] 
**key** | **str** | Key contains the actual SSH public key content | [optional] 
**key_type** | **str** | KeyType indicates the type of the SSH key | [optional] 
**last_used_at** | **datetime** | Updated is the time when the key was last used | [optional] 
**read_only** | **bool** | ReadOnly indicates if the key has read-only access | [optional] 
**title** | **str** | Title is the human-readable name for the key | [optional] 
**url** | **str** | URL is the API URL for this key | [optional] 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.public_key import PublicKey

# TODO update the JSON string below
json = "{}"
# create an instance of PublicKey from a JSON string
public_key_instance = PublicKey.from_json(json)
# print the JSON string representation of the object
print(PublicKey.to_json())

# convert the object into a dict
public_key_dict = public_key_instance.to_dict()
# create an instance of PublicKey from a dict
public_key_from_dict = PublicKey.from_dict(public_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



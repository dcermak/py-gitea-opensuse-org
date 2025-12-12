# GPGKey

GPGKey a user GPG key to sign commit and tag in repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_certify** | **bool** | Whether the key can be used for certification | [optional] 
**can_encrypt_comms** | **bool** | Whether the key can be used for encrypting communications | [optional] 
**can_encrypt_storage** | **bool** | Whether the key can be used for encrypting storage | [optional] 
**can_sign** | **bool** | Whether the key can be used for signing | [optional] 
**created_at** | **datetime** |  | [optional] 
**emails** | [**List[GPGKeyEmail]**](GPGKeyEmail.md) | List of email addresses associated with this GPG key | [optional] 
**expires_at** | **datetime** |  | [optional] 
**id** | **int** | The unique identifier of the GPG key | [optional] 
**key_id** | **str** | The key ID of the GPG key | [optional] 
**primary_key_id** | **str** | The primary key ID of the GPG key | [optional] 
**public_key** | **str** | The public key content in armored format | [optional] 
**subkeys** | [**List[GPGKey]**](GPGKey.md) | List of subkeys of this GPG key | [optional] 
**verified** | **bool** | Whether the GPG key has been verified | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.gpg_key import GPGKey

# TODO update the JSON string below
json = "{}"
# create an instance of GPGKey from a JSON string
gpg_key_instance = GPGKey.from_json(json)
# print the JSON string representation of the object
print(GPGKey.to_json())

# convert the object into a dict
gpg_key_dict = gpg_key_instance.to_dict()
# create an instance of GPGKey from a dict
gpg_key_from_dict = GPGKey.from_dict(gpg_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



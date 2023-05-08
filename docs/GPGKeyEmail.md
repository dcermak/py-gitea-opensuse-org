# GPGKeyEmail

GPGKeyEmail an email attached to a GPGKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.gpg_key_email import GPGKeyEmail

# TODO update the JSON string below
json = "{}"
# create an instance of GPGKeyEmail from a JSON string
gpg_key_email_instance = GPGKeyEmail.from_json(json)
# print the JSON string representation of the object
print GPGKeyEmail.to_json()

# convert the object into a dict
gpg_key_email_dict = gpg_key_email_instance.to_dict()
# create an instance of GPGKeyEmail from a dict
gpg_key_email_form_dict = gpg_key_email.from_dict(gpg_key_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



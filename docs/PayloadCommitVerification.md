# PayloadCommitVerification

PayloadCommitVerification represents the GPG verification of a commit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** | The signed payload content | [optional] 
**reason** | **str** | The reason for the verification status | [optional] 
**signature** | **str** | The GPG signature of the commit | [optional] 
**signer** | [**PayloadUser**](PayloadUser.md) |  | [optional] 
**verified** | **bool** | Whether the commit signature is verified | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.payload_commit_verification import PayloadCommitVerification

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadCommitVerification from a JSON string
payload_commit_verification_instance = PayloadCommitVerification.from_json(json)
# print the JSON string representation of the object
print(PayloadCommitVerification.to_json())

# convert the object into a dict
payload_commit_verification_dict = payload_commit_verification_instance.to_dict()
# create an instance of PayloadCommitVerification from a dict
payload_commit_verification_from_dict = PayloadCommitVerification.from_dict(payload_commit_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



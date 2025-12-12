# AccessToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The timestamp when the token was created | [optional] 
**id** | **int** | The unique identifier of the access token | [optional] 
**last_used_at** | **datetime** | The timestamp when the token was last used | [optional] 
**name** | **str** | The name of the access token | [optional] 
**scopes** | **List[str]** | The scopes granted to this access token | [optional] 
**sha1** | **str** | The SHA1 hash of the access token | [optional] 
**token_last_eight** | **str** | The last eight characters of the token | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.access_token import AccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of AccessToken from a JSON string
access_token_instance = AccessToken.from_json(json)
# print the JSON string representation of the object
print(AccessToken.to_json())

# convert the object into a dict
access_token_dict = access_token_instance.to_dict()
# create an instance of AccessToken from a dict
access_token_from_dict = AccessToken.from_dict(access_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



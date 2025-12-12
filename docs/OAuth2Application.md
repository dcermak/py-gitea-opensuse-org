# OAuth2Application


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The client ID of the OAuth2 application | [optional] 
**client_secret** | **str** | The client secret of the OAuth2 application | [optional] 
**confidential_client** | **bool** | Whether the client is confidential | [optional] 
**created** | **datetime** | The timestamp when the application was created | [optional] 
**id** | **int** | The unique identifier of the OAuth2 application | [optional] 
**name** | **str** | The name of the OAuth2 application | [optional] 
**redirect_uris** | **List[str]** | The list of allowed redirect URIs | [optional] 
**skip_secondary_authorization** | **bool** | Whether to skip secondary authorization | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.o_auth2_application import OAuth2Application

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Application from a JSON string
o_auth2_application_instance = OAuth2Application.from_json(json)
# print the JSON string representation of the object
print(OAuth2Application.to_json())

# convert the object into a dict
o_auth2_application_dict = o_auth2_application_instance.to_dict()
# create an instance of OAuth2Application from a dict
o_auth2_application_from_dict = OAuth2Application.from_dict(o_auth2_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



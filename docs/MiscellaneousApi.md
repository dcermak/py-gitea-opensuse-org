# py_gitea_opensuse_org.MiscellaneousApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_node_info**](MiscellaneousApi.md#get_node_info) | **GET** /nodeinfo | Returns the nodeinfo of the Gitea application
[**get_signing_key**](MiscellaneousApi.md#get_signing_key) | **GET** /signing-key.gpg | Get default signing-key.gpg
[**get_version**](MiscellaneousApi.md#get_version) | **GET** /version | Returns the version of the Gitea application
[**render_markdown**](MiscellaneousApi.md#render_markdown) | **POST** /markdown | Render a markdown document as HTML
[**render_markdown_raw**](MiscellaneousApi.md#render_markdown_raw) | **POST** /markdown/raw | Render raw markdown as HTML


# **get_node_info**
> NodeInfo get_node_info()

Returns the nodeinfo of the Gitea application

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):
```python
import time
import os
import py_gitea_opensuse_org
from py_gitea_opensuse_org.models.node_info import NodeInfo
from py_gitea_opensuse_org.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = py_gitea_opensuse_org.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = py_gitea_opensuse_org.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
async with py_gitea_opensuse_org.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_gitea_opensuse_org.MiscellaneousApi(api_client)

    try:
        # Returns the nodeinfo of the Gitea application
        api_response = await api_instance.get_node_info()
        print("The response of MiscellaneousApi->get_node_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscellaneousApi->get_node_info: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeInfo**](NodeInfo.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NodeInfo |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signing_key**
> str get_signing_key()

Get default signing-key.gpg

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):
```python
import time
import os
import py_gitea_opensuse_org
from py_gitea_opensuse_org.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = py_gitea_opensuse_org.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = py_gitea_opensuse_org.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
async with py_gitea_opensuse_org.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_gitea_opensuse_org.MiscellaneousApi(api_client)

    try:
        # Get default signing-key.gpg
        api_response = await api_instance.get_signing_key()
        print("The response of MiscellaneousApi->get_signing_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscellaneousApi->get_signing_key: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GPG armored public key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> ServerVersion get_version()

Returns the version of the Gitea application

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):
```python
import time
import os
import py_gitea_opensuse_org
from py_gitea_opensuse_org.models.server_version import ServerVersion
from py_gitea_opensuse_org.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = py_gitea_opensuse_org.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = py_gitea_opensuse_org.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
async with py_gitea_opensuse_org.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_gitea_opensuse_org.MiscellaneousApi(api_client)

    try:
        # Returns the version of the Gitea application
        api_response = await api_instance.get_version()
        print("The response of MiscellaneousApi->get_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscellaneousApi->get_version: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerVersion**](ServerVersion.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ServerVersion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_markdown**
> str render_markdown(body=body)

Render a markdown document as HTML

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):
```python
import time
import os
import py_gitea_opensuse_org
from py_gitea_opensuse_org.models.markdown_option import MarkdownOption
from py_gitea_opensuse_org.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = py_gitea_opensuse_org.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = py_gitea_opensuse_org.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
async with py_gitea_opensuse_org.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_gitea_opensuse_org.MiscellaneousApi(api_client)
    body = py_gitea_opensuse_org.MarkdownOption() # MarkdownOption |  (optional)

    try:
        # Render a markdown document as HTML
        api_response = await api_instance.render_markdown(body=body)
        print("The response of MiscellaneousApi->render_markdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscellaneousApi->render_markdown: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MarkdownOption**](MarkdownOption.md)|  | [optional] 

### Return type

**str**

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarkdownRender is a rendered markdown document |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_markdown_raw**
> str render_markdown_raw(body)

Render raw markdown as HTML

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):
```python
import time
import os
import py_gitea_opensuse_org
from py_gitea_opensuse_org.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = py_gitea_opensuse_org.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = py_gitea_opensuse_org.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
async with py_gitea_opensuse_org.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = py_gitea_opensuse_org.MiscellaneousApi(api_client)
    body = 'body_example' # str | Request body to render

    try:
        # Render raw markdown as HTML
        api_response = await api_instance.render_markdown_raw(body)
        print("The response of MiscellaneousApi->render_markdown_raw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscellaneousApi->render_markdown_raw: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Request body to render | 

### Return type

**str**

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarkdownRender is a rendered markdown document |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


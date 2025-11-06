# openapi_client.MethodsApi

All URIs are relative to *http://datamonkey.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_methods_list**](MethodsApi.md#get_methods_list) | **GET** /methods | Get a list of available HyPhy methods


# **get_methods_list**
> MethodsList get_methods_list(pretty_print=pretty_print)

Get a list of available HyPhy methods

Returns a list of all available HyPhy methods that can be run on the server

### Example


```python
import openapi_client
from openapi_client.models.methods_list import MethodsList
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://datamonkey.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://datamonkey.org/api/v1"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MethodsApi(api_client)
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Get a list of available HyPhy methods
        api_response = await api_instance.get_methods_list(pretty_print=pretty_print)
        print("The response of MethodsApi->get_methods_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MethodsApi->get_methods_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**MethodsList**](MethodsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


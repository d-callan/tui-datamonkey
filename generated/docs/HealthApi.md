# openapi_client.HealthApi

All URIs are relative to *http://datamonkey.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](HealthApi.md#get_health) | **GET** /health | Check health of Datamonkey


# **get_health**
> Health get_health(pretty_print=pretty_print)

Check health of Datamonkey

### Example


```python
import openapi_client
from openapi_client.models.health import Health
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
    api_instance = openapi_client.HealthApi(api_client)
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Check health of Datamonkey
        api_response = await api_instance.get_health(pretty_print=pretty_print)
        print("The response of HealthApi->get_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->get_health: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**Health**](Health.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Unable to get health. Internal server error |  -  |
**503** | Unable to get health. Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


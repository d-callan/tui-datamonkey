# openapi_client.ABSRELApi

All URIs are relative to *http://datamonkey.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_absrel_job**](ABSRELApi.md#get_absrel_job) | **POST** /methods/absrel-result | Get an ABSREL job result
[**get_absrel_job_by_id**](ABSRELApi.md#get_absrel_job_by_id) | **GET** /methods/absrel-result | Get an ABSREL job result by job ID
[**start_absrel_job**](ABSRELApi.md#start_absrel_job) | **POST** /methods/absrel-start | Start and monitor an ABSREL job


# **get_absrel_job**
> AbsrelResult get_absrel_job(user_token, absrel_request, pretty_print=pretty_print)

Get an ABSREL job result

### Example


```python
import openapi_client
from openapi_client.models.absrel_request import AbsrelRequest
from openapi_client.models.absrel_result import AbsrelResult
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
    api_instance = openapi_client.ABSRELApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user
    absrel_request = openapi_client.AbsrelRequest() # AbsrelRequest | 
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Get an ABSREL job result
        api_response = await api_instance.get_absrel_job(user_token, absrel_request, pretty_print=pretty_print)
        print("The response of ABSRELApi->get_absrel_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ABSRELApi->get_absrel_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user | 
 **absrel_request** | [**AbsrelRequest**](AbsrelRequest.md)|  | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**AbsrelResult**](AbsrelResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized - Invalid user token |  -  |
**403** | Forbidden - User does not have permission to access this job |  -  |
**404** | Job not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_absrel_job_by_id**
> AbsrelResult get_absrel_job_by_id(job_id, user_token, pretty_print=pretty_print)

Get an ABSREL job result by job ID

### Example


```python
import openapi_client
from openapi_client.models.absrel_result import AbsrelResult
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
    api_instance = openapi_client.ABSRELApi(api_client)
    job_id = 'job_id_example' # str | Job ID to fetch results for
    user_token = 'user_token_example' # str | Token identifying the user
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Get an ABSREL job result by job ID
        api_response = await api_instance.get_absrel_job_by_id(job_id, user_token, pretty_print=pretty_print)
        print("The response of ABSRELApi->get_absrel_job_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ABSRELApi->get_absrel_job_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID to fetch results for | 
 **user_token** | **str**| Token identifying the user | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**AbsrelResult**](AbsrelResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized - Invalid user token |  -  |
**403** | Forbidden - User does not have permission to access this job |  -  |
**404** | Job not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_absrel_job**
> JobStatus start_absrel_job(user_token, absrel_request, pretty_print=pretty_print)

Start and monitor an ABSREL job

### Example


```python
import openapi_client
from openapi_client.models.absrel_request import AbsrelRequest
from openapi_client.models.job_status import JobStatus
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
    api_instance = openapi_client.ABSRELApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user. Required to reference datasets owned by the user.
    absrel_request = openapi_client.AbsrelRequest() # AbsrelRequest | 
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Start and monitor an ABSREL job
        api_response = await api_instance.start_absrel_job(user_token, absrel_request, pretty_print=pretty_print)
        print("The response of ABSRELApi->start_absrel_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ABSRELApi->start_absrel_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user. Required to reference datasets owned by the user. | 
 **absrel_request** | [**AbsrelRequest**](AbsrelRequest.md)|  | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**JobStatus**](JobStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job started successfully. |  -  |
**401** | Unauthorized - Invalid or missing user token |  -  |
**403** | Forbidden - User does not have access to the specified dataset(s) |  -  |
**404** | Not Found - Specified dataset(s) not found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


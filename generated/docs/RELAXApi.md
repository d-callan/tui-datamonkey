# openapi_client.RELAXApi

All URIs are relative to *http://datamonkey.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_relax_job**](RELAXApi.md#get_relax_job) | **POST** /methods/relax-result | Get RELAX analysis results
[**get_relax_job_by_id**](RELAXApi.md#get_relax_job_by_id) | **GET** /methods/relax-result | Get a RELAX job result by job ID
[**start_relax_job**](RELAXApi.md#start_relax_job) | **POST** /methods/relax-start | Start and monitor a RELAX job


# **get_relax_job**
> RelaxResult get_relax_job(user_token, relax_request, pretty_print=pretty_print)

Get RELAX analysis results

### Example


```python
import openapi_client
from openapi_client.models.relax_request import RelaxRequest
from openapi_client.models.relax_result import RelaxResult
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
    api_instance = openapi_client.RELAXApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user
    relax_request = openapi_client.RelaxRequest() # RelaxRequest | 
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Get RELAX analysis results
        api_response = await api_instance.get_relax_job(user_token, relax_request, pretty_print=pretty_print)
        print("The response of RELAXApi->get_relax_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RELAXApi->get_relax_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user | 
 **relax_request** | [**RelaxRequest**](RelaxRequest.md)|  | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**RelaxResult**](RelaxResult.md)

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

# **get_relax_job_by_id**
> RelaxResult get_relax_job_by_id(job_id, user_token, pretty_print=pretty_print)

Get a RELAX job result by job ID

### Example


```python
import openapi_client
from openapi_client.models.relax_result import RelaxResult
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
    api_instance = openapi_client.RELAXApi(api_client)
    job_id = 'job_id_example' # str | Job ID to fetch results for
    user_token = 'user_token_example' # str | Token identifying the user
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Get a RELAX job result by job ID
        api_response = await api_instance.get_relax_job_by_id(job_id, user_token, pretty_print=pretty_print)
        print("The response of RELAXApi->get_relax_job_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RELAXApi->get_relax_job_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID to fetch results for | 
 **user_token** | **str**| Token identifying the user | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**RelaxResult**](RelaxResult.md)

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

# **start_relax_job**
> JobStatus start_relax_job(user_token, relax_request, pretty_print=pretty_print)

Start and monitor a RELAX job

### Example


```python
import openapi_client
from openapi_client.models.job_status import JobStatus
from openapi_client.models.relax_request import RelaxRequest
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
    api_instance = openapi_client.RELAXApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user. Required to reference datasets owned by the user.
    relax_request = openapi_client.RelaxRequest() # RelaxRequest | 
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Start and monitor a RELAX job
        api_response = await api_instance.start_relax_job(user_token, relax_request, pretty_print=pretty_print)
        print("The response of RELAXApi->start_relax_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RELAXApi->start_relax_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user. Required to reference datasets owned by the user. | 
 **relax_request** | [**RelaxRequest**](RelaxRequest.md)|  | 
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


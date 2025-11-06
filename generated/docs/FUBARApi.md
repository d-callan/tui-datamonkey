# openapi_client.FUBARApi

All URIs are relative to *http://datamonkey.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fubar_job**](FUBARApi.md#get_fubar_job) | **POST** /methods/fubar-result | Get FUBAR analysis results
[**get_fubar_job_by_id**](FUBARApi.md#get_fubar_job_by_id) | **GET** /methods/fubar-result | Get a FUBAR job result by job ID
[**start_fubar_job**](FUBARApi.md#start_fubar_job) | **POST** /methods/fubar-start | Start a FUBAR analysis


# **get_fubar_job**
> FubarResult get_fubar_job(user_token, fubar_request, pretty_print=pretty_print)

Get FUBAR analysis results

Retrieves the results of a previously submitted Fast Unconstrained Bayesian AppRoximation (FUBAR) job. FUBAR uses a Bayesian approach to infer selection pressures at individual sites, providing posterior probabilities of positive and negative selection. 

### Example


```python
import openapi_client
from openapi_client.models.fubar_request import FubarRequest
from openapi_client.models.fubar_result import FubarResult
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
    api_instance = openapi_client.FUBARApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user
    fubar_request = openapi_client.FubarRequest() # FubarRequest | 
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Get FUBAR analysis results
        api_response = await api_instance.get_fubar_job(user_token, fubar_request, pretty_print=pretty_print)
        print("The response of FUBARApi->get_fubar_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FUBARApi->get_fubar_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user | 
 **fubar_request** | [**FubarRequest**](FubarRequest.md)|  | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**FubarResult**](FubarResult.md)

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

# **get_fubar_job_by_id**
> FubarResult get_fubar_job_by_id(job_id, user_token, pretty_print=pretty_print)

Get a FUBAR job result by job ID

### Example


```python
import openapi_client
from openapi_client.models.fubar_result import FubarResult
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
    api_instance = openapi_client.FUBARApi(api_client)
    job_id = 'job_id_example' # str | Job ID to fetch results for
    user_token = 'user_token_example' # str | Token identifying the user
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Get a FUBAR job result by job ID
        api_response = await api_instance.get_fubar_job_by_id(job_id, user_token, pretty_print=pretty_print)
        print("The response of FUBARApi->get_fubar_job_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FUBARApi->get_fubar_job_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID to fetch results for | 
 **user_token** | **str**| Token identifying the user | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**FubarResult**](FubarResult.md)

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

# **start_fubar_job**
> JobStatus start_fubar_job(user_token, fubar_request, pretty_print=pretty_print)

Start a FUBAR analysis

Starts a Fast Unconstrained Bayesian AppRoximation (FUBAR) job to detect sites under positive selection. FUBAR uses a Bayesian approach to infer selection pressures at individual sites, providing posterior probabilities of positive and negative selection. 

### Example


```python
import openapi_client
from openapi_client.models.fubar_request import FubarRequest
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
    api_instance = openapi_client.FUBARApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user. Required to reference datasets owned by the user.
    fubar_request = openapi_client.FubarRequest() # FubarRequest | 
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Start a FUBAR analysis
        api_response = await api_instance.start_fubar_job(user_token, fubar_request, pretty_print=pretty_print)
        print("The response of FUBARApi->start_fubar_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FUBARApi->start_fubar_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user. Required to reference datasets owned by the user. | 
 **fubar_request** | [**FubarRequest**](FubarRequest.md)|  | 
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


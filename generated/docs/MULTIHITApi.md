# openapi_client.MULTIHITApi

All URIs are relative to *http://datamonkey.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_multihit_job**](MULTIHITApi.md#get_multihit_job) | **POST** /methods/multihit-result | Get MULTI-HIT analysis results
[**get_multihit_job_by_id**](MULTIHITApi.md#get_multihit_job_by_id) | **GET** /methods/multihit-result | Get a MULTI-HIT job result by job ID
[**start_multihit_job**](MULTIHITApi.md#start_multihit_job) | **POST** /methods/multihit-start | Start a MULTI-HIT analysis


# **get_multihit_job**
> MultihitResult get_multihit_job(user_token, multihit_request, pretty_print=pretty_print)

Get MULTI-HIT analysis results

Retrieve the results of a previously submitted MULTI-HIT analysis job. Results include evidence ratios for different substitution types, site-specific substitutions, model fitting information, and statistical test results comparing different models. 

### Example


```python
import openapi_client
from openapi_client.models.multihit_request import MultihitRequest
from openapi_client.models.multihit_result import MultihitResult
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
    api_instance = openapi_client.MULTIHITApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user
    multihit_request = openapi_client.MultihitRequest() # MultihitRequest | 
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Get MULTI-HIT analysis results
        api_response = await api_instance.get_multihit_job(user_token, multihit_request, pretty_print=pretty_print)
        print("The response of MULTIHITApi->get_multihit_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MULTIHITApi->get_multihit_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user | 
 **multihit_request** | [**MultihitRequest**](MultihitRequest.md)|  | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**MultihitResult**](MultihitResult.md)

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

# **get_multihit_job_by_id**
> MultihitResult get_multihit_job_by_id(job_id, user_token, pretty_print=pretty_print)

Get a MULTI-HIT job result by job ID

### Example


```python
import openapi_client
from openapi_client.models.multihit_result import MultihitResult
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
    api_instance = openapi_client.MULTIHITApi(api_client)
    job_id = 'job_id_example' # str | Job ID to fetch results for
    user_token = 'user_token_example' # str | Token identifying the user
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Get a MULTI-HIT job result by job ID
        api_response = await api_instance.get_multihit_job_by_id(job_id, user_token, pretty_print=pretty_print)
        print("The response of MULTIHITApi->get_multihit_job_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MULTIHITApi->get_multihit_job_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID to fetch results for | 
 **user_token** | **str**| Token identifying the user | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**MultihitResult**](MultihitResult.md)

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

# **start_multihit_job**
> JobStatus start_multihit_job(user_token, multihit_request, pretty_print=pretty_print)

Start a MULTI-HIT analysis

MULTI-HIT (Multiple Hit) examines whether or not a codon alignment is better fit by models  which permit multiple instantaneous substitutions. It can analyze both double-hit and  triple-hit substitutions, with an option to account for synonymous triple-hit substitutions. 

### Example


```python
import openapi_client
from openapi_client.models.job_status import JobStatus
from openapi_client.models.multihit_request import MultihitRequest
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
    api_instance = openapi_client.MULTIHITApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user. Required to reference datasets owned by the user.
    multihit_request = openapi_client.MultihitRequest() # MultihitRequest | 
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Start a MULTI-HIT analysis
        api_response = await api_instance.start_multihit_job(user_token, multihit_request, pretty_print=pretty_print)
        print("The response of MULTIHITApi->start_multihit_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MULTIHITApi->start_multihit_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user. Required to reference datasets owned by the user. | 
 **multihit_request** | [**MultihitRequest**](MultihitRequest.md)|  | 
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


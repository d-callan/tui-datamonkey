# openapi_client.FADEApi

All URIs are relative to *http://datamonkey.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fade_results**](FADEApi.md#get_fade_results) | **POST** /methods/fade-result | Get a FADE job result
[**get_fade_results_by_id**](FADEApi.md#get_fade_results_by_id) | **GET** /methods/fade-result | Get a FADE job result by job ID
[**start_fade_job**](FADEApi.md#start_fade_job) | **POST** /methods/fade-start | Start a FADE job


# **get_fade_results**
> FadeResult get_fade_results(user_token, fade_request, pretty_print=pretty_print)

Get a FADE job result

### Example


```python
import openapi_client
from openapi_client.models.fade_request import FadeRequest
from openapi_client.models.fade_result import FadeResult
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
    api_instance = openapi_client.FADEApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user
    fade_request = openapi_client.FadeRequest() # FadeRequest | 
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Get a FADE job result
        api_response = await api_instance.get_fade_results(user_token, fade_request, pretty_print=pretty_print)
        print("The response of FADEApi->get_fade_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FADEApi->get_fade_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user | 
 **fade_request** | [**FadeRequest**](FadeRequest.md)|  | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**FadeResult**](FadeResult.md)

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

# **get_fade_results_by_id**
> FadeResult get_fade_results_by_id(job_id, user_token, pretty_print=pretty_print)

Get a FADE job result by job ID

### Example


```python
import openapi_client
from openapi_client.models.fade_result import FadeResult
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
    api_instance = openapi_client.FADEApi(api_client)
    job_id = 'job_id_example' # str | Job ID to fetch results for
    user_token = 'user_token_example' # str | Token identifying the user
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Get a FADE job result by job ID
        api_response = await api_instance.get_fade_results_by_id(job_id, user_token, pretty_print=pretty_print)
        print("The response of FADEApi->get_fade_results_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FADEApi->get_fade_results_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID to fetch results for | 
 **user_token** | **str**| Token identifying the user | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**FadeResult**](FadeResult.md)

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

# **start_fade_job**
> JobStatus start_fade_job(user_token, fade_request, pretty_print=pretty_print)

Start a FADE job

Start a FADE (FUBAR Approach to Directional Evolution) job. FADE is a fast method to test  whether or not a subset of sites in a protein alignment evolve towards a particular residue  along a subset of branches at accelerated rates compared to reference model. FADE uses a  random effects model and latent Dirichlet allocation (LDA) - inspired approximation methods  to allocate sites to rate classes. 

### Example


```python
import openapi_client
from openapi_client.models.fade_request import FadeRequest
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
    api_instance = openapi_client.FADEApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user. Required to reference datasets owned by the user.
    fade_request = openapi_client.FadeRequest() # FadeRequest | 
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Start a FADE job
        api_response = await api_instance.start_fade_job(user_token, fade_request, pretty_print=pretty_print)
        print("The response of FADEApi->start_fade_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FADEApi->start_fade_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user. Required to reference datasets owned by the user. | 
 **fade_request** | [**FadeRequest**](FadeRequest.md)|  | 
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


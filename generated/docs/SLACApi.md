# openapi_client.SLACApi

All URIs are relative to *http://datamonkey.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_slac_job**](SLACApi.md#get_slac_job) | **POST** /methods/slac-result | Get SLAC analysis results
[**get_slac_job_by_id**](SLACApi.md#get_slac_job_by_id) | **GET** /methods/slac-result | Get a SLAC job result by job ID
[**start_slac_job**](SLACApi.md#start_slac_job) | **POST** /methods/slac-start | Start a SLAC analysis


# **get_slac_job**
> SlacResult get_slac_job(user_token, slac_request, pretty_print=pretty_print)

Get SLAC analysis results

Retrieve the results of a previously submitted SLAC (Single Likelihood Ancestor Counting) analysis job. Results include model fitting information, branch attributes, and site-specific dN/dS estimates. 

### Example


```python
import openapi_client
from openapi_client.models.slac_request import SlacRequest
from openapi_client.models.slac_result import SlacResult
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
    api_instance = openapi_client.SLACApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user
    slac_request = openapi_client.SlacRequest() # SlacRequest | 
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Get SLAC analysis results
        api_response = await api_instance.get_slac_job(user_token, slac_request, pretty_print=pretty_print)
        print("The response of SLACApi->get_slac_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLACApi->get_slac_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user | 
 **slac_request** | [**SlacRequest**](SlacRequest.md)|  | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**SlacResult**](SlacResult.md)

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

# **get_slac_job_by_id**
> SlacResult get_slac_job_by_id(job_id, user_token, pretty_print=pretty_print)

Get a SLAC job result by job ID

### Example


```python
import openapi_client
from openapi_client.models.slac_result import SlacResult
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
    api_instance = openapi_client.SLACApi(api_client)
    job_id = 'job_id_example' # str | Job ID to fetch results for
    user_token = 'user_token_example' # str | Token identifying the user
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Get a SLAC job result by job ID
        api_response = await api_instance.get_slac_job_by_id(job_id, user_token, pretty_print=pretty_print)
        print("The response of SLACApi->get_slac_job_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLACApi->get_slac_job_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID to fetch results for | 
 **user_token** | **str**| Token identifying the user | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**SlacResult**](SlacResult.md)

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

# **start_slac_job**
> JobStatus start_slac_job(user_token, slac_request, pretty_print=pretty_print)

Start a SLAC analysis

SLAC (Single Likelihood Ancestor Counting) uses a maximum likelihood ancestral state reconstruction and minimum path substitution counting to estimate site-level dS and dN, and applies a simple binomial-based test to test if dS differs from dN. The estimates aggregate information over all branches, so the signal is derived from pervasive diversification or conservation. 

### Example


```python
import openapi_client
from openapi_client.models.job_status import JobStatus
from openapi_client.models.slac_request import SlacRequest
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
    api_instance = openapi_client.SLACApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user. Required to reference datasets owned by the user.
    slac_request = openapi_client.SlacRequest() # SlacRequest | 
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Start a SLAC analysis
        api_response = await api_instance.start_slac_job(user_token, slac_request, pretty_print=pretty_print)
        print("The response of SLACApi->start_slac_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLACApi->start_slac_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user. Required to reference datasets owned by the user. | 
 **slac_request** | [**SlacRequest**](SlacRequest.md)|  | 
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


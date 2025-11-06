# openapi_client.CONTRASTFELApi

All URIs are relative to *http://datamonkey.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contrast_fel_job_by_id**](CONTRASTFELApi.md#get_contrast_fel_job_by_id) | **GET** /methods/contrast-fel-result | Get CONTRAST-FEL job result by job ID
[**get_contrastfel_job**](CONTRASTFELApi.md#get_contrastfel_job) | **POST** /methods/contrast-fel-result | Get CONTRAST-FEL analysis results
[**start_contrastfel_job**](CONTRASTFELApi.md#start_contrastfel_job) | **POST** /methods/contrast-fel-start | Start a CONTRAST-FEL analysis


# **get_contrast_fel_job_by_id**
> ContrastFelResult get_contrast_fel_job_by_id(job_id, user_token)

Get CONTRAST-FEL job result by job ID

### Example


```python
import openapi_client
from openapi_client.models.contrast_fel_result import ContrastFelResult
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
    api_instance = openapi_client.CONTRASTFELApi(api_client)
    job_id = 'job_id_example' # str | Job ID to fetch results for
    user_token = 'user_token_example' # str | Token identifying the user

    try:
        # Get CONTRAST-FEL job result by job ID
        api_response = await api_instance.get_contrast_fel_job_by_id(job_id, user_token)
        print("The response of CONTRASTFELApi->get_contrast_fel_job_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CONTRASTFELApi->get_contrast_fel_job_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID to fetch results for | 
 **user_token** | **str**| Token identifying the user | 

### Return type

[**ContrastFelResult**](ContrastFelResult.md)

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

# **get_contrastfel_job**
> ContrastFelResult get_contrastfel_job(user_token, contrast_fel_request)

Get CONTRAST-FEL analysis results

Retrieves the results of a previously submitted CONTRAST-FEL job. CONTRAST-FEL investigates whether  selective pressures differ between two or more sets of branches at a site by estimating site-specific  synonymous and non-synonymous substitution rates. 

### Example


```python
import openapi_client
from openapi_client.models.contrast_fel_request import ContrastFelRequest
from openapi_client.models.contrast_fel_result import ContrastFelResult
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
    api_instance = openapi_client.CONTRASTFELApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user
    contrast_fel_request = openapi_client.ContrastFelRequest() # ContrastFelRequest | 

    try:
        # Get CONTRAST-FEL analysis results
        api_response = await api_instance.get_contrastfel_job(user_token, contrast_fel_request)
        print("The response of CONTRASTFELApi->get_contrastfel_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CONTRASTFELApi->get_contrastfel_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user | 
 **contrast_fel_request** | [**ContrastFelRequest**](ContrastFelRequest.md)|  | 

### Return type

[**ContrastFelResult**](ContrastFelResult.md)

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

# **start_contrastfel_job**
> JobStatus start_contrastfel_job(user_token, contrast_fel_request, pretty_print=pretty_print)

Start a CONTRAST-FEL analysis

Starts a Contrast-FEL (Fixed Effects Likelihood with Contrast) job to investigate whether selective pressures differ  between two or more sets of branches at a site. The method estimates site-specific synonymous (alpha) and  non-synonymous (beta, one per branch set) substitution rates and tests beta rates for equality at each site. 

### Example


```python
import openapi_client
from openapi_client.models.contrast_fel_request import ContrastFelRequest
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
    api_instance = openapi_client.CONTRASTFELApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user. Required to reference datasets owned by the user.
    contrast_fel_request = openapi_client.ContrastFelRequest() # ContrastFelRequest | 
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Start a CONTRAST-FEL analysis
        api_response = await api_instance.start_contrastfel_job(user_token, contrast_fel_request, pretty_print=pretty_print)
        print("The response of CONTRASTFELApi->start_contrastfel_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CONTRASTFELApi->start_contrastfel_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user. Required to reference datasets owned by the user. | 
 **contrast_fel_request** | [**ContrastFelRequest**](ContrastFelRequest.md)|  | 
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


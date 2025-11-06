# openapi_client.JobsApi

All URIs are relative to *http://datamonkey.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_job**](JobsApi.md#delete_job) | **DELETE** /jobs/{jobId} | Delete a job
[**get_job_by_id**](JobsApi.md#get_job_by_id) | **GET** /jobs/{jobId} | Get details for a specific job
[**get_jobs_list**](JobsApi.md#get_jobs_list) | **GET** /jobs | Get a list of jobs for the authenticated user


# **delete_job**
> delete_job(job_id, user_token, pretty_print=pretty_print)

Delete a job

Delete a job from the Datamonkey server. If the job is running, it will be cancelled.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.JobsApi(api_client)
    job_id = 'job_id_example' # str | ID of the job
    user_token = 'user_token_example' # str | Token identifying the user who owns the job
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Delete a job
        await api_instance.delete_job(job_id, user_token, pretty_print=pretty_print)
    except Exception as e:
        print("Exception when calling JobsApi->delete_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| ID of the job | 
 **user_token** | **str**| Token identifying the user who owns the job | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Job deleted successfully |  -  |
**401** | Unauthorized - Invalid or missing user token |  -  |
**403** | Forbidden - User does not own this job |  -  |
**404** | Job not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_by_id**
> JobStatus get_job_by_id(job_id, pretty_print=pretty_print, user_token=user_token)

Get details for a specific job

Get detailed information about a specific job

### Example


```python
import openapi_client
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
    api_instance = openapi_client.JobsApi(api_client)
    job_id = 'job_id_example' # str | ID of the job
    pretty_print = True # bool | Pretty print response (optional)
    user_token = 'user_token_example' # str | Token identifying the user (required if job is private) (optional)

    try:
        # Get details for a specific job
        api_response = await api_instance.get_job_by_id(job_id, pretty_print=pretty_print, user_token=user_token)
        print("The response of JobsApi->get_job_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| ID of the job | 
 **pretty_print** | **bool**| Pretty print response | [optional] 
 **user_token** | **str**| Token identifying the user (required if job is private) | [optional] 

### Return type

[**JobStatus**](JobStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized - Invalid or missing user token for private job |  -  |
**403** | Forbidden - User does not own this job |  -  |
**404** | Job not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs_list**
> GetJobsList200Response get_jobs_list(user_token, pretty_print=pretty_print, alignment_id=alignment_id, tree_id=tree_id, method=method, status=status)

Get a list of jobs for the authenticated user

Returns jobs owned by the authenticated user, with optional filtering by alignment ID, tree ID, method, and/or status

### Example


```python
import openapi_client
from openapi_client.models.get_jobs_list200_response import GetJobsList200Response
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
    api_instance = openapi_client.JobsApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user
    pretty_print = True # bool | Pretty print response (optional)
    alignment_id = 'alignment_id_example' # str | Filter jobs by alignment dataset ID (optional)
    tree_id = 'tree_id_example' # str | Filter jobs by tree dataset ID (optional)
    method = 'method_example' # str | Filter jobs by HyPhy method (optional)
    status = 'status_example' # str | Filter jobs by status (optional)

    try:
        # Get a list of jobs for the authenticated user
        api_response = await api_instance.get_jobs_list(user_token, pretty_print=pretty_print, alignment_id=alignment_id, tree_id=tree_id, method=method, status=status)
        print("The response of JobsApi->get_jobs_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_jobs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user | 
 **pretty_print** | **bool**| Pretty print response | [optional] 
 **alignment_id** | **str**| Filter jobs by alignment dataset ID | [optional] 
 **tree_id** | **str**| Filter jobs by tree dataset ID | [optional] 
 **method** | **str**| Filter jobs by HyPhy method | [optional] 
 **status** | **str**| Filter jobs by status | [optional] 

### Return type

[**GetJobsList200Response**](GetJobsList200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - returns user&#39;s jobs |  -  |
**401** | Unauthorized - Invalid or missing user token |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


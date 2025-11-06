# openapi_client.FileUploadAndQCApi

All URIs are relative to *http://datamonkey.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dataset**](FileUploadAndQCApi.md#delete_dataset) | **DELETE** /datasets/{datasetId} | Delete a dataset
[**get_dataset_by_id**](FileUploadAndQCApi.md#get_dataset_by_id) | **GET** /datasets/{datasetId} | Get details for a specific dataset
[**get_datasets_list**](FileUploadAndQCApi.md#get_datasets_list) | **GET** /datasets | Get a list of datasets for the authenticated user
[**post_dataset**](FileUploadAndQCApi.md#post_dataset) | **POST** /datasets | Upload a dataset to Datamonkey


# **delete_dataset**
> delete_dataset(dataset_id, user_token, pretty_print=pretty_print)

Delete a dataset

Delete a dataset from the Datamonkey server

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
    api_instance = openapi_client.FileUploadAndQCApi(api_client)
    dataset_id = 'dataset_id_example' # str | ID of the dataset to retrieve
    user_token = 'user_token_example' # str | Token identifying the user who owns the dataset
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Delete a dataset
        await api_instance.delete_dataset(dataset_id, user_token, pretty_print=pretty_print)
    except Exception as e:
        print("Exception when calling FileUploadAndQCApi->delete_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| ID of the dataset to retrieve | 
 **user_token** | **str**| Token identifying the user who owns the dataset | 
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
**204** | Dataset deleted successfully |  -  |
**401** | Unauthorized - Invalid or missing user token |  -  |
**403** | Forbidden - User does not own this dataset |  -  |
**404** | Dataset not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_by_id**
> Dataset get_dataset_by_id(dataset_id, pretty_print=pretty_print, user_token=user_token, include_content=include_content)

Get details for a specific dataset

Get detailed information about a specific dataset. By default, returns metadata only (id, name, type, description, timestamps). Use `include_content=true` query parameter to include the actual sequence data. 

### Example


```python
import openapi_client
from openapi_client.models.dataset import Dataset
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
    api_instance = openapi_client.FileUploadAndQCApi(api_client)
    dataset_id = 'dataset_id_example' # str | ID of the dataset to retrieve
    pretty_print = True # bool | Pretty print response (optional)
    user_token = 'user_token_example' # str | Token identifying the user (required if dataset is private) (optional)
    include_content = False # bool | If true, includes the dataset content (sequence data) in the response. Default is false (metadata only) for better performance.  (optional) (default to False)

    try:
        # Get details for a specific dataset
        api_response = await api_instance.get_dataset_by_id(dataset_id, pretty_print=pretty_print, user_token=user_token, include_content=include_content)
        print("The response of FileUploadAndQCApi->get_dataset_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileUploadAndQCApi->get_dataset_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| ID of the dataset to retrieve | 
 **pretty_print** | **bool**| Pretty print response | [optional] 
 **user_token** | **str**| Token identifying the user (required if dataset is private) | [optional] 
 **include_content** | **bool**| If true, includes the dataset content (sequence data) in the response. Default is false (metadata only) for better performance.  | [optional] [default to False]

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized - Invalid or missing user token for private dataset |  -  |
**404** | Dataset not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasets_list**
> Datasets get_datasets_list(user_token, pretty_print=pretty_print)

Get a list of datasets for the authenticated user

Returns datasets owned by the authenticated user

### Example


```python
import openapi_client
from openapi_client.models.datasets import Datasets
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
    api_instance = openapi_client.FileUploadAndQCApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Get a list of datasets for the authenticated user
        api_response = await api_instance.get_datasets_list(user_token, pretty_print=pretty_print)
        print("The response of FileUploadAndQCApi->get_datasets_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileUploadAndQCApi->get_datasets_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**Datasets**](Datasets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - returns user&#39;s datasets |  -  |
**401** | Unauthorized - Invalid or missing user token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dataset**
> Datasets post_dataset(pretty_print=pretty_print, user_token=user_token, meta=meta, user_token2=user_token2, file=file, url=url)

Upload a dataset to Datamonkey

### Example


```python
import openapi_client
from openapi_client.models.dataset_meta import DatasetMeta
from openapi_client.models.datasets import Datasets
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
    api_instance = openapi_client.FileUploadAndQCApi(api_client)
    pretty_print = True # bool | Pretty print response (optional)
    user_token = 'user_token_example' # str | Token identifying the user. If not provided, a new session will be created automatically. (optional)
    meta = openapi_client.DatasetMeta() # DatasetMeta |  (optional)
    user_token2 = 'user_token_example' # str | Token identifying the user who is uploading the dataset (optional)
    file = None # bytearray | Dataset File. incompatible with the url field (optional)
    url = 'url_example' # str | URL of the file to upload. incompatible with the file field (optional)

    try:
        # Upload a dataset to Datamonkey
        api_response = await api_instance.post_dataset(pretty_print=pretty_print, user_token=user_token, meta=meta, user_token2=user_token2, file=file, url=url)
        print("The response of FileUploadAndQCApi->post_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileUploadAndQCApi->post_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty_print** | **bool**| Pretty print response | [optional] 
 **user_token** | **str**| Token identifying the user. If not provided, a new session will be created automatically. | [optional] 
 **meta** | [**DatasetMeta**](DatasetMeta.md)|  | [optional] 
 **user_token2** | **str**| Token identifying the user who is uploading the dataset | [optional] 
 **file** | **bytearray**| Dataset File. incompatible with the url field | [optional] 
 **url** | **str**| URL of the file to upload. incompatible with the file field | [optional] 

### Return type

[**Datasets**](Datasets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Dataset uploaded successfully. If no token was provided, a new session token is returned in the X-Session-Token response header. |  * X-Session-Token -  <br>  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


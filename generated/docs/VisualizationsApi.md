# openapi_client.VisualizationsApi

All URIs are relative to *http://datamonkey.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_visualization**](VisualizationsApi.md#create_visualization) | **POST** /visualizations | Create a new visualization
[**delete_visualization**](VisualizationsApi.md#delete_visualization) | **DELETE** /visualizations/{vizId} | Delete a visualization
[**get_visualization**](VisualizationsApi.md#get_visualization) | **GET** /visualizations/{vizId} | Get details for a specific visualization
[**get_visualizations_list**](VisualizationsApi.md#get_visualizations_list) | **GET** /visualizations | Get a list of visualizations for the authenticated user
[**update_visualization**](VisualizationsApi.md#update_visualization) | **PUT** /visualizations/{vizId} | Update a visualization


# **create_visualization**
> Visualization create_visualization(user_token, create_visualization_request, pretty_print=pretty_print)

Create a new visualization

Create and store a new Vega-Lite visualization specification

### Example


```python
import openapi_client
from openapi_client.models.create_visualization_request import CreateVisualizationRequest
from openapi_client.models.visualization import Visualization
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
    api_instance = openapi_client.VisualizationsApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user
    create_visualization_request = openapi_client.CreateVisualizationRequest() # CreateVisualizationRequest | 
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Create a new visualization
        api_response = await api_instance.create_visualization(user_token, create_visualization_request, pretty_print=pretty_print)
        print("The response of VisualizationsApi->create_visualization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VisualizationsApi->create_visualization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user | 
 **create_visualization_request** | [**CreateVisualizationRequest**](CreateVisualizationRequest.md)|  | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**Visualization**](Visualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Visualization created successfully |  -  |
**400** | Bad Request - Invalid visualization data |  -  |
**401** | Unauthorized - Invalid or missing user token |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_visualization**
> delete_visualization(viz_id, user_token, pretty_print=pretty_print)

Delete a visualization

Delete a visualization from the Datamonkey server

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
    api_instance = openapi_client.VisualizationsApi(api_client)
    viz_id = 'viz_id_example' # str | ID of the visualization to retrieve
    user_token = 'user_token_example' # str | Token identifying the user who owns the visualization
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Delete a visualization
        await api_instance.delete_visualization(viz_id, user_token, pretty_print=pretty_print)
    except Exception as e:
        print("Exception when calling VisualizationsApi->delete_visualization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viz_id** | **str**| ID of the visualization to retrieve | 
 **user_token** | **str**| Token identifying the user who owns the visualization | 
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
**204** | Visualization deleted successfully |  -  |
**401** | Unauthorized - Invalid or missing user token |  -  |
**403** | Forbidden - User does not own this visualization |  -  |
**404** | Visualization not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_visualization**
> Visualization get_visualization(viz_id, pretty_print=pretty_print, user_token=user_token)

Get details for a specific visualization

Retrieve a specific visualization by its ID

### Example


```python
import openapi_client
from openapi_client.models.visualization import Visualization
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
    api_instance = openapi_client.VisualizationsApi(api_client)
    viz_id = 'viz_id_example' # str | ID of the visualization to retrieve
    pretty_print = True # bool | Pretty print response (optional)
    user_token = 'user_token_example' # str | Token identifying the user. Required for private visualizations, optional for public ones. (optional)

    try:
        # Get details for a specific visualization
        api_response = await api_instance.get_visualization(viz_id, pretty_print=pretty_print, user_token=user_token)
        print("The response of VisualizationsApi->get_visualization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VisualizationsApi->get_visualization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viz_id** | **str**| ID of the visualization to retrieve | 
 **pretty_print** | **bool**| Pretty print response | [optional] 
 **user_token** | **str**| Token identifying the user. Required for private visualizations, optional for public ones. | [optional] 

### Return type

[**Visualization**](Visualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized - Invalid or missing user token for private visualization |  -  |
**404** | Visualization not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_visualizations_list**
> Visualizations get_visualizations_list(user_token, pretty_print=pretty_print, job_id=job_id, dataset_id=dataset_id)

Get a list of visualizations for the authenticated user

Returns visualizations owned by the authenticated user. Can be filtered by job ID or dataset ID.

### Example


```python
import openapi_client
from openapi_client.models.visualizations import Visualizations
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
    api_instance = openapi_client.VisualizationsApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user
    pretty_print = True # bool | Pretty print response (optional)
    job_id = 'job_id_example' # str | Filter visualizations by job ID (optional)
    dataset_id = 'dataset_id_example' # str | Filter visualizations by dataset ID (optional)

    try:
        # Get a list of visualizations for the authenticated user
        api_response = await api_instance.get_visualizations_list(user_token, pretty_print=pretty_print, job_id=job_id, dataset_id=dataset_id)
        print("The response of VisualizationsApi->get_visualizations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VisualizationsApi->get_visualizations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user | 
 **pretty_print** | **bool**| Pretty print response | [optional] 
 **job_id** | **str**| Filter visualizations by job ID | [optional] 
 **dataset_id** | **str**| Filter visualizations by dataset ID | [optional] 

### Return type

[**Visualizations**](Visualizations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - returns user&#39;s visualizations |  -  |
**401** | Unauthorized - Invalid or missing user token |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_visualization**
> Visualization update_visualization(viz_id, user_token, update_visualization_request, pretty_print=pretty_print)

Update a visualization

Update an existing visualization's metadata or spec

### Example


```python
import openapi_client
from openapi_client.models.update_visualization_request import UpdateVisualizationRequest
from openapi_client.models.visualization import Visualization
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
    api_instance = openapi_client.VisualizationsApi(api_client)
    viz_id = 'viz_id_example' # str | ID of the visualization to retrieve
    user_token = 'user_token_example' # str | Token identifying the user who owns the visualization
    update_visualization_request = openapi_client.UpdateVisualizationRequest() # UpdateVisualizationRequest | 
    pretty_print = True # bool | Pretty print response (optional)

    try:
        # Update a visualization
        api_response = await api_instance.update_visualization(viz_id, user_token, update_visualization_request, pretty_print=pretty_print)
        print("The response of VisualizationsApi->update_visualization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VisualizationsApi->update_visualization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viz_id** | **str**| ID of the visualization to retrieve | 
 **user_token** | **str**| Token identifying the user who owns the visualization | 
 **update_visualization_request** | [**UpdateVisualizationRequest**](UpdateVisualizationRequest.md)|  | 
 **pretty_print** | **bool**| Pretty print response | [optional] 

### Return type

[**Visualization**](Visualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Visualization updated successfully |  -  |
**400** | Bad Request - Invalid update data |  -  |
**401** | Unauthorized - Invalid or missing user token |  -  |
**403** | Forbidden - User does not own this visualization |  -  |
**404** | Visualization not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


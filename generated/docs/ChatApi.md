# openapi_client.ChatApi

All URIs are relative to *http://datamonkey.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_conversation**](ChatApi.md#create_conversation) | **POST** /chat | Create a new conversation
[**delete_conversation**](ChatApi.md#delete_conversation) | **DELETE** /chat/{conversationId} | Delete a conversation
[**get_conversation**](ChatApi.md#get_conversation) | **GET** /chat/{conversationId} | Get a conversation by ID
[**get_conversation_messages**](ChatApi.md#get_conversation_messages) | **GET** /chat/{conversationId}/messages | Get messages from a conversation
[**list_user_conversations**](ChatApi.md#list_user_conversations) | **GET** /chat | List conversations for the authenticated user
[**send_conversation_message**](ChatApi.md#send_conversation_message) | **POST** /chat/{conversationId}/messages | Send a message to the conversation


# **create_conversation**
> ChatConversation create_conversation(user_token=user_token, create_conversation_request=create_conversation_request)

Create a new conversation

### Example


```python
import openapi_client
from openapi_client.models.chat_conversation import ChatConversation
from openapi_client.models.create_conversation_request import CreateConversationRequest
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
    api_instance = openapi_client.ChatApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user. If not provided, a new session will be created automatically. (optional)
    create_conversation_request = openapi_client.CreateConversationRequest() # CreateConversationRequest |  (optional)

    try:
        # Create a new conversation
        api_response = await api_instance.create_conversation(user_token=user_token, create_conversation_request=create_conversation_request)
        print("The response of ChatApi->create_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->create_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user. If not provided, a new session will be created automatically. | [optional] 
 **create_conversation_request** | [**CreateConversationRequest**](CreateConversationRequest.md)|  | [optional] 

### Return type

[**ChatConversation**](ChatConversation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Conversation created successfully. If no token was provided, a new session token is returned in the X-Session-Token response header. |  * X-Session-Token -  <br>  |
**500** | Internal Server Error - Failed to create session or conversation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_conversation**
> delete_conversation(conversation_id, user_token)

Delete a conversation

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
    api_instance = openapi_client.ChatApi(api_client)
    conversation_id = 'conversation_id_example' # str | ID of the conversation
    user_token = 'user_token_example' # str | Token identifying the user

    try:
        # Delete a conversation
        await api_instance.delete_conversation(conversation_id, user_token)
    except Exception as e:
        print("Exception when calling ChatApi->delete_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| ID of the conversation | 
 **user_token** | **str**| Token identifying the user | 

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
**204** | Conversation deleted |  -  |
**401** | Unauthorized - Invalid or missing user token |  -  |
**403** | Forbidden - User does not own this conversation |  -  |
**404** | Conversation not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation**
> ChatConversation get_conversation(conversation_id, user_token)

Get a conversation by ID

### Example


```python
import openapi_client
from openapi_client.models.chat_conversation import ChatConversation
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
    api_instance = openapi_client.ChatApi(api_client)
    conversation_id = 'conversation_id_example' # str | ID of the conversation
    user_token = 'user_token_example' # str | Token identifying the user

    try:
        # Get a conversation by ID
        api_response = await api_instance.get_conversation(conversation_id, user_token)
        print("The response of ChatApi->get_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| ID of the conversation | 
 **user_token** | **str**| Token identifying the user | 

### Return type

[**ChatConversation**](ChatConversation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conversation details |  -  |
**401** | Unauthorized - Invalid or missing user token |  -  |
**403** | Forbidden - User does not own this conversation |  -  |
**404** | Conversation not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation_messages**
> GetConversationMessages200Response get_conversation_messages(conversation_id, user_token)

Get messages from a conversation

### Example


```python
import openapi_client
from openapi_client.models.get_conversation_messages200_response import GetConversationMessages200Response
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
    api_instance = openapi_client.ChatApi(api_client)
    conversation_id = 'conversation_id_example' # str | ID of the conversation
    user_token = 'user_token_example' # str | Token identifying the user

    try:
        # Get messages from a conversation
        api_response = await api_instance.get_conversation_messages(conversation_id, user_token)
        print("The response of ChatApi->get_conversation_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_conversation_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| ID of the conversation | 
 **user_token** | **str**| Token identifying the user | 

### Return type

[**GetConversationMessages200Response**](GetConversationMessages200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of conversation messages |  -  |
**401** | Unauthorized - Invalid or missing user token |  -  |
**403** | Forbidden - User does not own this conversation |  -  |
**404** | Conversation not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_conversations**
> ListUserConversations200Response list_user_conversations(user_token)

List conversations for the authenticated user

### Example


```python
import openapi_client
from openapi_client.models.list_user_conversations200_response import ListUserConversations200Response
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
    api_instance = openapi_client.ChatApi(api_client)
    user_token = 'user_token_example' # str | Token identifying the user

    try:
        # List conversations for the authenticated user
        api_response = await api_instance.list_user_conversations(user_token)
        print("The response of ChatApi->list_user_conversations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->list_user_conversations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| Token identifying the user | 

### Return type

[**ListUserConversations200Response**](ListUserConversations200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of user&#39;s conversations |  -  |
**401** | Unauthorized - Invalid or missing user token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_conversation_message**
> SendConversationMessage200Response send_conversation_message(conversation_id, user_token, send_conversation_message_request)

Send a message to the conversation

### Example


```python
import openapi_client
from openapi_client.models.send_conversation_message200_response import SendConversationMessage200Response
from openapi_client.models.send_conversation_message_request import SendConversationMessageRequest
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
    api_instance = openapi_client.ChatApi(api_client)
    conversation_id = 'conversation_id_example' # str | ID of the conversation
    user_token = 'user_token_example' # str | Token identifying the user
    send_conversation_message_request = openapi_client.SendConversationMessageRequest() # SendConversationMessageRequest | 

    try:
        # Send a message to the conversation
        api_response = await api_instance.send_conversation_message(conversation_id, user_token, send_conversation_message_request)
        print("The response of ChatApi->send_conversation_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->send_conversation_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| ID of the conversation | 
 **user_token** | **str**| Token identifying the user | 
 **send_conversation_message_request** | [**SendConversationMessageRequest**](SendConversationMessageRequest.md)|  | 

### Return type

[**SendConversationMessage200Response**](SendConversationMessage200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AI response |  -  |
**401** | Unauthorized - Invalid or missing user token |  -  |
**403** | Forbidden - User does not own this conversation |  -  |
**404** | Conversation not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


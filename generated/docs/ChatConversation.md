# ChatConversation

A conversation between a user and the AI assistant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the conversation | 
**title** | **str** | Optional title for the conversation | [optional] 
**created** | **int** | Timestamp when the conversation was created (Unix timestamp in milliseconds) | 
**updated** | **int** | Timestamp when the conversation was last updated (Unix timestamp in milliseconds) | 
**messages** | [**List[ChatMessage]**](ChatMessage.md) | List of messages in the conversation | [optional] 

## Example

```python
from openapi_client.models.chat_conversation import ChatConversation

# TODO update the JSON string below
json = "{}"
# create an instance of ChatConversation from a JSON string
chat_conversation_instance = ChatConversation.from_json(json)
# print the JSON string representation of the object
print(ChatConversation.to_json())

# convert the object into a dict
chat_conversation_dict = chat_conversation_instance.to_dict()
# create an instance of ChatConversation from a dict
chat_conversation_from_dict = ChatConversation.from_dict(chat_conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



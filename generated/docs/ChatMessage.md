# ChatMessage

A message in a chat session

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Role of the message sender | 
**content** | **str** | Content of the message | 
**timestamp** | **int** | Timestamp when the message was sent (Unix timestamp in milliseconds) | [optional] 

## Example

```python
from openapi_client.models.chat_message import ChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessage from a JSON string
chat_message_instance = ChatMessage.from_json(json)
# print the JSON string representation of the object
print(ChatMessage.to_json())

# convert the object into a dict
chat_message_dict = chat_message_instance.to_dict()
# create an instance of ChatMessage from a dict
chat_message_from_dict = ChatMessage.from_dict(chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



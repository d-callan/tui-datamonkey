# SendConversationMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message content to send | 

## Example

```python
from openapi_client.models.send_conversation_message_request import SendConversationMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendConversationMessageRequest from a JSON string
send_conversation_message_request_instance = SendConversationMessageRequest.from_json(json)
# print the JSON string representation of the object
print(SendConversationMessageRequest.to_json())

# convert the object into a dict
send_conversation_message_request_dict = send_conversation_message_request_instance.to_dict()
# create an instance of SendConversationMessageRequest from a dict
send_conversation_message_request_from_dict = SendConversationMessageRequest.from_dict(send_conversation_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



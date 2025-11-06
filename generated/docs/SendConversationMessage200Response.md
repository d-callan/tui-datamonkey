# SendConversationMessage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | [**ChatMessage**](ChatMessage.md) |  | [optional] 

## Example

```python
from openapi_client.models.send_conversation_message200_response import SendConversationMessage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SendConversationMessage200Response from a JSON string
send_conversation_message200_response_instance = SendConversationMessage200Response.from_json(json)
# print the JSON string representation of the object
print(SendConversationMessage200Response.to_json())

# convert the object into a dict
send_conversation_message200_response_dict = send_conversation_message200_response_instance.to_dict()
# create an instance of SendConversationMessage200Response from a dict
send_conversation_message200_response_from_dict = SendConversationMessage200Response.from_dict(send_conversation_message200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



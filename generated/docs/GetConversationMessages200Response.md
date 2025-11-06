# GetConversationMessages200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[ChatMessage]**](ChatMessage.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_conversation_messages200_response import GetConversationMessages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetConversationMessages200Response from a JSON string
get_conversation_messages200_response_instance = GetConversationMessages200Response.from_json(json)
# print the JSON string representation of the object
print(GetConversationMessages200Response.to_json())

# convert the object into a dict
get_conversation_messages200_response_dict = get_conversation_messages200_response_instance.to_dict()
# create an instance of GetConversationMessages200Response from a dict
get_conversation_messages200_response_from_dict = GetConversationMessages200Response.from_dict(get_conversation_messages200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



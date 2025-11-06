# ListUserConversations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversations** | [**List[ChatConversation]**](ChatConversation.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_user_conversations200_response import ListUserConversations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserConversations200Response from a JSON string
list_user_conversations200_response_instance = ListUserConversations200Response.from_json(json)
# print the JSON string representation of the object
print(ListUserConversations200Response.to_json())

# convert the object into a dict
list_user_conversations200_response_dict = list_user_conversations200_response_instance.to_dict()
# create an instance of ListUserConversations200Response from a dict
list_user_conversations200_response_from_dict = ListUserConversations200Response.from_dict(list_user_conversations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



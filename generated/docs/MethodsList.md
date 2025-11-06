# MethodsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**methods** | [**List[MethodsListMethodsInner]**](MethodsListMethodsInner.md) | List of available HyPhy methods | [optional] 

## Example

```python
from openapi_client.models.methods_list import MethodsList

# TODO update the JSON string below
json = "{}"
# create an instance of MethodsList from a JSON string
methods_list_instance = MethodsList.from_json(json)
# print the JSON string representation of the object
print(MethodsList.to_json())

# convert the object into a dict
methods_list_dict = methods_list_instance.to_dict()
# create an instance of MethodsList from a dict
methods_list_from_dict = MethodsList.from_dict(methods_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



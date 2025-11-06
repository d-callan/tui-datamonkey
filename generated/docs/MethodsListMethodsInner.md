# MethodsListMethodsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Method identifier (e.g., \&quot;fel\&quot;, \&quot;busted\&quot;, \&quot;absrel\&quot;) | [optional] 
**name** | **str** | Human-readable name of the method | [optional] 
**description** | **str** | Brief description of what the method does | [optional] 
**status** | **str** | Current status of the method | [optional] [default to 'available']
**start_endpoint** | **str** | API endpoint to start a job for this method | [optional] 
**result_endpoint** | **str** | API endpoint to retrieve results for this method | [optional] 
**parameters** | [**List[MethodsListMethodsInnerParametersInner]**](MethodsListMethodsInnerParametersInner.md) | List of parameters expected by this method | [optional] 

## Example

```python
from openapi_client.models.methods_list_methods_inner import MethodsListMethodsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MethodsListMethodsInner from a JSON string
methods_list_methods_inner_instance = MethodsListMethodsInner.from_json(json)
# print the JSON string representation of the object
print(MethodsListMethodsInner.to_json())

# convert the object into a dict
methods_list_methods_inner_dict = methods_list_methods_inner_instance.to_dict()
# create an instance of MethodsListMethodsInner from a dict
methods_list_methods_inner_from_dict = MethodsListMethodsInner.from_dict(methods_list_methods_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



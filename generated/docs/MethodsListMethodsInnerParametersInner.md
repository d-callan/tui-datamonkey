# MethodsListMethodsInnerParametersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Parameter name | [optional] 
**description** | **str** | Description of the parameter | [optional] 
**required** | **bool** | Whether the parameter is required | [optional] 
**type** | **str** | Data type of the parameter | [optional] 
**default** | **str** | Default value of the parameter (if any) | [optional] 

## Example

```python
from openapi_client.models.methods_list_methods_inner_parameters_inner import MethodsListMethodsInnerParametersInner

# TODO update the JSON string below
json = "{}"
# create an instance of MethodsListMethodsInnerParametersInner from a JSON string
methods_list_methods_inner_parameters_inner_instance = MethodsListMethodsInnerParametersInner.from_json(json)
# print the JSON string representation of the object
print(MethodsListMethodsInnerParametersInner.to_json())

# convert the object into a dict
methods_list_methods_inner_parameters_inner_dict = methods_list_methods_inner_parameters_inner_instance.to_dict()
# create an instance of MethodsListMethodsInnerParametersInner from a dict
methods_list_methods_inner_parameters_inner_from_dict = MethodsListMethodsInnerParametersInner.from_dict(methods_list_methods_inner_parameters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



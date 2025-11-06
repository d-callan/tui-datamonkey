# InvalidDataErrorErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The field that caused the error | [optional] 
**message** | **str** | The error message | [optional] 

## Example

```python
from openapi_client.models.invalid_data_error_errors_inner import InvalidDataErrorErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidDataErrorErrorsInner from a JSON string
invalid_data_error_errors_inner_instance = InvalidDataErrorErrorsInner.from_json(json)
# print the JSON string representation of the object
print(InvalidDataErrorErrorsInner.to_json())

# convert the object into a dict
invalid_data_error_errors_inner_dict = invalid_data_error_errors_inner_instance.to_dict()
# create an instance of InvalidDataErrorErrorsInner from a dict
invalid_data_error_errors_inner_from_dict = InvalidDataErrorErrorsInner.from_dict(invalid_data_error_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



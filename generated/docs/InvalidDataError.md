# InvalidDataError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[InvalidDataErrorErrorsInner]**](InvalidDataErrorErrorsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.invalid_data_error import InvalidDataError

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidDataError from a JSON string
invalid_data_error_instance = InvalidDataError.from_json(json)
# print the JSON string representation of the object
print(InvalidDataError.to_json())

# convert the object into a dict
invalid_data_error_dict = invalid_data_error_instance.to_dict()
# create an instance of InvalidDataError from a dict
invalid_data_error_from_dict = InvalidDataError.from_dict(invalid_data_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



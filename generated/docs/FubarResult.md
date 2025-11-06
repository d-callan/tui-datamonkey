# FubarResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**result** | [**FubarResultResult**](FubarResultResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.fubar_result import FubarResult

# TODO update the JSON string below
json = "{}"
# create an instance of FubarResult from a JSON string
fubar_result_instance = FubarResult.from_json(json)
# print the JSON string representation of the object
print(FubarResult.to_json())

# convert the object into a dict
fubar_result_dict = fubar_result_instance.to_dict()
# create an instance of FubarResult from a dict
fubar_result_from_dict = FubarResult.from_dict(fubar_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



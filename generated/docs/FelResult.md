# FelResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**result** | [**FelResultResult**](FelResultResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.fel_result import FelResult

# TODO update the JSON string below
json = "{}"
# create an instance of FelResult from a JSON string
fel_result_instance = FelResult.from_json(json)
# print the JSON string representation of the object
print(FelResult.to_json())

# convert the object into a dict
fel_result_dict = fel_result_instance.to_dict()
# create an instance of FelResult from a dict
fel_result_from_dict = FelResult.from_dict(fel_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AbsrelResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**result** | [**AbsrelResultResult**](AbsrelResultResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.absrel_result import AbsrelResult

# TODO update the JSON string below
json = "{}"
# create an instance of AbsrelResult from a JSON string
absrel_result_instance = AbsrelResult.from_json(json)
# print the JSON string representation of the object
print(AbsrelResult.to_json())

# convert the object into a dict
absrel_result_dict = absrel_result_instance.to_dict()
# create an instance of AbsrelResult from a dict
absrel_result_from_dict = AbsrelResult.from_dict(absrel_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RelaxResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**result** | [**RelaxResultResult**](RelaxResultResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.relax_result import RelaxResult

# TODO update the JSON string below
json = "{}"
# create an instance of RelaxResult from a JSON string
relax_result_instance = RelaxResult.from_json(json)
# print the JSON string representation of the object
print(RelaxResult.to_json())

# convert the object into a dict
relax_result_dict = relax_result_instance.to_dict()
# create an instance of RelaxResult from a dict
relax_result_from_dict = RelaxResult.from_dict(relax_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



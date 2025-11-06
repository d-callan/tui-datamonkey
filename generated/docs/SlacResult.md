# SlacResult

Results from a SLAC (Single Likelihood Ancestor Counting) analysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**result** | [**SlacResultResult**](SlacResultResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.slac_result import SlacResult

# TODO update the JSON string below
json = "{}"
# create an instance of SlacResult from a JSON string
slac_result_instance = SlacResult.from_json(json)
# print the JSON string representation of the object
print(SlacResult.to_json())

# convert the object into a dict
slac_result_dict = slac_result_instance.to_dict()
# create an instance of SlacResult from a dict
slac_result_from_dict = SlacResult.from_dict(slac_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



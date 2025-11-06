# GardResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**result** | [**GardResultResult**](GardResultResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.gard_result import GardResult

# TODO update the JSON string below
json = "{}"
# create an instance of GardResult from a JSON string
gard_result_instance = GardResult.from_json(json)
# print the JSON string representation of the object
print(GardResult.to_json())

# convert the object into a dict
gard_result_dict = gard_result_instance.to_dict()
# create an instance of GardResult from a dict
gard_result_from_dict = GardResult.from_dict(gard_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



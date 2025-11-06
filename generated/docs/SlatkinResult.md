# SlatkinResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**result** | [**SlatkinResultResult**](SlatkinResultResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.slatkin_result import SlatkinResult

# TODO update the JSON string below
json = "{}"
# create an instance of SlatkinResult from a JSON string
slatkin_result_instance = SlatkinResult.from_json(json)
# print the JSON string representation of the object
print(SlatkinResult.to_json())

# convert the object into a dict
slatkin_result_dict = slatkin_result_instance.to_dict()
# create an instance of SlatkinResult from a dict
slatkin_result_from_dict = SlatkinResult.from_dict(slatkin_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



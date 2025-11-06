# MultihitResult

Results from a MULTI-HIT analysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**result** | [**MultihitResultResult**](MultihitResultResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.multihit_result import MultihitResult

# TODO update the JSON string below
json = "{}"
# create an instance of MultihitResult from a JSON string
multihit_result_instance = MultihitResult.from_json(json)
# print the JSON string representation of the object
print(MultihitResult.to_json())

# convert the object into a dict
multihit_result_dict = multihit_result_instance.to_dict()
# create an instance of MultihitResult from a dict
multihit_result_from_dict = MultihitResult.from_dict(multihit_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



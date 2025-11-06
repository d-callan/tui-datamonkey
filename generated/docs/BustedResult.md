# BustedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**result** | [**BustedResultResult**](BustedResultResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.busted_result import BustedResult

# TODO update the JSON string below
json = "{}"
# create an instance of BustedResult from a JSON string
busted_result_instance = BustedResult.from_json(json)
# print the JSON string representation of the object
print(BustedResult.to_json())

# convert the object into a dict
busted_result_dict = busted_result_instance.to_dict()
# create an instance of BustedResult from a dict
busted_result_from_dict = BustedResult.from_dict(busted_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



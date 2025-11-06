# FadeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**result** | [**FadeResultResult**](FadeResultResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.fade_result import FadeResult

# TODO update the JSON string below
json = "{}"
# create an instance of FadeResult from a JSON string
fade_result_instance = FadeResult.from_json(json)
# print the JSON string representation of the object
print(FadeResult.to_json())

# convert the object into a dict
fade_result_dict = fade_result_instance.to_dict()
# create an instance of FadeResult from a dict
fade_result_from_dict = FadeResult.from_dict(fade_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



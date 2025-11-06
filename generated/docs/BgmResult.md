# BgmResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**result** | [**BgmResultResult**](BgmResultResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.bgm_result import BgmResult

# TODO update the JSON string below
json = "{}"
# create an instance of BgmResult from a JSON string
bgm_result_instance = BgmResult.from_json(json)
# print the JSON string representation of the object
print(BgmResult.to_json())

# convert the object into a dict
bgm_result_dict = bgm_result_instance.to_dict()
# create an instance of BgmResult from a dict
bgm_result_from_dict = BgmResult.from_dict(bgm_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BgmResultResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**AnalysisInfo**](AnalysisInfo.md) |  | [optional] 
**input** | [**InputInfo**](InputInfo.md) |  | [optional] 
**tested** | **Dict[str, Dict[str, str]]** |  | [optional] 
**timers** | [**Dict[str, TimersInfoValue]**](TimersInfoValue.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**data_partitions** | [**Dict[str, PartitionsInfoValue]**](PartitionsInfoValue.md) |  | [optional] 
**fits** | [**Dict[str, BgmResultResultAllOfFitsValue]**](BgmResultResultAllOfFitsValue.md) | Model fit information | [optional] 
**mle** | [**BgmResultResultAllOfMLE**](BgmResultResultAllOfMLE.md) |  | [optional] 
**branch_attributes** | **Dict[str, Dict[str, Dict[str, float]]]** | Branch-specific attributes | [optional] 

## Example

```python
from openapi_client.models.bgm_result_result import BgmResultResult

# TODO update the JSON string below
json = "{}"
# create an instance of BgmResultResult from a JSON string
bgm_result_result_instance = BgmResultResult.from_json(json)
# print the JSON string representation of the object
print(BgmResultResult.to_json())

# convert the object into a dict
bgm_result_result_dict = bgm_result_result_instance.to_dict()
# create an instance of BgmResultResult from a dict
bgm_result_result_from_dict = BgmResultResult.from_dict(bgm_result_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



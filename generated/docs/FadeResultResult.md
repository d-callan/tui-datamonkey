# FadeResultResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**AnalysisInfo**](AnalysisInfo.md) |  | [optional] 
**input** | [**InputInfo**](InputInfo.md) |  | [optional] 
**tested** | **Dict[str, Dict[str, str]]** |  | [optional] 
**timers** | [**Dict[str, TimersInfoValue]**](TimersInfoValue.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**data_partitions** | [**Dict[str, PartitionsInfoValue]**](PartitionsInfoValue.md) |  | [optional] 
**fits** | [**Dict[str, FadeResultResultAllOfFitsValue]**](FadeResultResultAllOfFitsValue.md) | Model fit information | [optional] 
**mle** | [**FadeResultResultAllOfMLE**](FadeResultResultAllOfMLE.md) |  | [optional] 
**site_annotations** | [**FadeResultResultAllOfSiteAnnotations**](FadeResultResultAllOfSiteAnnotations.md) |  | [optional] 

## Example

```python
from openapi_client.models.fade_result_result import FadeResultResult

# TODO update the JSON string below
json = "{}"
# create an instance of FadeResultResult from a JSON string
fade_result_result_instance = FadeResultResult.from_json(json)
# print the JSON string representation of the object
print(FadeResultResult.to_json())

# convert the object into a dict
fade_result_result_dict = fade_result_result_instance.to_dict()
# create an instance of FadeResultResult from a dict
fade_result_result_from_dict = FadeResultResult.from_dict(fade_result_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



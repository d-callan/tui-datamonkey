# FubarResultResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**AnalysisInfo**](AnalysisInfo.md) |  | [optional] 
**input** | [**InputInfo**](InputInfo.md) |  | [optional] 
**tested** | **Dict[str, Dict[str, str]]** |  | [optional] 
**timers** | [**Dict[str, TimersInfoValue]**](TimersInfoValue.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**data_partitions** | [**Dict[str, PartitionsInfoValue]**](PartitionsInfoValue.md) |  | [optional] 
**fits** | **Dict[str, object]** | Model fit statistics | [optional] 
**mle** | [**ContrastFelResultResultAllOfMLE**](ContrastFelResultResultAllOfMLE.md) |  | [optional] 
**grid** | **List[List[float]]** | Grid points for the Bayesian analysis | [optional] 

## Example

```python
from openapi_client.models.fubar_result_result import FubarResultResult

# TODO update the JSON string below
json = "{}"
# create an instance of FubarResultResult from a JSON string
fubar_result_result_instance = FubarResultResult.from_json(json)
# print the JSON string representation of the object
print(FubarResultResult.to_json())

# convert the object into a dict
fubar_result_result_dict = fubar_result_result_instance.to_dict()
# create an instance of FubarResultResult from a dict
fubar_result_result_from_dict = FubarResultResult.from_dict(fubar_result_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



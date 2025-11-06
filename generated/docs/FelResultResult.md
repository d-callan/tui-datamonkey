# FelResultResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**AnalysisInfo**](AnalysisInfo.md) |  | [optional] 
**input** | [**InputInfo**](InputInfo.md) |  | [optional] 
**tested** | **Dict[str, Dict[str, str]]** |  | [optional] 
**timers** | [**Dict[str, TimersInfoValue]**](TimersInfoValue.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**data_partitions** | [**Dict[str, PartitionsInfoValue]**](PartitionsInfoValue.md) |  | [optional] 
**fits** | [**Dict[str, FelResultResultAllOfFitsValue]**](FelResultResultAllOfFitsValue.md) |  | [optional] 
**branch_attributes** | [**FelResultResultAllOfBranchAttributes**](FelResultResultAllOfBranchAttributes.md) |  | [optional] 
**mle** | [**FelResultResultAllOfMLE**](FelResultResultAllOfMLE.md) |  | [optional] 

## Example

```python
from openapi_client.models.fel_result_result import FelResultResult

# TODO update the JSON string below
json = "{}"
# create an instance of FelResultResult from a JSON string
fel_result_result_instance = FelResultResult.from_json(json)
# print the JSON string representation of the object
print(FelResultResult.to_json())

# convert the object into a dict
fel_result_result_dict = fel_result_result_instance.to_dict()
# create an instance of FelResultResult from a dict
fel_result_result_from_dict = FelResultResult.from_dict(fel_result_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



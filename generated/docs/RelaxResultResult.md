# RelaxResultResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**AnalysisInfo**](AnalysisInfo.md) |  | [optional] 
**input** | [**InputInfo**](InputInfo.md) |  | [optional] 
**tested** | **Dict[str, Dict[str, str]]** |  | [optional] 
**timers** | [**Dict[str, TimersInfoValue]**](TimersInfoValue.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**data_partitions** | [**Dict[str, PartitionsInfoValue]**](PartitionsInfoValue.md) |  | [optional] 
**fits** | [**RelaxResultResultAllOfFits**](RelaxResultResultAllOfFits.md) |  | [optional] 
**test_results** | [**RelaxResultResultAllOfTestResults**](RelaxResultResultAllOfTestResults.md) |  | [optional] 

## Example

```python
from openapi_client.models.relax_result_result import RelaxResultResult

# TODO update the JSON string below
json = "{}"
# create an instance of RelaxResultResult from a JSON string
relax_result_result_instance = RelaxResultResult.from_json(json)
# print the JSON string representation of the object
print(RelaxResultResult.to_json())

# convert the object into a dict
relax_result_result_dict = relax_result_result_instance.to_dict()
# create an instance of RelaxResultResult from a dict
relax_result_result_from_dict = RelaxResultResult.from_dict(relax_result_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



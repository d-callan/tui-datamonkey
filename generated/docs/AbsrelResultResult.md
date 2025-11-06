# AbsrelResultResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**AnalysisInfo**](AnalysisInfo.md) |  | [optional] 
**input** | [**InputInfo**](InputInfo.md) |  | [optional] 
**tested** | **Dict[str, Dict[str, str]]** |  | [optional] 
**timers** | [**Dict[str, AbsrelResultResultAllOfTimersValue]**](AbsrelResultResultAllOfTimersValue.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**data_partitions** | [**Dict[str, PartitionsInfoValue]**](PartitionsInfoValue.md) |  | [optional] 
**fits** | [**Dict[str, AbsrelResultResultAllOfFitsValue]**](AbsrelResultResultAllOfFitsValue.md) |  | [optional] 
**test_results** | [**AbsrelResultResultAllOfTestResults**](AbsrelResultResultAllOfTestResults.md) |  | [optional] 
**branch_attributes** | [**AbsrelResultResultAllOfBranchAttributes**](AbsrelResultResultAllOfBranchAttributes.md) |  | [optional] 

## Example

```python
from openapi_client.models.absrel_result_result import AbsrelResultResult

# TODO update the JSON string below
json = "{}"
# create an instance of AbsrelResultResult from a JSON string
absrel_result_result_instance = AbsrelResultResult.from_json(json)
# print the JSON string representation of the object
print(AbsrelResultResult.to_json())

# convert the object into a dict
absrel_result_result_dict = absrel_result_result_instance.to_dict()
# create an instance of AbsrelResultResult from a dict
absrel_result_result_from_dict = AbsrelResultResult.from_dict(absrel_result_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



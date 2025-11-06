# NrmResultResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**AnalysisInfo**](AnalysisInfo.md) |  | [optional] 
**input** | [**InputInfo**](InputInfo.md) |  | [optional] 
**tested** | **bool** |  | [optional] 
**timers** | [**Dict[str, TimersInfoValue]**](TimersInfoValue.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**data_partitions** | [**Dict[str, PartitionsInfoValue]**](PartitionsInfoValue.md) |  | [optional] 
**fits** | [**Dict[str, NrmResultResultAllOfFitsValue]**](NrmResultResultAllOfFitsValue.md) |  | [optional] 
**branch_attributes** | **Dict[str, Dict[str, NrmResultResultAllOfBranchAttributesValueValue]]** |  | [optional] 
**test_results** | [**Dict[str, NrmResultResultAllOfTestResultsValue]**](NrmResultResultAllOfTestResultsValue.md) |  | [optional] 
**characters** | **List[List[str]]** |  | [optional] 

## Example

```python
from openapi_client.models.nrm_result_result import NrmResultResult

# TODO update the JSON string below
json = "{}"
# create an instance of NrmResultResult from a JSON string
nrm_result_result_instance = NrmResultResult.from_json(json)
# print the JSON string representation of the object
print(NrmResultResult.to_json())

# convert the object into a dict
nrm_result_result_dict = nrm_result_result_instance.to_dict()
# create an instance of NrmResultResult from a dict
nrm_result_result_from_dict = NrmResultResult.from_dict(nrm_result_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



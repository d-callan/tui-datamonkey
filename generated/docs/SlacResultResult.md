# SlacResultResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**AnalysisInfo**](AnalysisInfo.md) |  | [optional] 
**input** | [**InputInfo**](InputInfo.md) |  | [optional] 
**tested** | **Dict[str, Dict[str, str]]** |  | [optional] 
**timers** | [**Dict[str, TimersInfoValue]**](TimersInfoValue.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**data_partitions** | [**Dict[str, PartitionsInfoValue]**](PartitionsInfoValue.md) |  | [optional] 
**fits** | [**SlacResultResultAllOfFits**](SlacResultResultAllOfFits.md) |  | [optional] 
**branch_attributes** | **Dict[str, Dict[str, SlacResultResultAllOfBranchAttributesValueValue]]** | Branch-specific attributes | [optional] 
**mle** | [**SlacResultResultAllOfMLE**](SlacResultResultAllOfMLE.md) |  | [optional] 
**site_results** | **Dict[str, List[float]]** | Site-specific results | [optional] 

## Example

```python
from openapi_client.models.slac_result_result import SlacResultResult

# TODO update the JSON string below
json = "{}"
# create an instance of SlacResultResult from a JSON string
slac_result_result_instance = SlacResultResult.from_json(json)
# print the JSON string representation of the object
print(SlacResultResult.to_json())

# convert the object into a dict
slac_result_result_dict = slac_result_result_instance.to_dict()
# create an instance of SlacResultResult from a dict
slac_result_result_from_dict = SlacResultResult.from_dict(slac_result_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



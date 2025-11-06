# GardResultResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**AnalysisInfo**](AnalysisInfo.md) |  | [optional] 
**input** | [**InputInfo**](InputInfo.md) |  | [optional] 
**tested** | **Dict[str, Dict[str, str]]** |  | [optional] 
**timers** | [**Dict[str, TimersInfoValue]**](TimersInfoValue.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**data_partitions** | [**Dict[str, PartitionsInfoValue]**](PartitionsInfoValue.md) |  | [optional] 
**baseline_score** | **float** | Baseline score for the analysis | [optional] 
**potential_breakpoints** | **int** | Number of potential breakpoints analyzed | [optional] 
**single_tree_aicc** | **float** | AICc score for the single tree model | [optional] 
**time_elapsed** | **int** | Time elapsed for the analysis in seconds | [optional] 
**total_model_count** | **int** | Total number of models evaluated | [optional] 
**breakpoint_data** | [**Dict[str, GardResultResultAllOfBreakpointDataValue]**](GardResultResultAllOfBreakpointDataValue.md) | Data for each segment between breakpoints | [optional] 
**improvements** | [**Dict[str, GardResultResultAllOfImprovementsValue]**](GardResultResultAllOfImprovementsValue.md) | Improvement metrics for each breakpoint | [optional] 
**site_break_point_support** | **Dict[str, float]** | Support values for potential breakpoints at each site | [optional] 
**trees** | **Dict[str, object]** | Tree data | [optional] 

## Example

```python
from openapi_client.models.gard_result_result import GardResultResult

# TODO update the JSON string below
json = "{}"
# create an instance of GardResultResult from a JSON string
gard_result_result_instance = GardResultResult.from_json(json)
# print the JSON string representation of the object
print(GardResultResult.to_json())

# convert the object into a dict
gard_result_result_dict = gard_result_result_instance.to_dict()
# create an instance of GardResultResult from a dict
gard_result_result_from_dict = GardResultResult.from_dict(gard_result_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



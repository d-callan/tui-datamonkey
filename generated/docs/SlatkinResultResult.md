# SlatkinResultResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**AnalysisInfo**](AnalysisInfo.md) |  | [optional] 
**input** | [**InputInfo**](InputInfo.md) |  | [optional] 
**tested** | **Dict[str, Dict[str, str]]** |  | [optional] 
**timers** | [**Dict[str, TimersInfoValue]**](TimersInfoValue.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**data_partitions** | [**Dict[str, PartitionsInfoValue]**](PartitionsInfoValue.md) |  | [optional] 
**compartments** | **int** | Number of compartments in the analysis | [optional] 
**events** | [**Dict[str, SlatkinResultResultAllOfEventsValue]**](SlatkinResultResultAllOfEventsValue.md) | Migration events between compartments | [optional] 
**leaf_count** | **int** | Number of leaves in the tree | [optional] 
**migrations** | **int** | Number of migration events | [optional] 
**p_value** | [**SlatkinResultResultAllOfPValue**](SlatkinResultResultAllOfPValue.md) |  | [optional] 
**partition_counts** | **Dict[str, int]** | Number of sequences in each partition/compartment | [optional] 
**partitions** | **Dict[str, Dict[str, str]]** | Sequences in each partition/compartment | [optional] 
**replicates** | **int** | Number of bootstrap replicates used | [optional] 
**node_migrations** | **Dict[str, int]** | Number of migrations at each node | [optional] 
**structured_cutoff** | **int** | Cutoff value for structured test | [optional] 
**node_p_value** | [**SlatkinResultResultAllOfNodePValue**](SlatkinResultResultAllOfNodePValue.md) |  | [optional] 
**simulations** | [**SlatkinResultResultAllOfSimulations**](SlatkinResultResultAllOfSimulations.md) |  | [optional] 

## Example

```python
from openapi_client.models.slatkin_result_result import SlatkinResultResult

# TODO update the JSON string below
json = "{}"
# create an instance of SlatkinResultResult from a JSON string
slatkin_result_result_instance = SlatkinResultResult.from_json(json)
# print the JSON string representation of the object
print(SlatkinResultResult.to_json())

# convert the object into a dict
slatkin_result_result_dict = slatkin_result_result_instance.to_dict()
# create an instance of SlatkinResultResult from a dict
slatkin_result_result_from_dict = SlatkinResultResult.from_dict(slatkin_result_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MultihitResultResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**AnalysisInfo**](AnalysisInfo.md) |  | [optional] 
**input** | [**InputInfo**](InputInfo.md) |  | [optional] 
**tested** | **Dict[str, Dict[str, str]]** |  | [optional] 
**timers** | [**Dict[str, TimersInfoValue]**](TimersInfoValue.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**data_partitions** | [**Dict[str, PartitionsInfoValue]**](PartitionsInfoValue.md) |  | [optional] 
**evidence_ratios** | [**MultihitResultResultAllOfEvidenceRatios**](MultihitResultResultAllOfEvidenceRatios.md) |  | [optional] 
**site_substitutions** | **Dict[str, Dict[str, object]]** | Detailed site substitution mappings | [optional] 
**fits** | [**MultihitResultResultAllOfFits**](MultihitResultResultAllOfFits.md) |  | [optional] 
**test_results** | [**MultihitResultResultAllOfTestResults**](MultihitResultResultAllOfTestResults.md) |  | [optional] 

## Example

```python
from openapi_client.models.multihit_result_result import MultihitResultResult

# TODO update the JSON string below
json = "{}"
# create an instance of MultihitResultResult from a JSON string
multihit_result_result_instance = MultihitResultResult.from_json(json)
# print the JSON string representation of the object
print(MultihitResultResult.to_json())

# convert the object into a dict
multihit_result_result_dict = multihit_result_result_instance.to_dict()
# create an instance of MultihitResultResult from a dict
multihit_result_result_from_dict = MultihitResultResult.from_dict(multihit_result_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



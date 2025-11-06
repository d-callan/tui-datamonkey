# BustedResultResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**AnalysisInfo**](AnalysisInfo.md) |  | [optional] 
**input** | [**InputInfo**](InputInfo.md) |  | [optional] 
**tested** | **Dict[str, Dict[str, str]]** |  | [optional] 
**timers** | [**Dict[str, TimersInfoValue]**](TimersInfoValue.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**data_partitions** | [**Dict[str, PartitionsInfoValue]**](PartitionsInfoValue.md) |  | [optional] 
**background** | **float** |  | [optional] 
**fits** | [**Dict[str, BustedResultResultAllOfFitsValue]**](BustedResultResultAllOfFitsValue.md) |  | [optional] 
**branch_attributes** | [**BustedResultResultAllOfBranchAttributes**](BustedResultResultAllOfBranchAttributes.md) |  | [optional] 
**test_results** | [**BustedResultResultAllOfTestResults**](BustedResultResultAllOfTestResults.md) |  | [optional] 
**substitutions** | **Dict[str, Dict[str, BustedResultResultAllOfSubstitutionsValueValue]]** |  | [optional] 
**synonymous_site_posteriors** | **List[List[float]]** |  | [optional] 
**site_log_likelihood** | [**BustedResultResultAllOfSiteLogLikelihood**](BustedResultResultAllOfSiteLogLikelihood.md) |  | [optional] 
**evidence_ratios** | [**BustedResultResultAllOfEvidenceRatios**](BustedResultResultAllOfEvidenceRatios.md) |  | [optional] 

## Example

```python
from openapi_client.models.busted_result_result import BustedResultResult

# TODO update the JSON string below
json = "{}"
# create an instance of BustedResultResult from a JSON string
busted_result_result_instance = BustedResultResult.from_json(json)
# print the JSON string representation of the object
print(BustedResultResult.to_json())

# convert the object into a dict
busted_result_result_dict = busted_result_result_instance.to_dict()
# create an instance of BustedResultResult from a dict
busted_result_result_from_dict = BustedResultResult.from_dict(busted_result_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



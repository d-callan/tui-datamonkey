# MultihitResultResultAllOfTestResults

Statistical test results comparing different models

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**double_hit_vs_single_hit** | [**BustedResultResultAllOfTestResults**](BustedResultResultAllOfTestResults.md) |  | [optional] 
**triple_hit_vs_triple_hit_island** | [**BustedResultResultAllOfTestResults**](BustedResultResultAllOfTestResults.md) |  | [optional] 
**triple_hit_vs_double_hit** | [**BustedResultResultAllOfTestResults**](BustedResultResultAllOfTestResults.md) |  | [optional] 
**triple_hit_vs_single_hit** | [**BustedResultResultAllOfTestResults**](BustedResultResultAllOfTestResults.md) |  | [optional] 
**triple_hit_island_vs_double_hit** | [**BustedResultResultAllOfTestResults**](BustedResultResultAllOfTestResults.md) |  | [optional] 

## Example

```python
from openapi_client.models.multihit_result_result_all_of_test_results import MultihitResultResultAllOfTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of MultihitResultResultAllOfTestResults from a JSON string
multihit_result_result_all_of_test_results_instance = MultihitResultResultAllOfTestResults.from_json(json)
# print the JSON string representation of the object
print(MultihitResultResultAllOfTestResults.to_json())

# convert the object into a dict
multihit_result_result_all_of_test_results_dict = multihit_result_result_all_of_test_results_instance.to_dict()
# create an instance of MultihitResultResultAllOfTestResults from a dict
multihit_result_result_all_of_test_results_from_dict = MultihitResultResultAllOfTestResults.from_dict(multihit_result_result_all_of_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RelaxResultResultAllOfTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**p_value** | **float** |  | [optional] 
**relaxation_or_intensification_parameter** | **float** |  | [optional] 
**test** | **str** |  | [optional] 
**alternative** | **str** |  | [optional] 
**null** | **str** |  | [optional] 
**background** | **str** |  | [optional] 
**log_likelihood_ratio** | **float** |  | [optional] 
**degrees_of_freedom** | **int** |  | [optional] 
**branch_attributes** | **Dict[str, Dict[str, RelaxResultResultAllOfTestResultsBranchAttributesValueValue]]** |  | [optional] 

## Example

```python
from openapi_client.models.relax_result_result_all_of_test_results import RelaxResultResultAllOfTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of RelaxResultResultAllOfTestResults from a JSON string
relax_result_result_all_of_test_results_instance = RelaxResultResultAllOfTestResults.from_json(json)
# print the JSON string representation of the object
print(RelaxResultResultAllOfTestResults.to_json())

# convert the object into a dict
relax_result_result_all_of_test_results_dict = relax_result_result_all_of_test_results_instance.to_dict()
# create an instance of RelaxResultResultAllOfTestResults from a dict
relax_result_result_all_of_test_results_from_dict = RelaxResultResultAllOfTestResults.from_dict(relax_result_result_all_of_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



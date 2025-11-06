# AbsrelResultResultAllOfBranchAttributesAdditionalPropertiesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_name** | **str** |  | [optional] 
**nucleotide_gtr** | **float** |  | [optional] 
**baseline_mg94x_rev** | **float** |  | [optional] 
**baseline_mg94x_rev_omega_ratio** | **float** |  | [optional] 
**rate_classes** | **int** |  | [optional] 
**full_adaptive_model** | **float** |  | [optional] 
**rate_distributions** | **List[List[float]]** |  | [optional] 
**lrt** | **float** |  | [optional] 
**uncorrected_p_value** | **float** |  | [optional] 
**corrected_p_value** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.absrel_result_result_all_of_branch_attributes_additional_properties_value import AbsrelResultResultAllOfBranchAttributesAdditionalPropertiesValue

# TODO update the JSON string below
json = "{}"
# create an instance of AbsrelResultResultAllOfBranchAttributesAdditionalPropertiesValue from a JSON string
absrel_result_result_all_of_branch_attributes_additional_properties_value_instance = AbsrelResultResultAllOfBranchAttributesAdditionalPropertiesValue.from_json(json)
# print the JSON string representation of the object
print(AbsrelResultResultAllOfBranchAttributesAdditionalPropertiesValue.to_json())

# convert the object into a dict
absrel_result_result_all_of_branch_attributes_additional_properties_value_dict = absrel_result_result_all_of_branch_attributes_additional_properties_value_instance.to_dict()
# create an instance of AbsrelResultResultAllOfBranchAttributesAdditionalPropertiesValue from a dict
absrel_result_result_all_of_branch_attributes_additional_properties_value_from_dict = AbsrelResultResultAllOfBranchAttributesAdditionalPropertiesValue.from_dict(absrel_result_result_all_of_branch_attributes_additional_properties_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SlacResultResultAllOfBranchAttributesValueValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_name** | **str** |  | [optional] 
**nucleotide_gtr** | **float** |  | [optional] 
**global_mg94x_rev** | **float** |  | [optional] 
**codon** | **List[List[str]]** |  | [optional] 
**amino_acid** | **List[List[str]]** |  | [optional] 
**synonymous_substitution_count** | **List[List[float]]** |  | [optional] 
**nonsynonymous_substitution_count** | **List[List[float]]** |  | [optional] 

## Example

```python
from openapi_client.models.slac_result_result_all_of_branch_attributes_value_value import SlacResultResultAllOfBranchAttributesValueValue

# TODO update the JSON string below
json = "{}"
# create an instance of SlacResultResultAllOfBranchAttributesValueValue from a JSON string
slac_result_result_all_of_branch_attributes_value_value_instance = SlacResultResultAllOfBranchAttributesValueValue.from_json(json)
# print the JSON string representation of the object
print(SlacResultResultAllOfBranchAttributesValueValue.to_json())

# convert the object into a dict
slac_result_result_all_of_branch_attributes_value_value_dict = slac_result_result_all_of_branch_attributes_value_value_instance.to_dict()
# create an instance of SlacResultResultAllOfBranchAttributesValueValue from a dict
slac_result_result_all_of_branch_attributes_value_value_from_dict = SlacResultResultAllOfBranchAttributesValueValue.from_dict(slac_result_result_all_of_branch_attributes_value_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RelaxResultResultAllOfFits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nucleotide_gtr** | [**RelaxResultResultAllOfFitsNucleotideGTR**](RelaxResultResultAllOfFitsNucleotideGTR.md) |  | [optional] 
**mg94x_rev_with_separate_rates_for_branch_sets** | [**RelaxResultResultAllOfFitsMG94xREVWithSeparateRatesForBranchSets**](RelaxResultResultAllOfFitsMG94xREVWithSeparateRatesForBranchSets.md) |  | [optional] 
**general_descriptive** | [**RelaxResultResultAllOfFitsGeneralDescriptive**](RelaxResultResultAllOfFitsGeneralDescriptive.md) |  | [optional] 
**relax_alternative** | [**RelaxResultResultAllOfFitsRELAXAlternative**](RelaxResultResultAllOfFitsRELAXAlternative.md) |  | [optional] 
**relax_null** | [**RelaxResultResultAllOfFitsRELAXAlternative**](RelaxResultResultAllOfFitsRELAXAlternative.md) |  | [optional] 

## Example

```python
from openapi_client.models.relax_result_result_all_of_fits import RelaxResultResultAllOfFits

# TODO update the JSON string below
json = "{}"
# create an instance of RelaxResultResultAllOfFits from a JSON string
relax_result_result_all_of_fits_instance = RelaxResultResultAllOfFits.from_json(json)
# print the JSON string representation of the object
print(RelaxResultResultAllOfFits.to_json())

# convert the object into a dict
relax_result_result_all_of_fits_dict = relax_result_result_all_of_fits_instance.to_dict()
# create an instance of RelaxResultResultAllOfFits from a dict
relax_result_result_all_of_fits_from_dict = RelaxResultResultAllOfFits.from_dict(relax_result_result_all_of_fits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



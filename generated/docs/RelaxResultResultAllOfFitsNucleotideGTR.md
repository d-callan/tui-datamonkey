# RelaxResultResultAllOfFitsNucleotideGTR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_likelihood** | **float** |  | [optional] 
**estimated_parameters** | **int** |  | [optional] 
**aic_c** | **float** |  | [optional] 
**equilibrium_frequencies** | **List[List[float]]** |  | [optional] 
**rate_distributions** | **Dict[str, float]** |  | [optional] 
**display_order** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.relax_result_result_all_of_fits_nucleotide_gtr import RelaxResultResultAllOfFitsNucleotideGTR

# TODO update the JSON string below
json = "{}"
# create an instance of RelaxResultResultAllOfFitsNucleotideGTR from a JSON string
relax_result_result_all_of_fits_nucleotide_gtr_instance = RelaxResultResultAllOfFitsNucleotideGTR.from_json(json)
# print the JSON string representation of the object
print(RelaxResultResultAllOfFitsNucleotideGTR.to_json())

# convert the object into a dict
relax_result_result_all_of_fits_nucleotide_gtr_dict = relax_result_result_all_of_fits_nucleotide_gtr_instance.to_dict()
# create an instance of RelaxResultResultAllOfFitsNucleotideGTR from a dict
relax_result_result_all_of_fits_nucleotide_gtr_from_dict = RelaxResultResultAllOfFitsNucleotideGTR.from_dict(relax_result_result_all_of_fits_nucleotide_gtr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



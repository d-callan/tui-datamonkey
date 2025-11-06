# SlacResultResultAllOfFits

Model fitting information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nucleotide_gtr** | [**RelaxResultResultAllOfFitsNucleotideGTR**](RelaxResultResultAllOfFitsNucleotideGTR.md) |  | [optional] 
**global_mg94x_rev** | [**SlacResultResultAllOfFitsGlobalMG94xREV**](SlacResultResultAllOfFitsGlobalMG94xREV.md) |  | [optional] 

## Example

```python
from openapi_client.models.slac_result_result_all_of_fits import SlacResultResultAllOfFits

# TODO update the JSON string below
json = "{}"
# create an instance of SlacResultResultAllOfFits from a JSON string
slac_result_result_all_of_fits_instance = SlacResultResultAllOfFits.from_json(json)
# print the JSON string representation of the object
print(SlacResultResultAllOfFits.to_json())

# convert the object into a dict
slac_result_result_all_of_fits_dict = slac_result_result_all_of_fits_instance.to_dict()
# create an instance of SlacResultResultAllOfFits from a dict
slac_result_result_all_of_fits_from_dict = SlacResultResultAllOfFits.from_dict(slac_result_result_all_of_fits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



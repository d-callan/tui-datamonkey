# NrmResultResultAllOfFitsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aic_c** | **float** |  | [optional] 
**log_likelihood** | **float** |  | [optional] 
**rate_distributions** | **List[List[float]]** |  | [optional] 
**display_order** | **float** |  | [optional] 
**estimated_parameters** | **float** |  | [optional] 
**equilibrium_frequencies** | **List[List[float]]** |  | [optional] 

## Example

```python
from openapi_client.models.nrm_result_result_all_of_fits_value import NrmResultResultAllOfFitsValue

# TODO update the JSON string below
json = "{}"
# create an instance of NrmResultResultAllOfFitsValue from a JSON string
nrm_result_result_all_of_fits_value_instance = NrmResultResultAllOfFitsValue.from_json(json)
# print the JSON string representation of the object
print(NrmResultResultAllOfFitsValue.to_json())

# convert the object into a dict
nrm_result_result_all_of_fits_value_dict = nrm_result_result_all_of_fits_value_instance.to_dict()
# create an instance of NrmResultResultAllOfFitsValue from a dict
nrm_result_result_all_of_fits_value_from_dict = NrmResultResultAllOfFitsValue.from_dict(nrm_result_result_all_of_fits_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FadeResultResultAllOfFitsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_likelihood** | **float** | Log likelihood of the model fit | [optional] 
**estimated_parameters** | **int** | Number of estimated parameters | [optional] 
**aic_c** | **float** | AIC-c score for the model | [optional] 
**equilibrium_frequencies** | **List[List[float]]** | Equilibrium frequencies for the model | [optional] 
**rate_distributions** | **object** |  | [optional] 
**display_order** | **int** | Display order for the model | [optional] 

## Example

```python
from openapi_client.models.fade_result_result_all_of_fits_value import FadeResultResultAllOfFitsValue

# TODO update the JSON string below
json = "{}"
# create an instance of FadeResultResultAllOfFitsValue from a JSON string
fade_result_result_all_of_fits_value_instance = FadeResultResultAllOfFitsValue.from_json(json)
# print the JSON string representation of the object
print(FadeResultResultAllOfFitsValue.to_json())

# convert the object into a dict
fade_result_result_all_of_fits_value_dict = fade_result_result_all_of_fits_value_instance.to_dict()
# create an instance of FadeResultResultAllOfFitsValue from a dict
fade_result_result_all_of_fits_value_from_dict = FadeResultResultAllOfFitsValue.from_dict(fade_result_result_all_of_fits_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_token** | **str** | Token identifying the user who is starting the job | [optional] 
**alignment** | **str** |  | [optional] 
**tree** | **str** |  | [optional] 
**ci** | **str** | Compute confidence intervals for estimated rates | [optional] [default to 'No']
**srv** | **str** | Include synonymous rate variation in the model | [optional] [default to 'Yes']
**resample** | **float** | Number of bootstrap resamples | [optional] [default to 0]
**multiple_hits** | **str** | Specify handling of multiple nucleotide substitutions | [optional] [default to 'None']
**site_multihit** | **str** | Specify whether to estimate multiple hit rates for each site | [optional] [default to 'Estimate']
**genetic_code** | [**GeneticCode**](GeneticCode.md) |  | [optional] [default to GeneticCode.UNIVERSAL]
**branches** | **List[str]** | Branches to include in the analysis. If empty, all branches are included. | [optional] [default to []]

## Example

```python
from openapi_client.models.fel_request import FelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FelRequest from a JSON string
fel_request_instance = FelRequest.from_json(json)
# print the JSON string representation of the object
print(FelRequest.to_json())

# convert the object into a dict
fel_request_dict = fel_request_instance.to_dict()
# create an instance of FelRequest from a dict
fel_request_from_dict = FelRequest.from_dict(fel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



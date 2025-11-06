# MemeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_token** | **str** | Token identifying the user who is starting the job | [optional] 
**alignment** | **str** |  | [optional] 
**tree** | **str** |  | [optional] 
**genetic_code** | [**GeneticCode**](GeneticCode.md) |  | [optional] [default to GeneticCode.UNIVERSAL]
**multiple_hits** | **str** | Specify handling of multiple nucleotide substitutions | [optional] [default to 'None']
**site_multihit** | **str** | Specify whether to estimate multiple hit rates for each site | [optional] [default to 'Estimate']
**rates** | **int** | Number of different categories of non-synonymous rates | [optional] [default to 2]
**resample** | **float** | Number of bootstrapping replicates | [optional] [default to 0]
**impute_states** | **str** | Option to impute likely character states for missing data | [optional] [default to 'No']

## Example

```python
from openapi_client.models.meme_request import MemeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemeRequest from a JSON string
meme_request_instance = MemeRequest.from_json(json)
# print the JSON string representation of the object
print(MemeRequest.to_json())

# convert the object into a dict
meme_request_dict = meme_request_instance.to_dict()
# create an instance of MemeRequest from a dict
meme_request_from_dict = MemeRequest.from_dict(meme_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



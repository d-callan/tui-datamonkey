# BgmRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_token** | **str** | Token identifying the user who is starting the job | [optional] 
**alignment** | **str** |  | [optional] 
**tree** | **str** |  | [optional] 
**branches** | **str** | Specify branches to test | [optional] [default to 'All']
**genetic_code** | [**GeneticCode**](GeneticCode.md) |  | [optional] [default to GeneticCode.UNIVERSAL]
**data_type** | **str** | The type of data being analyzed | [optional] [default to 'codon']
**steps** | **int** | Number of MCMC steps to sample | [optional] [default to 100000]
**burn_in** | **int** | Number of MCMC steps to discard as burn-in | [optional] [default to 10000]
**samples** | **int** | Number of samples to extract from the chain | [optional] [default to 100]
**max_parents** | **int** | Maximum number of parents allowed per node | [optional] [default to 1]
**min_subs** | **int** | Minimum number of substitutions per site to include in the analysis | [optional] [default to 1]

## Example

```python
from openapi_client.models.bgm_request import BgmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BgmRequest from a JSON string
bgm_request_instance = BgmRequest.from_json(json)
# print the JSON string representation of the object
print(BgmRequest.to_json())

# convert the object into a dict
bgm_request_dict = bgm_request_instance.to_dict()
# create an instance of BgmRequest from a dict
bgm_request_from_dict = BgmRequest.from_dict(bgm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



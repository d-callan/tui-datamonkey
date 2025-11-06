# SlacRequest

Request parameters for SLAC (Single Likelihood Ancestor Counting) analysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_token** | **str** | Token identifying the user who is starting the job | [optional] 
**alignment** | **str** |  | [optional] 
**tree** | **str** |  | [optional] 
**genetic_code** | [**GeneticCode**](GeneticCode.md) |  | [optional] [default to GeneticCode.UNIVERSAL]
**branches** | **List[str]** | Branches to include in the analysis. If empty, all branches are included. | [optional] [default to []]
**samples** | **int** | Number of samples for ancestral reconstruction uncertainty | [optional] [default to 100]
**pvalue** | **float** | Threshold for statistical significance | [optional] [default to 0.1]

## Example

```python
from openapi_client.models.slac_request import SlacRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SlacRequest from a JSON string
slac_request_instance = SlacRequest.from_json(json)
# print the JSON string representation of the object
print(SlacRequest.to_json())

# convert the object into a dict
slac_request_dict = slac_request_instance.to_dict()
# create an instance of SlacRequest from a dict
slac_request_from_dict = SlacRequest.from_dict(slac_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



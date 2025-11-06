# BustedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_token** | **str** | Token identifying the user who is starting the job | [optional] 
**alignment** | **str** |  | [optional] 
**tree** | **str** |  | [optional] 
**srv** | **str** | Include synonymous rate variation in the model | [optional] [default to 'Yes']
**multiple_hits** | **str** | Specify handling of multiple nucleotide substitutions | [optional] [default to 'None']
**genetic_code** | [**GeneticCode**](GeneticCode.md) |  | [optional] [default to GeneticCode.UNIVERSAL]
**branches** | **List[str]** | Branches to include in the analysis. If empty, all branches are included. | [optional] [default to []]
**rates** | **int** | The number omega rate classes to include in the model | [optional] [default to 3]
**syn_rates** | **int** | The number synonymous rate classes to include in the model | [optional] [default to 3]
**grid_size** | **int** | The number of points in the initial distributional guess for likelihood fitting | [optional] [default to 250]
**starting_points** | **int** | The number of initial random guesses to seed rate values optimization | [optional] [default to 1]
**error_sink** | **str** | An advanced experimental setting; include a rate class to capture misalignment artifacts | [optional] [default to 'No']

## Example

```python
from openapi_client.models.busted_request import BustedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BustedRequest from a JSON string
busted_request_instance = BustedRequest.from_json(json)
# print the JSON string representation of the object
print(BustedRequest.to_json())

# convert the object into a dict
busted_request_dict = busted_request_instance.to_dict()
# create an instance of BustedRequest from a dict
busted_request_from_dict = BustedRequest.from_dict(busted_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



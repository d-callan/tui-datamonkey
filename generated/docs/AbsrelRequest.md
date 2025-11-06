# AbsrelRequest


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
**blb** | **float** | Bag of little bootstrap alignment resampling rate | [optional] [default to 1]

## Example

```python
from openapi_client.models.absrel_request import AbsrelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AbsrelRequest from a JSON string
absrel_request_instance = AbsrelRequest.from_json(json)
# print the JSON string representation of the object
print(AbsrelRequest.to_json())

# convert the object into a dict
absrel_request_dict = absrel_request_instance.to_dict()
# create an instance of AbsrelRequest from a dict
absrel_request_from_dict = AbsrelRequest.from_dict(absrel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



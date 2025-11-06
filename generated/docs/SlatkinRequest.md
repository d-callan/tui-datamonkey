# SlatkinRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_token** | **str** | Token identifying the user who is starting the job | [optional] 
**tree** | **str** |  | [optional] 
**groups** | **int** | The number of compartments/groups to test | [optional] [default to 2]
**compartment_definitions** | [**List[SlatkinRequestCompartmentDefinitionsInner]**](SlatkinRequestCompartmentDefinitionsInner.md) | Array of compartment definitions | [optional] 
**replicates** | **int** | The number of bootstrap replicates | [optional] [default to 1000]
**weight** | **float** | Probability of branch selection for structured permutation [0-1]; 0 &#x3D; classical Slatkin-Maddison, 1 &#x3D; fully structured | [optional] [default to 0.2]
**use_bootstrap** | **bool** | Whether to use bootstrap weights to respect well-supported clades | [optional] [default to True]

## Example

```python
from openapi_client.models.slatkin_request import SlatkinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SlatkinRequest from a JSON string
slatkin_request_instance = SlatkinRequest.from_json(json)
# print the JSON string representation of the object
print(SlatkinRequest.to_json())

# convert the object into a dict
slatkin_request_dict = slatkin_request_instance.to_dict()
# create an instance of SlatkinRequest from a dict
slatkin_request_from_dict = SlatkinRequest.from_dict(slatkin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



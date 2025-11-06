# FubarRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_token** | **str** | Token identifying the user who is starting the job | [optional] 
**alignment** | **str** |  | 
**tree** | **str** |  | 
**genetic_code** | **str** | Which genetic code should be used | [optional] [default to 'Universal']
**grid_points** | **int** | Number of grid points for the Bayesian analysis (must be between 5 and 50) | [optional] [default to 20]
**concentration_parameter** | **float** | Concentration parameter for the Dirichlet prior in the Bayesian estimation | [optional] [default to 0.5]

## Example

```python
from openapi_client.models.fubar_request import FubarRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FubarRequest from a JSON string
fubar_request_instance = FubarRequest.from_json(json)
# print the JSON string representation of the object
print(FubarRequest.to_json())

# convert the object into a dict
fubar_request_dict = fubar_request_instance.to_dict()
# create an instance of FubarRequest from a dict
fubar_request_from_dict = FubarRequest.from_dict(fubar_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# NrmRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_token** | **str** | Token identifying the user who is starting the job | [optional] 
**alignment** | **str** |  | [optional] 
**tree** | **str** |  | [optional] 
**genetic_code** | [**GeneticCode**](GeneticCode.md) |  | [optional] [default to GeneticCode.UNIVERSAL]
**save_fit** | **bool** | Save NRM+F model fit to a file | [optional] [default to False]

## Example

```python
from openapi_client.models.nrm_request import NrmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NrmRequest from a JSON string
nrm_request_instance = NrmRequest.from_json(json)
# print the JSON string representation of the object
print(NrmRequest.to_json())

# convert the object into a dict
nrm_request_dict = nrm_request_instance.to_dict()
# create an instance of NrmRequest from a dict
nrm_request_from_dict = NrmRequest.from_dict(nrm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



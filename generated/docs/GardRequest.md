# GardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_token** | **str** | Token identifying the user who is starting the job | [optional] 
**alignment** | **str** |  | [optional] 
**genetic_code** | [**GeneticCode**](GeneticCode.md) |  | [optional] [default to GeneticCode.UNIVERSAL]
**data_type** | **str** | The type of data being analyzed | [optional] [default to 'Nucleotide']
**run_mode** | **str** | The optimization mode | [optional] [default to 'Normal']
**site_to_site_variation** | **str** | Specifies the model for rate variation among sites | [optional] [default to 'None']
**rate_classes** | **int** | The number of discrete rate classes for rate variation | [optional] [default to 2]
**model** | **str** | The substitution model to use | [optional] [default to 'JTT']

## Example

```python
from openapi_client.models.gard_request import GardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GardRequest from a JSON string
gard_request_instance = GardRequest.from_json(json)
# print the JSON string representation of the object
print(GardRequest.to_json())

# convert the object into a dict
gard_request_dict = gard_request_instance.to_dict()
# create an instance of GardRequest from a dict
gard_request_from_dict = GardRequest.from_dict(gard_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



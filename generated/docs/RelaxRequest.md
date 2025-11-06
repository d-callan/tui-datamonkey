# RelaxRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_token** | **str** | Token identifying the user who is starting the job | [optional] 
**alignment** | **str** |  | [optional] 
**tree** | **str** |  | [optional] 
**genetic_code** | [**GeneticCode**](GeneticCode.md) |  | [optional] [default to GeneticCode.UNIVERSAL]
**test_branches** | **List[str]** | Branches to be considered as &#39;Test&#39; | [optional] [default to []]
**reference_branches** | **List[str]** | Branches to be considered as &#39;Reference&#39; | [optional] [default to []]
**models** | **str** | Type of analysis to run (All for descriptive models and RELAX test, Minimal for only the RELAX test) | [optional] [default to 'All']
**rates** | **int** | Number of omega rate classes | [optional] [default to 3]
**kill_zero_lengths** | **str** | Specify whether to handle zero-length branches | [optional] [default to 'No']

## Example

```python
from openapi_client.models.relax_request import RelaxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RelaxRequest from a JSON string
relax_request_instance = RelaxRequest.from_json(json)
# print the JSON string representation of the object
print(RelaxRequest.to_json())

# convert the object into a dict
relax_request_dict = relax_request_instance.to_dict()
# create an instance of RelaxRequest from a dict
relax_request_from_dict = RelaxRequest.from_dict(relax_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MultihitRequest

Request parameters for MULTI-HIT analysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_token** | **str** | Token identifying the user who is starting the job | [optional] 
**alignment** | **str** |  | 
**genetic_code** | **str** | The genetic code to use for the analysis | [default to 'Universal']
**triple_islands** | **str** | Toggle for accounting synonymous triple-hit substitutions | [optional] [default to 'No']
**rate_classes** | **int** | Number of rate classes to use | [optional] [default to 3]

## Example

```python
from openapi_client.models.multihit_request import MultihitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MultihitRequest from a JSON string
multihit_request_instance = MultihitRequest.from_json(json)
# print the JSON string representation of the object
print(MultihitRequest.to_json())

# convert the object into a dict
multihit_request_dict = multihit_request_instance.to_dict()
# create an instance of MultihitRequest from a dict
multihit_request_from_dict = MultihitRequest.from_dict(multihit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



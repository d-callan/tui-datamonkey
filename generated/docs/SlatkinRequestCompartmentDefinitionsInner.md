# SlatkinRequestCompartmentDefinitionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description for sequences in this compartment | 
**regexp** | **str** | Regular expression to select the branches in this compartment | 

## Example

```python
from openapi_client.models.slatkin_request_compartment_definitions_inner import SlatkinRequestCompartmentDefinitionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SlatkinRequestCompartmentDefinitionsInner from a JSON string
slatkin_request_compartment_definitions_inner_instance = SlatkinRequestCompartmentDefinitionsInner.from_json(json)
# print the JSON string representation of the object
print(SlatkinRequestCompartmentDefinitionsInner.to_json())

# convert the object into a dict
slatkin_request_compartment_definitions_inner_dict = slatkin_request_compartment_definitions_inner_instance.to_dict()
# create an instance of SlatkinRequestCompartmentDefinitionsInner from a dict
slatkin_request_compartment_definitions_inner_from_dict = SlatkinRequestCompartmentDefinitionsInner.from_dict(slatkin_request_compartment_definitions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



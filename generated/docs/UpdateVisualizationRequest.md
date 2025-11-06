# UpdateVisualizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Updated title of the visualization | [optional] 
**description** | **str** | Updated description | [optional] 
**spec** | **Dict[str, object]** | Updated Vega-Lite visualization specification | [optional] 
**config** | **Dict[str, object]** | Updated configuration options | [optional] 
**metadata** | **Dict[str, object]** | Updated metadata | [optional] 

## Example

```python
from openapi_client.models.update_visualization_request import UpdateVisualizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVisualizationRequest from a JSON string
update_visualization_request_instance = UpdateVisualizationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateVisualizationRequest.to_json())

# convert the object into a dict
update_visualization_request_dict = update_visualization_request_instance.to_dict()
# create an instance of UpdateVisualizationRequest from a dict
update_visualization_request_from_dict = UpdateVisualizationRequest.from_dict(update_visualization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



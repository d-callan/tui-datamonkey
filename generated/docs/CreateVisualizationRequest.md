# CreateVisualizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Job ID to associate with this visualization | 
**dataset_id** | **str** | Dataset ID to associate with this visualization (optional) | [optional] 
**title** | **str** | Title of the visualization | 
**description** | **str** | Description of what the visualization shows | [optional] 
**spec** | **Dict[str, object]** | The Vega-Lite visualization specification | 
**config** | **Dict[str, object]** | Additional configuration options | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata about the visualization | [optional] 

## Example

```python
from openapi_client.models.create_visualization_request import CreateVisualizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVisualizationRequest from a JSON string
create_visualization_request_instance = CreateVisualizationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateVisualizationRequest.to_json())

# convert the object into a dict
create_visualization_request_dict = create_visualization_request_instance.to_dict()
# create an instance of CreateVisualizationRequest from a dict
create_visualization_request_from_dict = CreateVisualizationRequest.from_dict(create_visualization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



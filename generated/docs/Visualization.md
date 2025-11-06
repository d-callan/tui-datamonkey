# Visualization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**viz_id** | **str** | Unique identifier for the visualization | 
**job_id** | **str** | Job ID associated with this visualization | 
**dataset_id** | **str** | Dataset ID associated with this visualization (optional) | [optional] 
**title** | **str** | Title of the visualization | 
**description** | **str** | Description of what the visualization shows | [optional] 
**spec** | **Dict[str, object]** | The Vega-Lite visualization specification | 
**config** | **Dict[str, object]** | Additional configuration options | [optional] 
**metadata** | [**VisualizationMetadata**](VisualizationMetadata.md) |  | [optional] 
**created_at** | **datetime** | Timestamp when the visualization was created | [optional] 
**updated_at** | **datetime** | Timestamp when the visualization was last updated | [optional] 

## Example

```python
from openapi_client.models.visualization import Visualization

# TODO update the JSON string below
json = "{}"
# create an instance of Visualization from a JSON string
visualization_instance = Visualization.from_json(json)
# print the JSON string representation of the object
print(Visualization.to_json())

# convert the object into a dict
visualization_dict = visualization_instance.to_dict()
# create an instance of Visualization from a dict
visualization_from_dict = Visualization.from_dict(visualization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



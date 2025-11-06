# VisualizationMetadata

Additional metadata about the visualization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**library** | **str** | Visualization library used | [optional] 
**generated_by** | **str** | Tool or method that generated this visualization | [optional] 
**prompt** | **str** | Original prompt used to generate the visualization | [optional] 

## Example

```python
from openapi_client.models.visualization_metadata import VisualizationMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of VisualizationMetadata from a JSON string
visualization_metadata_instance = VisualizationMetadata.from_json(json)
# print the JSON string representation of the object
print(VisualizationMetadata.to_json())

# convert the object into a dict
visualization_metadata_dict = visualization_metadata_instance.to_dict()
# create an instance of VisualizationMetadata from a dict
visualization_metadata_from_dict = VisualizationMetadata.from_dict(visualization_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



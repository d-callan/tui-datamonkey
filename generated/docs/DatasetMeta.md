# DatasetMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dataset_meta import DatasetMeta

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetMeta from a JSON string
dataset_meta_instance = DatasetMeta.from_json(json)
# print the JSON string representation of the object
print(DatasetMeta.to_json())

# convert the object into a dict
dataset_meta_dict = dataset_meta_instance.to_dict()
# create an instance of DatasetMeta from a dict
dataset_meta_from_dict = DatasetMeta.from_dict(dataset_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



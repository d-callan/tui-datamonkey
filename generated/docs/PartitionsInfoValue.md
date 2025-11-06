# PartitionsInfoValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**coverage** | **List[List[int]]** |  | [optional] 

## Example

```python
from openapi_client.models.partitions_info_value import PartitionsInfoValue

# TODO update the JSON string below
json = "{}"
# create an instance of PartitionsInfoValue from a JSON string
partitions_info_value_instance = PartitionsInfoValue.from_json(json)
# print the JSON string representation of the object
print(PartitionsInfoValue.to_json())

# convert the object into a dict
partitions_info_value_dict = partitions_info_value_instance.to_dict()
# create an instance of PartitionsInfoValue from a dict
partitions_info_value_from_dict = PartitionsInfoValue.from_dict(partitions_info_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



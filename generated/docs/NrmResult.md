# NrmResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**result** | [**NrmResultResult**](NrmResultResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.nrm_result import NrmResult

# TODO update the JSON string below
json = "{}"
# create an instance of NrmResult from a JSON string
nrm_result_instance = NrmResult.from_json(json)
# print the JSON string representation of the object
print(NrmResult.to_json())

# convert the object into a dict
nrm_result_dict = nrm_result_instance.to_dict()
# create an instance of NrmResult from a dict
nrm_result_from_dict = NrmResult.from_dict(nrm_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



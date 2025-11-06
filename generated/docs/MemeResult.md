# MemeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**result** | [**FelResultResult**](FelResultResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.meme_result import MemeResult

# TODO update the JSON string below
json = "{}"
# create an instance of MemeResult from a JSON string
meme_result_instance = MemeResult.from_json(json)
# print the JSON string representation of the object
print(MemeResult.to_json())

# convert the object into a dict
meme_result_dict = meme_result_instance.to_dict()
# create an instance of MemeResult from a dict
meme_result_from_dict = MemeResult.from_dict(meme_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



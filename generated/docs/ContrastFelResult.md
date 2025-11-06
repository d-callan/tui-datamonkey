# ContrastFelResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**result** | [**ContrastFelResultResult**](ContrastFelResultResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.contrast_fel_result import ContrastFelResult

# TODO update the JSON string below
json = "{}"
# create an instance of ContrastFelResult from a JSON string
contrast_fel_result_instance = ContrastFelResult.from_json(json)
# print the JSON string representation of the object
print(ContrastFelResult.to_json())

# convert the object into a dict
contrast_fel_result_dict = contrast_fel_result_instance.to_dict()
# create an instance of ContrastFelResult from a dict
contrast_fel_result_from_dict = ContrastFelResult.from_dict(contrast_fel_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



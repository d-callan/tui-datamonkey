# SlacResultResultAllOfMLE

Maximum likelihood estimates for site-specific results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **List[List[str]]** | Headers describing the columns in the content array | [optional] 
**content** | **Dict[str, List[List[float]]]** | Site-specific results with statistical values | [optional] 

## Example

```python
from openapi_client.models.slac_result_result_all_of_mle import SlacResultResultAllOfMLE

# TODO update the JSON string below
json = "{}"
# create an instance of SlacResultResultAllOfMLE from a JSON string
slac_result_result_all_of_mle_instance = SlacResultResultAllOfMLE.from_json(json)
# print the JSON string representation of the object
print(SlacResultResultAllOfMLE.to_json())

# convert the object into a dict
slac_result_result_all_of_mle_dict = slac_result_result_all_of_mle_instance.to_dict()
# create an instance of SlacResultResultAllOfMLE from a dict
slac_result_result_all_of_mle_from_dict = SlacResultResultAllOfMLE.from_dict(slac_result_result_all_of_mle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



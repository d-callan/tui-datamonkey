# BgmResultResultAllOfMLE

Maximum likelihood estimates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **List[List[str]]** | Column headers for the content array | [optional] 
**content** | **List[List[float]]** | Site pair data with correlation values | [optional] 

## Example

```python
from openapi_client.models.bgm_result_result_all_of_mle import BgmResultResultAllOfMLE

# TODO update the JSON string below
json = "{}"
# create an instance of BgmResultResultAllOfMLE from a JSON string
bgm_result_result_all_of_mle_instance = BgmResultResultAllOfMLE.from_json(json)
# print the JSON string representation of the object
print(BgmResultResultAllOfMLE.to_json())

# convert the object into a dict
bgm_result_result_all_of_mle_dict = bgm_result_result_all_of_mle_instance.to_dict()
# create an instance of BgmResultResultAllOfMLE from a dict
bgm_result_result_all_of_mle_from_dict = BgmResultResultAllOfMLE.from_dict(bgm_result_result_all_of_mle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



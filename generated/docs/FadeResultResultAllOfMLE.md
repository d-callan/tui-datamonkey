# FadeResultResultAllOfMLE

Maximum likelihood estimates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **List[List[str]]** | Column headers for the MLE data | [optional] 
**content** | **Dict[str, Dict[str, List[List[float]]]]** | MLE content organized by amino acid and partition | [optional] 

## Example

```python
from openapi_client.models.fade_result_result_all_of_mle import FadeResultResultAllOfMLE

# TODO update the JSON string below
json = "{}"
# create an instance of FadeResultResultAllOfMLE from a JSON string
fade_result_result_all_of_mle_instance = FadeResultResultAllOfMLE.from_json(json)
# print the JSON string representation of the object
print(FadeResultResultAllOfMLE.to_json())

# convert the object into a dict
fade_result_result_all_of_mle_dict = fade_result_result_all_of_mle_instance.to_dict()
# create an instance of FadeResultResultAllOfMLE from a dict
fade_result_result_all_of_mle_from_dict = FadeResultResultAllOfMLE.from_dict(fade_result_result_all_of_mle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



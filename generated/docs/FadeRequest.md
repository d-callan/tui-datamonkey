# FadeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_token** | **str** | Token identifying the user who is starting the job | [optional] 
**alignment** | **str** |  | [optional] 
**tree** | **str** |  | [optional] 
**bayes_factor_threshold** | **int** | Bayes Factor threshold for determining significant sites (default 100) | [optional] [default to 100]

## Example

```python
from openapi_client.models.fade_request import FadeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FadeRequest from a JSON string
fade_request_instance = FadeRequest.from_json(json)
# print the JSON string representation of the object
print(FadeRequest.to_json())

# convert the object into a dict
fade_request_dict = fade_request_instance.to_dict()
# create an instance of FadeRequest from a dict
fade_request_from_dict = FadeRequest.from_dict(fade_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



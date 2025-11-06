# AnalysisInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | **str** | User email address | [optional] 
**settings** | [**AnalysisInfoSettings**](AnalysisInfoSettings.md) |  | [optional] 

## Example

```python
from openapi_client.models.analysis_info import AnalysisInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisInfo from a JSON string
analysis_info_instance = AnalysisInfo.from_json(json)
# print the JSON string representation of the object
print(AnalysisInfo.to_json())

# convert the object into a dict
analysis_info_dict = analysis_info_instance.to_dict()
# create an instance of AnalysisInfo from a dict
analysis_info_from_dict = AnalysisInfo.from_dict(analysis_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



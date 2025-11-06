# HealthDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_scheduler** | [**Status**](Status.md) |  | [optional] 
**datamonkey** | [**Status**](Status.md) |  | [optional] 
**llm** | [**Status**](Status.md) |  | [optional] 
**database** | [**Status**](Status.md) |  | [optional] 

## Example

```python
from openapi_client.models.health_details import HealthDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HealthDetails from a JSON string
health_details_instance = HealthDetails.from_json(json)
# print the JSON string representation of the object
print(HealthDetails.to_json())

# convert the object into a dict
health_details_dict = health_details_instance.to_dict()
# create an instance of HealthDetails from a dict
health_details_from_dict = HealthDetails.from_dict(health_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FadeResultResultAllOfSiteAnnotations

Annotations for each site

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | [**FadeResultResultAllOfSiteAnnotationsHeaders**](FadeResultResultAllOfSiteAnnotationsHeaders.md) |  | [optional] 
**site_annotations** | **Dict[str, List[List[str]]]** | Site annotations by partition | [optional] 

## Example

```python
from openapi_client.models.fade_result_result_all_of_site_annotations import FadeResultResultAllOfSiteAnnotations

# TODO update the JSON string below
json = "{}"
# create an instance of FadeResultResultAllOfSiteAnnotations from a JSON string
fade_result_result_all_of_site_annotations_instance = FadeResultResultAllOfSiteAnnotations.from_json(json)
# print the JSON string representation of the object
print(FadeResultResultAllOfSiteAnnotations.to_json())

# convert the object into a dict
fade_result_result_all_of_site_annotations_dict = fade_result_result_all_of_site_annotations_instance.to_dict()
# create an instance of FadeResultResultAllOfSiteAnnotations from a dict
fade_result_result_all_of_site_annotations_from_dict = FadeResultResultAllOfSiteAnnotations.from_dict(fade_result_result_all_of_site_annotations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



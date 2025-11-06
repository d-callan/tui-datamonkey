# MultihitResultResultAllOfEvidenceRatios

Evidence ratios for different substitution types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**three_hit** | **List[List[float]]** | Evidence ratios for three-hit substitutions | [optional] 
**two_hit** | **List[List[float]]** | Evidence ratios for two-hit substitutions | [optional] 
**three_hit_islands_vs_2_hit** | **List[List[float]]** | Evidence ratios comparing three-hit islands vs two-hit substitutions | [optional] 

## Example

```python
from openapi_client.models.multihit_result_result_all_of_evidence_ratios import MultihitResultResultAllOfEvidenceRatios

# TODO update the JSON string below
json = "{}"
# create an instance of MultihitResultResultAllOfEvidenceRatios from a JSON string
multihit_result_result_all_of_evidence_ratios_instance = MultihitResultResultAllOfEvidenceRatios.from_json(json)
# print the JSON string representation of the object
print(MultihitResultResultAllOfEvidenceRatios.to_json())

# convert the object into a dict
multihit_result_result_all_of_evidence_ratios_dict = multihit_result_result_all_of_evidence_ratios_instance.to_dict()
# create an instance of MultihitResultResultAllOfEvidenceRatios from a dict
multihit_result_result_all_of_evidence_ratios_from_dict = MultihitResultResultAllOfEvidenceRatios.from_dict(multihit_result_result_all_of_evidence_ratios_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



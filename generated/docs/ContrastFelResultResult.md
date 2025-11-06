# ContrastFelResultResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**AnalysisInfo**](AnalysisInfo.md) |  | [optional] 
**input** | [**InputInfo**](InputInfo.md) |  | [optional] 
**tested** | **Dict[str, str]** | Mapping of branch names to their test groups (e.g., \&quot;TREATED\&quot;, \&quot;NAIVE\&quot;, \&quot;background\&quot;) | [optional] 
**timers** | [**Dict[str, TimersInfoValue]**](TimersInfoValue.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**data_partitions** | [**Dict[str, PartitionsInfoValue]**](PartitionsInfoValue.md) |  | [optional] 
**mle** | [**ContrastFelResultResultAllOfMLE**](ContrastFelResultResultAllOfMLE.md) |  | [optional] 
**branch_attributes** | **Dict[str, object]** | Attributes for each branch in the phylogenetic tree | [optional] 
**fits** | **Dict[str, object]** | Model fit statistics | [optional] 

## Example

```python
from openapi_client.models.contrast_fel_result_result import ContrastFelResultResult

# TODO update the JSON string below
json = "{}"
# create an instance of ContrastFelResultResult from a JSON string
contrast_fel_result_result_instance = ContrastFelResultResult.from_json(json)
# print the JSON string representation of the object
print(ContrastFelResultResult.to_json())

# convert the object into a dict
contrast_fel_result_result_dict = contrast_fel_result_result_instance.to_dict()
# create an instance of ContrastFelResultResult from a dict
contrast_fel_result_result_from_dict = ContrastFelResultResult.from_dict(contrast_fel_result_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



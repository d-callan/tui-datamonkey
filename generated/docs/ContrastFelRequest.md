# ContrastFelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_token** | **str** | Token identifying the user who is starting the job | [optional] 
**alignment** | **str** |  | 
**tree** | **str** |  | 
**branch_sets** | **List[str]** | Array of branch sets to be used for comparison (e.g., \&quot;Source\&quot; and \&quot;Test\&quot; groups) | 
**genetic_code** | **str** | Which genetic code should be used | [optional] [default to 'Universal']
**srv** | **str** | Include synonymous rate variation in the model (\&quot;Yes\&quot; or \&quot;No\&quot;) | [optional] [default to 'Yes']
**permutations** | **str** | Perform permutation significance tests (\&quot;Yes\&quot; or \&quot;No\&quot;) | [optional] [default to 'Yes']
**p_value** | **float** | Significance value for site tests | [optional] [default to 0.05]
**q_value** | **float** | Significance value for False Discovery Rate reporting | [optional] [default to 0.2]

## Example

```python
from openapi_client.models.contrast_fel_request import ContrastFelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContrastFelRequest from a JSON string
contrast_fel_request_instance = ContrastFelRequest.from_json(json)
# print the JSON string representation of the object
print(ContrastFelRequest.to_json())

# convert the object into a dict
contrast_fel_request_dict = contrast_fel_request_instance.to_dict()
# create an instance of ContrastFelRequest from a dict
contrast_fel_request_from_dict = ContrastFelRequest.from_dict(contrast_fel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TopicResponse

TopicResponse for returning topics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**repo_count** | **int** |  | [optional] 
**topic_name** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.topic_response import TopicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TopicResponse from a JSON string
topic_response_instance = TopicResponse.from_json(json)
# print the JSON string representation of the object
print TopicResponse.to_json()

# convert the object into a dict
topic_response_dict = topic_response_instance.to_dict()
# create an instance of TopicResponse from a dict
topic_response_form_dict = topic_response.from_dict(topic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



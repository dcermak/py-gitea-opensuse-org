# TopicResponse

TopicResponse for returning topics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | The date and time when the topic was created | [optional] 
**id** | **int** | The unique identifier of the topic | [optional] 
**repo_count** | **int** | The number of repositories using this topic | [optional] 
**topic_name** | **str** | The name of the topic | [optional] 
**updated** | **datetime** | The date and time when the topic was last updated | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.topic_response import TopicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TopicResponse from a JSON string
topic_response_instance = TopicResponse.from_json(json)
# print the JSON string representation of the object
print(TopicResponse.to_json())

# convert the object into a dict
topic_response_dict = topic_response_instance.to_dict()
# create an instance of TopicResponse from a dict
topic_response_from_dict = TopicResponse.from_dict(topic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Package

Package represents a package

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**creator** | [**User**](User.md) |  | [optional] 
**html_url** | **str** | The HTML URL to view the package | [optional] 
**id** | **int** | The unique identifier of the package | [optional] 
**name** | **str** | The name of the package | [optional] 
**owner** | [**User**](User.md) |  | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**type** | **str** | The type of the package (e.g., npm, maven, docker) | [optional] 
**version** | **str** | The version of the package | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.package import Package

# TODO update the JSON string below
json = "{}"
# create an instance of Package from a JSON string
package_instance = Package.from_json(json)
# print the JSON string representation of the object
print(Package.to_json())

# convert the object into a dict
package_dict = package_instance.to_dict()
# create an instance of Package from a dict
package_from_dict = Package.from_dict(package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



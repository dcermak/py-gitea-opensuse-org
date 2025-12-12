# PackageFile

PackageFile represents a package file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the package file | [optional] 
**md5** | **str** | The MD5 hash of the package file | [optional] 
**name** | **str** | The name of the package file | [optional] 
**sha1** | **str** | The SHA1 hash of the package file | [optional] 
**sha256** | **str** | The SHA256 hash of the package file | [optional] 
**sha512** | **str** | The SHA512 hash of the package file | [optional] 
**size** | **int** | The size of the package file in bytes | [optional] 

## Example

```python
from py_gitea_opensuse_org.models.package_file import PackageFile

# TODO update the JSON string below
json = "{}"
# create an instance of PackageFile from a JSON string
package_file_instance = PackageFile.from_json(json)
# print the JSON string representation of the object
print(PackageFile.to_json())

# convert the object into a dict
package_file_dict = package_file_instance.to_dict()
# create an instance of PackageFile from a dict
package_file_from_dict = PackageFile.from_dict(package_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



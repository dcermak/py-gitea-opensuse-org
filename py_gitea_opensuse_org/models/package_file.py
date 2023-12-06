# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.21.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PackageFile(BaseModel):
    """
    PackageFile represents a package file
    """ # noqa: E501
    size: Optional[StrictInt] = Field(default=None, alias="Size")
    id: Optional[StrictInt] = None
    md5: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    sha1: Optional[StrictStr] = None
    sha256: Optional[StrictStr] = None
    sha512: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["Size", "id", "md5", "name", "sha1", "sha256", "sha512"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PackageFile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PackageFile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Size": obj.get("Size"),
            "id": obj.get("id"),
            "md5": obj.get("md5"),
            "name": obj.get("name"),
            "sha1": obj.get("sha1"),
            "sha256": obj.get("sha256"),
            "sha512": obj.get("sha512")
        })
        return _obj



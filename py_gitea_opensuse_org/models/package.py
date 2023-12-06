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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from py_gitea_opensuse_org.models.repository import Repository
from py_gitea_opensuse_org.models.user import User
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Package(BaseModel):
    """
    Package represents a package
    """ # noqa: E501
    created_at: Optional[datetime] = None
    creator: Optional[User] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    owner: Optional[User] = None
    repository: Optional[Repository] = None
    type: Optional[StrictStr] = None
    version: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["created_at", "creator", "html_url", "id", "name", "owner", "repository", "type", "version"]

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
        """Create an instance of Package from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of repository
        if self.repository:
            _dict['repository'] = self.repository.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Package from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "creator": User.from_dict(obj.get("creator")) if obj.get("creator") is not None else None,
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "owner": User.from_dict(obj.get("owner")) if obj.get("owner") is not None else None,
            "repository": Repository.from_dict(obj.get("repository")) if obj.get("repository") is not None else None,
            "type": obj.get("type"),
            "version": obj.get("version")
        })
        return _obj



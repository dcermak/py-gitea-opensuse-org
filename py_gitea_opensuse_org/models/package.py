# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr
from py_gitea_opensuse_org.models.repository import Repository
from py_gitea_opensuse_org.models.user import User

class Package(BaseModel):
    """
    Package represents a package
    """
    created_at: Optional[datetime] = None
    creator: Optional[User] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    owner: Optional[User] = None
    repository: Optional[Repository] = None
    type: Optional[StrictStr] = None
    version: Optional[StrictStr] = None
    __properties = ["created_at", "creator", "id", "name", "owner", "repository", "type", "version"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Package:
        """Create an instance of Package from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
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
    def from_dict(cls, obj: dict) -> Package:
        """Create an instance of Package from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Package.parse_obj(obj)

        _obj = Package.parse_obj({
            "created_at": obj.get("created_at"),
            "creator": User.from_dict(obj.get("creator")) if obj.get("creator") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "owner": User.from_dict(obj.get("owner")) if obj.get("owner") is not None else None,
            "repository": Repository.from_dict(obj.get("repository")) if obj.get("repository") is not None else None,
            "type": obj.get("type"),
            "version": obj.get("version")
        })
        return _obj


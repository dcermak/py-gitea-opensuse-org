# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.19.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from py_gitea_opensuse_org.models.user import User

class PublicKey(BaseModel):
    """
    PublicKey publickey is a user key to push code to repository  # noqa: E501
    """
    created_at: Optional[datetime] = None
    fingerprint: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    key: Optional[StrictStr] = None
    key_type: Optional[StrictStr] = None
    read_only: Optional[StrictBool] = None
    title: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    user: Optional[User] = None
    __properties = ["created_at", "fingerprint", "id", "key", "key_type", "read_only", "title", "url", "user"]

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
    def from_json(cls, json_str: str) -> PublicKey:
        """Create an instance of PublicKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PublicKey:
        """Create an instance of PublicKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PublicKey.parse_obj(obj)

        _obj = PublicKey.parse_obj({
            "created_at": obj.get("created_at"),
            "fingerprint": obj.get("fingerprint"),
            "id": obj.get("id"),
            "key": obj.get("key"),
            "key_type": obj.get("key_type"),
            "read_only": obj.get("read_only"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "user": User.from_dict(obj.get("user")) if obj.get("user") is not None else None
        })
        return _obj



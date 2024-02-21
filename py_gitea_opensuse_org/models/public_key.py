# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.21.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_gitea_opensuse_org.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class PublicKey(BaseModel):
    """
    PublicKey publickey is a user key to push code to repository
    """ # noqa: E501
    created_at: Optional[datetime] = None
    fingerprint: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    key: Optional[StrictStr] = None
    key_type: Optional[StrictStr] = None
    read_only: Optional[StrictBool] = None
    title: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    user: Optional[User] = None
    __properties: ClassVar[List[str]] = ["created_at", "fingerprint", "id", "key", "key_type", "read_only", "title", "url", "user"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PublicKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "fingerprint": obj.get("fingerprint"),
            "id": obj.get("id"),
            "key": obj.get("key"),
            "key_type": obj.get("key_type"),
            "read_only": obj.get("read_only"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "user": User.from_dict(obj["user"]) if obj.get("user") is not None else None
        })
        return _obj



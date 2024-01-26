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
from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_gitea_opensuse_org.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class CommitStatus(BaseModel):
    """
    CommitStatus holds a single status of a single Commit
    """ # noqa: E501
    context: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    creator: Optional[User] = None
    description: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    status: Optional[StrictStr] = Field(default=None, description="CommitStatusState holds the state of a CommitStatus It can be \"pending\", \"success\", \"error\" and \"failure\"")
    target_url: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["context", "created_at", "creator", "description", "id", "status", "target_url", "updated_at", "url"]

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
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CommitStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommitStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "context": obj.get("context"),
            "created_at": obj.get("created_at"),
            "creator": User.from_dict(obj["creator"]) if obj.get("creator") is not None else None,
            "description": obj.get("description"),
            "id": obj.get("id"),
            "status": obj.get("status"),
            "target_url": obj.get("target_url"),
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url")
        })
        return _obj



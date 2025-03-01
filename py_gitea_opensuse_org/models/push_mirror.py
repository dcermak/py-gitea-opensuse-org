# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.23.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PushMirror(BaseModel):
    """
    PushMirror represents information of a push mirror
    """ # noqa: E501
    created: Optional[datetime] = None
    interval: Optional[StrictStr] = None
    last_error: Optional[StrictStr] = None
    last_update: Optional[datetime] = None
    remote_address: Optional[StrictStr] = None
    remote_name: Optional[StrictStr] = None
    repo_name: Optional[StrictStr] = None
    sync_on_commit: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["created", "interval", "last_error", "last_update", "remote_address", "remote_name", "repo_name", "sync_on_commit"]

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
        """Create an instance of PushMirror from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PushMirror from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created": obj.get("created"),
            "interval": obj.get("interval"),
            "last_error": obj.get("last_error"),
            "last_update": obj.get("last_update"),
            "remote_address": obj.get("remote_address"),
            "remote_name": obj.get("remote_name"),
            "repo_name": obj.get("repo_name"),
            "sync_on_commit": obj.get("sync_on_commit")
        })
        return _obj



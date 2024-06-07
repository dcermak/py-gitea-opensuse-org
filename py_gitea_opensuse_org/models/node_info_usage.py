# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from py_gitea_opensuse_org.models.node_info_usage_users import NodeInfoUsageUsers
from typing import Optional, Set
from typing_extensions import Self

class NodeInfoUsage(BaseModel):
    """
    NodeInfoUsage contains usage statistics for this server
    """ # noqa: E501
    local_comments: Optional[StrictInt] = Field(default=None, alias="localComments")
    local_posts: Optional[StrictInt] = Field(default=None, alias="localPosts")
    users: Optional[NodeInfoUsageUsers] = None
    __properties: ClassVar[List[str]] = ["localComments", "localPosts", "users"]

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
        """Create an instance of NodeInfoUsage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of users
        if self.users:
            _dict['users'] = self.users.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodeInfoUsage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "localComments": obj.get("localComments"),
            "localPosts": obj.get("localPosts"),
            "users": NodeInfoUsageUsers.from_dict(obj["users"]) if obj.get("users") is not None else None
        })
        return _obj



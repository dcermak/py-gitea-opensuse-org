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
from py_gitea_opensuse_org.models.comment import Comment
from py_gitea_opensuse_org.models.repository import Repository
from py_gitea_opensuse_org.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class Activity(BaseModel):
    """
    Activity
    """ # noqa: E501
    act_user: Optional[User] = None
    act_user_id: Optional[StrictInt] = None
    comment: Optional[Comment] = None
    comment_id: Optional[StrictInt] = None
    content: Optional[StrictStr] = None
    created: Optional[datetime] = None
    id: Optional[StrictInt] = None
    is_private: Optional[StrictBool] = None
    op_type: Optional[StrictStr] = None
    ref_name: Optional[StrictStr] = None
    repo: Optional[Repository] = None
    repo_id: Optional[StrictInt] = None
    user_id: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["act_user", "act_user_id", "comment", "comment_id", "content", "created", "id", "is_private", "op_type", "ref_name", "repo", "repo_id", "user_id"]

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
        """Create an instance of Activity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of act_user
        if self.act_user:
            _dict['act_user'] = self.act_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of comment
        if self.comment:
            _dict['comment'] = self.comment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of repo
        if self.repo:
            _dict['repo'] = self.repo.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Activity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "act_user": User.from_dict(obj["act_user"]) if obj.get("act_user") is not None else None,
            "act_user_id": obj.get("act_user_id"),
            "comment": Comment.from_dict(obj["comment"]) if obj.get("comment") is not None else None,
            "comment_id": obj.get("comment_id"),
            "content": obj.get("content"),
            "created": obj.get("created"),
            "id": obj.get("id"),
            "is_private": obj.get("is_private"),
            "op_type": obj.get("op_type"),
            "ref_name": obj.get("ref_name"),
            "repo": Repository.from_dict(obj["repo"]) if obj.get("repo") is not None else None,
            "repo_id": obj.get("repo_id"),
            "user_id": obj.get("user_id")
        })
        return _obj



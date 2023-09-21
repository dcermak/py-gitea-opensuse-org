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
from typing import List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, conlist
from py_gitea_opensuse_org.models.attachment import Attachment
from py_gitea_opensuse_org.models.user import User

class Comment(BaseModel):
    """
    Comment represents a comment on a commit or issue  # noqa: E501
    """
    assets: Optional[conlist(Attachment)] = None
    body: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    issue_url: Optional[StrictStr] = None
    original_author: Optional[StrictStr] = None
    original_author_id: Optional[StrictInt] = None
    pull_request_url: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    user: Optional[User] = None
    __properties = ["assets", "body", "created_at", "html_url", "id", "issue_url", "original_author", "original_author_id", "pull_request_url", "updated_at", "user"]

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
    def from_json(cls, json_str: str) -> Comment:
        """Create an instance of Comment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in assets (list)
        _items = []
        if self.assets:
            for _item in self.assets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['assets'] = _items
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Comment:
        """Create an instance of Comment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Comment.parse_obj(obj)

        _obj = Comment.parse_obj({
            "assets": [Attachment.from_dict(_item) for _item in obj.get("assets")] if obj.get("assets") is not None else None,
            "body": obj.get("body"),
            "created_at": obj.get("created_at"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "issue_url": obj.get("issue_url"),
            "original_author": obj.get("original_author"),
            "original_author_id": obj.get("original_author_id"),
            "pull_request_url": obj.get("pull_request_url"),
            "updated_at": obj.get("updated_at"),
            "user": User.from_dict(obj.get("user")) if obj.get("user") is not None else None
        })
        return _obj



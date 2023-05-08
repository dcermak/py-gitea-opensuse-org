# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, conlist
from py_gitea_opensuse_org.models.attachment import Attachment
from py_gitea_opensuse_org.models.user import User

class Release(BaseModel):
    """
    Release represents a repository release
    """
    assets: Optional[conlist(Attachment)] = None
    author: Optional[User] = None
    body: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    draft: Optional[StrictBool] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    prerelease: Optional[StrictBool] = None
    published_at: Optional[datetime] = None
    tag_name: Optional[StrictStr] = None
    tarball_url: Optional[StrictStr] = None
    target_commitish: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    zipball_url: Optional[StrictStr] = None
    __properties = ["assets", "author", "body", "created_at", "draft", "html_url", "id", "name", "prerelease", "published_at", "tag_name", "tarball_url", "target_commitish", "url", "zipball_url"]

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
    def from_json(cls, json_str: str) -> Release:
        """Create an instance of Release from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Release:
        """Create an instance of Release from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Release.parse_obj(obj)

        _obj = Release.parse_obj({
            "assets": [Attachment.from_dict(_item) for _item in obj.get("assets")] if obj.get("assets") is not None else None,
            "author": User.from_dict(obj.get("author")) if obj.get("author") is not None else None,
            "body": obj.get("body"),
            "created_at": obj.get("created_at"),
            "draft": obj.get("draft"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "prerelease": obj.get("prerelease"),
            "published_at": obj.get("published_at"),
            "tag_name": obj.get("tag_name"),
            "tarball_url": obj.get("tarball_url"),
            "target_commitish": obj.get("target_commitish"),
            "url": obj.get("url"),
            "zipball_url": obj.get("zipball_url")
        })
        return _obj


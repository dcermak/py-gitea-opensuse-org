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


from typing import List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, conlist
from py_gitea_opensuse_org.models.git_entry import GitEntry

class GitTreeResponse(BaseModel):
    """
    GitTreeResponse returns a git tree
    """
    page: Optional[StrictInt] = None
    sha: Optional[StrictStr] = None
    total_count: Optional[StrictInt] = None
    tree: Optional[conlist(GitEntry)] = None
    truncated: Optional[StrictBool] = None
    url: Optional[StrictStr] = None
    __properties = ["page", "sha", "total_count", "tree", "truncated", "url"]

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
    def from_json(cls, json_str: str) -> GitTreeResponse:
        """Create an instance of GitTreeResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in tree (list)
        _items = []
        if self.tree:
            for _item in self.tree:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tree'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GitTreeResponse:
        """Create an instance of GitTreeResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GitTreeResponse.parse_obj(obj)

        _obj = GitTreeResponse.parse_obj({
            "page": obj.get("page"),
            "sha": obj.get("sha"),
            "total_count": obj.get("total_count"),
            "tree": [GitEntry.from_dict(_item) for _item in obj.get("tree")] if obj.get("tree") is not None else None,
            "truncated": obj.get("truncated"),
            "url": obj.get("url")
        })
        return _obj


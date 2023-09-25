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
from pydantic import BaseModel, Field, StrictStr, conlist
from py_gitea_opensuse_org.models.payload_commit_verification import PayloadCommitVerification
from py_gitea_opensuse_org.models.payload_user import PayloadUser

class PayloadCommit(BaseModel):
    """
    PayloadCommit represents a commit  # noqa: E501
    """
    added: Optional[conlist(StrictStr)] = None
    author: Optional[PayloadUser] = None
    committer: Optional[PayloadUser] = None
    id: Optional[StrictStr] = Field(None, description="sha1 hash of the commit")
    message: Optional[StrictStr] = None
    modified: Optional[conlist(StrictStr)] = None
    removed: Optional[conlist(StrictStr)] = None
    timestamp: Optional[datetime] = None
    url: Optional[StrictStr] = None
    verification: Optional[PayloadCommitVerification] = None
    __properties = ["added", "author", "committer", "id", "message", "modified", "removed", "timestamp", "url", "verification"]

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
    def from_json(cls, json_str: str) -> PayloadCommit:
        """Create an instance of PayloadCommit from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of committer
        if self.committer:
            _dict['committer'] = self.committer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of verification
        if self.verification:
            _dict['verification'] = self.verification.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PayloadCommit:
        """Create an instance of PayloadCommit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PayloadCommit.parse_obj(obj)

        _obj = PayloadCommit.parse_obj({
            "added": obj.get("added"),
            "author": PayloadUser.from_dict(obj.get("author")) if obj.get("author") is not None else None,
            "committer": PayloadUser.from_dict(obj.get("committer")) if obj.get("committer") is not None else None,
            "id": obj.get("id"),
            "message": obj.get("message"),
            "modified": obj.get("modified"),
            "removed": obj.get("removed"),
            "timestamp": obj.get("timestamp"),
            "url": obj.get("url"),
            "verification": PayloadCommitVerification.from_dict(obj.get("verification")) if obj.get("verification") is not None else None
        })
        return _obj



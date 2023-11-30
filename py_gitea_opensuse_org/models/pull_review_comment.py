# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.21.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from py_gitea_opensuse_org.models.user import User
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PullReviewComment(BaseModel):
    """
    PullReviewComment represents a comment on a pull request review
    """ # noqa: E501
    body: Optional[StrictStr] = None
    commit_id: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    diff_hunk: Optional[StrictStr] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    original_commit_id: Optional[StrictStr] = None
    original_position: Optional[StrictInt] = None
    path: Optional[StrictStr] = None
    position: Optional[StrictInt] = None
    pull_request_review_id: Optional[StrictInt] = None
    pull_request_url: Optional[StrictStr] = None
    resolver: Optional[User] = None
    updated_at: Optional[datetime] = None
    user: Optional[User] = None
    __properties: ClassVar[List[str]] = ["body", "commit_id", "created_at", "diff_hunk", "html_url", "id", "original_commit_id", "original_position", "path", "position", "pull_request_review_id", "pull_request_url", "resolver", "updated_at", "user"]

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
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PullReviewComment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of resolver
        if self.resolver:
            _dict['resolver'] = self.resolver.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PullReviewComment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "body": obj.get("body"),
            "commit_id": obj.get("commit_id"),
            "created_at": obj.get("created_at"),
            "diff_hunk": obj.get("diff_hunk"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "original_commit_id": obj.get("original_commit_id"),
            "original_position": obj.get("original_position"),
            "path": obj.get("path"),
            "position": obj.get("position"),
            "pull_request_review_id": obj.get("pull_request_review_id"),
            "pull_request_url": obj.get("pull_request_url"),
            "resolver": User.from_dict(obj.get("resolver")) if obj.get("resolver") is not None else None,
            "updated_at": obj.get("updated_at"),
            "user": User.from_dict(obj.get("user")) if obj.get("user") is not None else None
        })
        return _obj



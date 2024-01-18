# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.21.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_gitea_opensuse_org.models.team import Team
from py_gitea_opensuse_org.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class PullReview(BaseModel):
    """
    PullReview represents a pull request review
    """ # noqa: E501
    body: Optional[StrictStr] = None
    comments_count: Optional[StrictInt] = None
    commit_id: Optional[StrictStr] = None
    dismissed: Optional[StrictBool] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    official: Optional[StrictBool] = None
    pull_request_url: Optional[StrictStr] = None
    stale: Optional[StrictBool] = None
    state: Optional[StrictStr] = Field(default=None, description="ReviewStateType review state type")
    submitted_at: Optional[datetime] = None
    team: Optional[Team] = None
    updated_at: Optional[datetime] = None
    user: Optional[User] = None
    __properties: ClassVar[List[str]] = ["body", "comments_count", "commit_id", "dismissed", "html_url", "id", "official", "pull_request_url", "stale", "state", "submitted_at", "team", "updated_at", "user"]

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
        """Create an instance of PullReview from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of team
        if self.team:
            _dict['team'] = self.team.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PullReview from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "body": obj.get("body"),
            "comments_count": obj.get("comments_count"),
            "commit_id": obj.get("commit_id"),
            "dismissed": obj.get("dismissed"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "official": obj.get("official"),
            "pull_request_url": obj.get("pull_request_url"),
            "stale": obj.get("stale"),
            "state": obj.get("state"),
            "submitted_at": obj.get("submitted_at"),
            "team": Team.from_dict(obj["team"]) if obj.get("team") is not None else None,
            "updated_at": obj.get("updated_at"),
            "user": User.from_dict(obj["user"]) if obj.get("user") is not None else None
        })
        return _obj



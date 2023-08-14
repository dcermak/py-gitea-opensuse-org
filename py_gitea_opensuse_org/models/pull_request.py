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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from py_gitea_opensuse_org.models.label import Label
from py_gitea_opensuse_org.models.milestone import Milestone
from py_gitea_opensuse_org.models.pr_branch_info import PRBranchInfo
from py_gitea_opensuse_org.models.user import User

class PullRequest(BaseModel):
    """
    PullRequest represents a pull request
    """
    allow_maintainer_edit: Optional[StrictBool] = None
    assignee: Optional[User] = None
    assignees: Optional[conlist(User)] = None
    base: Optional[PRBranchInfo] = None
    body: Optional[StrictStr] = None
    closed_at: Optional[datetime] = None
    comments: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    diff_url: Optional[StrictStr] = None
    due_date: Optional[datetime] = None
    head: Optional[PRBranchInfo] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    is_locked: Optional[StrictBool] = None
    labels: Optional[conlist(Label)] = None
    merge_base: Optional[StrictStr] = None
    merge_commit_sha: Optional[StrictStr] = None
    mergeable: Optional[StrictBool] = None
    merged: Optional[StrictBool] = None
    merged_at: Optional[datetime] = None
    merged_by: Optional[User] = None
    milestone: Optional[Milestone] = None
    number: Optional[StrictInt] = None
    patch_url: Optional[StrictStr] = None
    state: Optional[StrictStr] = Field(None, description="StateType issue state type")
    title: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
    user: Optional[User] = None
    __properties = ["allow_maintainer_edit", "assignee", "assignees", "base", "body", "closed_at", "comments", "created_at", "diff_url", "due_date", "head", "html_url", "id", "is_locked", "labels", "merge_base", "merge_commit_sha", "mergeable", "merged", "merged_at", "merged_by", "milestone", "number", "patch_url", "state", "title", "updated_at", "url", "user"]

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
    def from_json(cls, json_str: str) -> PullRequest:
        """Create an instance of PullRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of assignee
        if self.assignee:
            _dict['assignee'] = self.assignee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in assignees (list)
        _items = []
        if self.assignees:
            for _item in self.assignees:
                if _item:
                    _items.append(_item.to_dict())
            _dict['assignees'] = _items
        # override the default output from pydantic by calling `to_dict()` of base
        if self.base:
            _dict['base'] = self.base.to_dict()
        # override the default output from pydantic by calling `to_dict()` of head
        if self.head:
            _dict['head'] = self.head.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item in self.labels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['labels'] = _items
        # override the default output from pydantic by calling `to_dict()` of merged_by
        if self.merged_by:
            _dict['merged_by'] = self.merged_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of milestone
        if self.milestone:
            _dict['milestone'] = self.milestone.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PullRequest:
        """Create an instance of PullRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PullRequest.parse_obj(obj)

        _obj = PullRequest.parse_obj({
            "allow_maintainer_edit": obj.get("allow_maintainer_edit"),
            "assignee": User.from_dict(obj.get("assignee")) if obj.get("assignee") is not None else None,
            "assignees": [User.from_dict(_item) for _item in obj.get("assignees")] if obj.get("assignees") is not None else None,
            "base": PRBranchInfo.from_dict(obj.get("base")) if obj.get("base") is not None else None,
            "body": obj.get("body"),
            "closed_at": obj.get("closed_at"),
            "comments": obj.get("comments"),
            "created_at": obj.get("created_at"),
            "diff_url": obj.get("diff_url"),
            "due_date": obj.get("due_date"),
            "head": PRBranchInfo.from_dict(obj.get("head")) if obj.get("head") is not None else None,
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "is_locked": obj.get("is_locked"),
            "labels": [Label.from_dict(_item) for _item in obj.get("labels")] if obj.get("labels") is not None else None,
            "merge_base": obj.get("merge_base"),
            "merge_commit_sha": obj.get("merge_commit_sha"),
            "mergeable": obj.get("mergeable"),
            "merged": obj.get("merged"),
            "merged_at": obj.get("merged_at"),
            "merged_by": User.from_dict(obj.get("merged_by")) if obj.get("merged_by") is not None else None,
            "milestone": Milestone.from_dict(obj.get("milestone")) if obj.get("milestone") is not None else None,
            "number": obj.get("number"),
            "patch_url": obj.get("patch_url"),
            "state": obj.get("state"),
            "title": obj.get("title"),
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url"),
            "user": User.from_dict(obj.get("user")) if obj.get("user") is not None else None
        })
        return _obj



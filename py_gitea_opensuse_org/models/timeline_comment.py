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
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from py_gitea_opensuse_org.models.comment import Comment
from py_gitea_opensuse_org.models.issue import Issue
from py_gitea_opensuse_org.models.label import Label
from py_gitea_opensuse_org.models.milestone import Milestone
from py_gitea_opensuse_org.models.team import Team
from py_gitea_opensuse_org.models.tracked_time import TrackedTime
from py_gitea_opensuse_org.models.user import User

class TimelineComment(BaseModel):
    """
    TimelineComment represents a timeline comment (comment of any type) on a commit or issue  # noqa: E501
    """
    assignee: Optional[User] = None
    assignee_team: Optional[Team] = None
    body: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    dependent_issue: Optional[Issue] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    issue_url: Optional[StrictStr] = None
    label: Optional[Label] = None
    milestone: Optional[Milestone] = None
    new_ref: Optional[StrictStr] = None
    new_title: Optional[StrictStr] = None
    old_milestone: Optional[Milestone] = None
    old_project_id: Optional[StrictInt] = None
    old_ref: Optional[StrictStr] = None
    old_title: Optional[StrictStr] = None
    project_id: Optional[StrictInt] = None
    pull_request_url: Optional[StrictStr] = None
    ref_action: Optional[StrictStr] = None
    ref_comment: Optional[Comment] = None
    ref_commit_sha: Optional[StrictStr] = Field(None, description="commit SHA where issue/PR was referenced")
    ref_issue: Optional[Issue] = None
    removed_assignee: Optional[StrictBool] = Field(None, description="whether the assignees were removed or added")
    resolve_doer: Optional[User] = None
    review_id: Optional[StrictInt] = None
    tracked_time: Optional[TrackedTime] = None
    type: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    user: Optional[User] = None
    __properties = ["assignee", "assignee_team", "body", "created_at", "dependent_issue", "html_url", "id", "issue_url", "label", "milestone", "new_ref", "new_title", "old_milestone", "old_project_id", "old_ref", "old_title", "project_id", "pull_request_url", "ref_action", "ref_comment", "ref_commit_sha", "ref_issue", "removed_assignee", "resolve_doer", "review_id", "tracked_time", "type", "updated_at", "user"]

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
    def from_json(cls, json_str: str) -> TimelineComment:
        """Create an instance of TimelineComment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of assignee_team
        if self.assignee_team:
            _dict['assignee_team'] = self.assignee_team.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dependent_issue
        if self.dependent_issue:
            _dict['dependent_issue'] = self.dependent_issue.to_dict()
        # override the default output from pydantic by calling `to_dict()` of label
        if self.label:
            _dict['label'] = self.label.to_dict()
        # override the default output from pydantic by calling `to_dict()` of milestone
        if self.milestone:
            _dict['milestone'] = self.milestone.to_dict()
        # override the default output from pydantic by calling `to_dict()` of old_milestone
        if self.old_milestone:
            _dict['old_milestone'] = self.old_milestone.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ref_comment
        if self.ref_comment:
            _dict['ref_comment'] = self.ref_comment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ref_issue
        if self.ref_issue:
            _dict['ref_issue'] = self.ref_issue.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resolve_doer
        if self.resolve_doer:
            _dict['resolve_doer'] = self.resolve_doer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tracked_time
        if self.tracked_time:
            _dict['tracked_time'] = self.tracked_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TimelineComment:
        """Create an instance of TimelineComment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TimelineComment.parse_obj(obj)

        _obj = TimelineComment.parse_obj({
            "assignee": User.from_dict(obj.get("assignee")) if obj.get("assignee") is not None else None,
            "assignee_team": Team.from_dict(obj.get("assignee_team")) if obj.get("assignee_team") is not None else None,
            "body": obj.get("body"),
            "created_at": obj.get("created_at"),
            "dependent_issue": Issue.from_dict(obj.get("dependent_issue")) if obj.get("dependent_issue") is not None else None,
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "issue_url": obj.get("issue_url"),
            "label": Label.from_dict(obj.get("label")) if obj.get("label") is not None else None,
            "milestone": Milestone.from_dict(obj.get("milestone")) if obj.get("milestone") is not None else None,
            "new_ref": obj.get("new_ref"),
            "new_title": obj.get("new_title"),
            "old_milestone": Milestone.from_dict(obj.get("old_milestone")) if obj.get("old_milestone") is not None else None,
            "old_project_id": obj.get("old_project_id"),
            "old_ref": obj.get("old_ref"),
            "old_title": obj.get("old_title"),
            "project_id": obj.get("project_id"),
            "pull_request_url": obj.get("pull_request_url"),
            "ref_action": obj.get("ref_action"),
            "ref_comment": Comment.from_dict(obj.get("ref_comment")) if obj.get("ref_comment") is not None else None,
            "ref_commit_sha": obj.get("ref_commit_sha"),
            "ref_issue": Issue.from_dict(obj.get("ref_issue")) if obj.get("ref_issue") is not None else None,
            "removed_assignee": obj.get("removed_assignee"),
            "resolve_doer": User.from_dict(obj.get("resolve_doer")) if obj.get("resolve_doer") is not None else None,
            "review_id": obj.get("review_id"),
            "tracked_time": TrackedTime.from_dict(obj.get("tracked_time")) if obj.get("tracked_time") is not None else None,
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at"),
            "user": User.from_dict(obj.get("user")) if obj.get("user") is not None else None
        })
        return _obj



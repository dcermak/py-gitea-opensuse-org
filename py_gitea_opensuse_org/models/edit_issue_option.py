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

class EditIssueOption(BaseModel):
    """
    EditIssueOption options for editing an issue  # noqa: E501
    """
    assignee: Optional[StrictStr] = Field(None, description="deprecated")
    assignees: Optional[conlist(StrictStr)] = None
    body: Optional[StrictStr] = None
    due_date: Optional[datetime] = None
    milestone: Optional[StrictInt] = None
    ref: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    unset_due_date: Optional[StrictBool] = None
    __properties = ["assignee", "assignees", "body", "due_date", "milestone", "ref", "state", "title", "unset_due_date"]

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
    def from_json(cls, json_str: str) -> EditIssueOption:
        """Create an instance of EditIssueOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EditIssueOption:
        """Create an instance of EditIssueOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EditIssueOption.parse_obj(obj)

        _obj = EditIssueOption.parse_obj({
            "assignee": obj.get("assignee"),
            "assignees": obj.get("assignees"),
            "body": obj.get("body"),
            "due_date": obj.get("due_date"),
            "milestone": obj.get("milestone"),
            "ref": obj.get("ref"),
            "state": obj.get("state"),
            "title": obj.get("title"),
            "unset_due_date": obj.get("unset_due_date")
        })
        return _obj



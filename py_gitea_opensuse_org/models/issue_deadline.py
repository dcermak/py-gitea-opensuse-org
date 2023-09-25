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
from pydantic import BaseModel

class IssueDeadline(BaseModel):
    """
    IssueDeadline represents an issue deadline  # noqa: E501
    """
    due_date: Optional[datetime] = None
    __properties = ["due_date"]

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
    def from_json(cls, json_str: str) -> IssueDeadline:
        """Create an instance of IssueDeadline from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IssueDeadline:
        """Create an instance of IssueDeadline from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IssueDeadline.parse_obj(obj)

        _obj = IssueDeadline.parse_obj({
            "due_date": obj.get("due_date")
        })
        return _obj



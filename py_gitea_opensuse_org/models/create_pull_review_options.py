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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from py_gitea_opensuse_org.models.create_pull_review_comment import CreatePullReviewComment

class CreatePullReviewOptions(BaseModel):
    """
    CreatePullReviewOptions are options to create a pull review
    """
    body: Optional[StrictStr] = None
    comments: Optional[conlist(CreatePullReviewComment)] = None
    commit_id: Optional[StrictStr] = None
    event: Optional[StrictStr] = Field(None, description="ReviewStateType review state type")
    __properties = ["body", "comments", "commit_id", "event"]

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
    def from_json(cls, json_str: str) -> CreatePullReviewOptions:
        """Create an instance of CreatePullReviewOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in comments (list)
        _items = []
        if self.comments:
            for _item in self.comments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['comments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreatePullReviewOptions:
        """Create an instance of CreatePullReviewOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreatePullReviewOptions.parse_obj(obj)

        _obj = CreatePullReviewOptions.parse_obj({
            "body": obj.get("body"),
            "comments": [CreatePullReviewComment.from_dict(_item) for _item in obj.get("comments")] if obj.get("comments") is not None else None,
            "commit_id": obj.get("commit_id"),
            "event": obj.get("event")
        })
        return _obj


# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.21.0-rc1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateIssueOption(BaseModel):
    """
    CreateIssueOption options to create one issue
    """ # noqa: E501
    assignee: Optional[StrictStr] = Field(default=None, description="deprecated")
    assignees: Optional[List[StrictStr]] = None
    body: Optional[StrictStr] = None
    closed: Optional[StrictBool] = None
    due_date: Optional[datetime] = None
    labels: Optional[List[StrictInt]] = Field(default=None, description="list of label ids")
    milestone: Optional[StrictInt] = Field(default=None, description="milestone id")
    ref: Optional[StrictStr] = None
    title: StrictStr
    __properties: ClassVar[List[str]] = ["assignee", "assignees", "body", "closed", "due_date", "labels", "milestone", "ref", "title"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
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
        """Create an instance of CreateIssueOption from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateIssueOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assignee": obj.get("assignee"),
            "assignees": obj.get("assignees"),
            "body": obj.get("body"),
            "closed": obj.get("closed"),
            "due_date": obj.get("due_date"),
            "labels": obj.get("labels"),
            "milestone": obj.get("milestone"),
            "ref": obj.get("ref"),
            "title": obj.get("title")
        })
        return _obj



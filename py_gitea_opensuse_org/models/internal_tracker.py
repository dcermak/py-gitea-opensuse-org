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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class InternalTracker(BaseModel):
    """
    InternalTracker represents settings for internal tracker
    """ # noqa: E501
    allow_only_contributors_to_track_time: Optional[StrictBool] = Field(default=None, description="Let only contributors track time (Built-in issue tracker)")
    enable_issue_dependencies: Optional[StrictBool] = Field(default=None, description="Enable dependencies for issues and pull requests (Built-in issue tracker)")
    enable_time_tracker: Optional[StrictBool] = Field(default=None, description="Enable time tracking (Built-in issue tracker)")
    __properties: ClassVar[List[str]] = ["allow_only_contributors_to_track_time", "enable_issue_dependencies", "enable_time_tracker"]

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
        """Create an instance of InternalTracker from a JSON string"""
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
        """Create an instance of InternalTracker from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allow_only_contributors_to_track_time": obj.get("allow_only_contributors_to_track_time"),
            "enable_issue_dependencies": obj.get("enable_issue_dependencies"),
            "enable_time_tracker": obj.get("enable_time_tracker")
        })
        return _obj



# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.21.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UserSettingsOptions(BaseModel):
    """
    UserSettingsOptions represents options to change user settings
    """ # noqa: E501
    description: Optional[StrictStr] = None
    diff_view_style: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = None
    hide_activity: Optional[StrictBool] = None
    hide_email: Optional[StrictBool] = Field(default=None, description="Privacy")
    language: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    theme: Optional[StrictStr] = None
    website: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["description", "diff_view_style", "full_name", "hide_activity", "hide_email", "language", "location", "theme", "website"]

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
        """Create an instance of UserSettingsOptions from a JSON string"""
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
        """Create an instance of UserSettingsOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "diff_view_style": obj.get("diff_view_style"),
            "full_name": obj.get("full_name"),
            "hide_activity": obj.get("hide_activity"),
            "hide_email": obj.get("hide_email"),
            "language": obj.get("language"),
            "location": obj.get("location"),
            "theme": obj.get("theme"),
            "website": obj.get("website")
        })
        return _obj



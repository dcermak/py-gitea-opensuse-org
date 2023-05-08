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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, validator

class EditTeamOption(BaseModel):
    """
    EditTeamOption options for editing a team
    """
    can_create_org_repo: Optional[StrictBool] = None
    description: Optional[StrictStr] = None
    includes_all_repositories: Optional[StrictBool] = None
    name: StrictStr = Field(...)
    permission: Optional[StrictStr] = None
    units: Optional[conlist(StrictStr)] = None
    units_map: Optional[Dict[str, StrictStr]] = None
    __properties = ["can_create_org_repo", "description", "includes_all_repositories", "name", "permission", "units", "units_map"]

    @validator('permission')
    def permission_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('read', 'write', 'admin'):
            raise ValueError("must be one of enum values ('read', 'write', 'admin')")
        return value

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
    def from_json(cls, json_str: str) -> EditTeamOption:
        """Create an instance of EditTeamOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EditTeamOption:
        """Create an instance of EditTeamOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EditTeamOption.parse_obj(obj)

        _obj = EditTeamOption.parse_obj({
            "can_create_org_repo": obj.get("can_create_org_repo"),
            "description": obj.get("description"),
            "includes_all_repositories": obj.get("includes_all_repositories"),
            "name": obj.get("name"),
            "permission": obj.get("permission"),
            "units": obj.get("units"),
            "units_map": obj.get("units_map")
        })
        return _obj


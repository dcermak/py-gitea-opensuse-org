# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.22.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Organization(BaseModel):
    """
    Organization represents an organization
    """ # noqa: E501
    avatar_url: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    location: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    repo_admin_change_team_access: Optional[StrictBool] = None
    username: Optional[StrictStr] = Field(default=None, description="deprecated")
    visibility: Optional[StrictStr] = None
    website: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["avatar_url", "description", "email", "full_name", "id", "location", "name", "repo_admin_change_team_access", "username", "visibility", "website"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Organization from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Organization from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "avatar_url": obj.get("avatar_url"),
            "description": obj.get("description"),
            "email": obj.get("email"),
            "full_name": obj.get("full_name"),
            "id": obj.get("id"),
            "location": obj.get("location"),
            "name": obj.get("name"),
            "repo_admin_change_team_access": obj.get("repo_admin_change_team_access"),
            "username": obj.get("username"),
            "visibility": obj.get("visibility"),
            "website": obj.get("website")
        })
        return _obj



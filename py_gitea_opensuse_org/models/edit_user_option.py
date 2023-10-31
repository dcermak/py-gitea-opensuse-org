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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EditUserOption(BaseModel):
    """
    EditUserOption edit user options
    """ # noqa: E501
    active: Optional[StrictBool] = None
    admin: Optional[StrictBool] = None
    allow_create_organization: Optional[StrictBool] = None
    allow_git_hook: Optional[StrictBool] = None
    allow_import_local: Optional[StrictBool] = None
    description: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    login_name: StrictStr
    max_repo_creation: Optional[StrictInt] = None
    must_change_password: Optional[StrictBool] = None
    password: Optional[StrictStr] = None
    prohibit_login: Optional[StrictBool] = None
    restricted: Optional[StrictBool] = None
    source_id: StrictInt
    visibility: Optional[StrictStr] = None
    website: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["active", "admin", "allow_create_organization", "allow_git_hook", "allow_import_local", "description", "email", "full_name", "location", "login_name", "max_repo_creation", "must_change_password", "password", "prohibit_login", "restricted", "source_id", "visibility", "website"]

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
        """Create an instance of EditUserOption from a JSON string"""
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
        """Create an instance of EditUserOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": obj.get("active"),
            "admin": obj.get("admin"),
            "allow_create_organization": obj.get("allow_create_organization"),
            "allow_git_hook": obj.get("allow_git_hook"),
            "allow_import_local": obj.get("allow_import_local"),
            "description": obj.get("description"),
            "email": obj.get("email"),
            "full_name": obj.get("full_name"),
            "location": obj.get("location"),
            "login_name": obj.get("login_name"),
            "max_repo_creation": obj.get("max_repo_creation"),
            "must_change_password": obj.get("must_change_password"),
            "password": obj.get("password"),
            "prohibit_login": obj.get("prohibit_login"),
            "restricted": obj.get("restricted"),
            "source_id": obj.get("source_id"),
            "visibility": obj.get("visibility"),
            "website": obj.get("website")
        })
        return _obj



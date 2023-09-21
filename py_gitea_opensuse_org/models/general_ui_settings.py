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


from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist

class GeneralUISettings(BaseModel):
    """
    GeneralUISettings contains global ui settings exposed by API  # noqa: E501
    """
    allowed_reactions: Optional[conlist(StrictStr)] = None
    custom_emojis: Optional[conlist(StrictStr)] = None
    default_theme: Optional[StrictStr] = None
    __properties = ["allowed_reactions", "custom_emojis", "default_theme"]

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
    def from_json(cls, json_str: str) -> GeneralUISettings:
        """Create an instance of GeneralUISettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GeneralUISettings:
        """Create an instance of GeneralUISettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GeneralUISettings.parse_obj(obj)

        _obj = GeneralUISettings.parse_obj({
            "allowed_reactions": obj.get("allowed_reactions"),
            "custom_emojis": obj.get("custom_emojis"),
            "default_theme": obj.get("default_theme")
        })
        return _obj



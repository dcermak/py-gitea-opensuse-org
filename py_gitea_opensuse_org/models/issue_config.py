# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.23.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from py_gitea_opensuse_org.models.issue_config_contact_link import IssueConfigContactLink
from typing import Optional, Set
from typing_extensions import Self

class IssueConfig(BaseModel):
    """
    IssueConfig
    """ # noqa: E501
    blank_issues_enabled: Optional[StrictBool] = None
    contact_links: Optional[List[IssueConfigContactLink]] = None
    __properties: ClassVar[List[str]] = ["blank_issues_enabled", "contact_links"]

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
        """Create an instance of IssueConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in contact_links (list)
        _items = []
        if self.contact_links:
            for _item_contact_links in self.contact_links:
                if _item_contact_links:
                    _items.append(_item_contact_links.to_dict())
            _dict['contact_links'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IssueConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "blank_issues_enabled": obj.get("blank_issues_enabled"),
            "contact_links": [IssueConfigContactLink.from_dict(_item) for _item in obj["contact_links"]] if obj.get("contact_links") is not None else None
        })
        return _obj



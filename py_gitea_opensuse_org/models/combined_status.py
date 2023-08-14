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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from py_gitea_opensuse_org.models.commit_status import CommitStatus
from py_gitea_opensuse_org.models.repository import Repository

class CombinedStatus(BaseModel):
    """
    CombinedStatus holds the combined state of several statuses for a single commit
    """
    commit_url: Optional[StrictStr] = None
    repository: Optional[Repository] = None
    sha: Optional[StrictStr] = None
    state: Optional[StrictStr] = Field(None, description="CommitStatusState holds the state of a CommitStatus It can be \"pending\", \"success\", \"error\", \"failure\", and \"warning\"")
    statuses: Optional[conlist(CommitStatus)] = None
    total_count: Optional[StrictInt] = None
    url: Optional[StrictStr] = None
    __properties = ["commit_url", "repository", "sha", "state", "statuses", "total_count", "url"]

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
    def from_json(cls, json_str: str) -> CombinedStatus:
        """Create an instance of CombinedStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of repository
        if self.repository:
            _dict['repository'] = self.repository.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in statuses (list)
        _items = []
        if self.statuses:
            for _item in self.statuses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['statuses'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CombinedStatus:
        """Create an instance of CombinedStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CombinedStatus.parse_obj(obj)

        _obj = CombinedStatus.parse_obj({
            "commit_url": obj.get("commit_url"),
            "repository": Repository.from_dict(obj.get("repository")) if obj.get("repository") is not None else None,
            "sha": obj.get("sha"),
            "state": obj.get("state"),
            "statuses": [CommitStatus.from_dict(_item) for _item in obj.get("statuses")] if obj.get("statuses") is not None else None,
            "total_count": obj.get("total_count"),
            "url": obj.get("url")
        })
        return _obj



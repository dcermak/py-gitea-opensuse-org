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
from pydantic import BaseModel, StrictStr
from py_gitea_opensuse_org.models.commit_user import CommitUser
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WikiCommit(BaseModel):
    """
    WikiCommit page commit/revision
    """ # noqa: E501
    author: Optional[CommitUser] = None
    commiter: Optional[CommitUser] = None
    message: Optional[StrictStr] = None
    sha: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["author", "commiter", "message", "sha"]

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
        """Create an instance of WikiCommit from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of commiter
        if self.commiter:
            _dict['commiter'] = self.commiter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WikiCommit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "author": CommitUser.from_dict(obj.get("author")) if obj.get("author") is not None else None,
            "commiter": CommitUser.from_dict(obj.get("commiter")) if obj.get("commiter") is not None else None,
            "message": obj.get("message"),
            "sha": obj.get("sha")
        })
        return _obj



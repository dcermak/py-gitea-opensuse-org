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
from pydantic import BaseModel, StrictInt, StrictStr
from py_gitea_opensuse_org.models.repository import Repository
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PRBranchInfo(BaseModel):
    """
    PRBranchInfo information about a branch
    """ # noqa: E501
    label: Optional[StrictStr] = None
    ref: Optional[StrictStr] = None
    repo: Optional[Repository] = None
    repo_id: Optional[StrictInt] = None
    sha: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["label", "ref", "repo", "repo_id", "sha"]

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
        """Create an instance of PRBranchInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of repo
        if self.repo:
            _dict['repo'] = self.repo.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PRBranchInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "label": obj.get("label"),
            "ref": obj.get("ref"),
            "repo": Repository.from_dict(obj.get("repo")) if obj.get("repo") is not None else None,
            "repo_id": obj.get("repo_id"),
            "sha": obj.get("sha")
        })
        return _obj



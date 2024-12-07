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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_gitea_opensuse_org.models.commit_meta import CommitMeta
from py_gitea_opensuse_org.models.commit_user import CommitUser
from typing import Optional, Set
from typing_extensions import Self

class FileCommitResponse(BaseModel):
    """
    FileCommitResponse
    """ # noqa: E501
    author: Optional[CommitUser] = None
    committer: Optional[CommitUser] = None
    created: Optional[datetime] = None
    html_url: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
    parents: Optional[List[CommitMeta]] = None
    sha: Optional[StrictStr] = None
    tree: Optional[CommitMeta] = None
    url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["author", "committer", "created", "html_url", "message", "parents", "sha", "tree", "url"]

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
        """Create an instance of FileCommitResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of committer
        if self.committer:
            _dict['committer'] = self.committer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in parents (list)
        _items = []
        if self.parents:
            for _item_parents in self.parents:
                if _item_parents:
                    _items.append(_item_parents.to_dict())
            _dict['parents'] = _items
        # override the default output from pydantic by calling `to_dict()` of tree
        if self.tree:
            _dict['tree'] = self.tree.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FileCommitResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "author": CommitUser.from_dict(obj["author"]) if obj.get("author") is not None else None,
            "committer": CommitUser.from_dict(obj["committer"]) if obj.get("committer") is not None else None,
            "created": obj.get("created"),
            "html_url": obj.get("html_url"),
            "message": obj.get("message"),
            "parents": [CommitMeta.from_dict(_item) for _item in obj["parents"]] if obj.get("parents") is not None else None,
            "sha": obj.get("sha"),
            "tree": CommitMeta.from_dict(obj["tree"]) if obj.get("tree") is not None else None,
            "url": obj.get("url")
        })
        return _obj



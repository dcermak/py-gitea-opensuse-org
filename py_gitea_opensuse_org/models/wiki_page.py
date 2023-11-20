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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from py_gitea_opensuse_org.models.wiki_commit import WikiCommit
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WikiPage(BaseModel):
    """
    WikiPage a wiki page
    """ # noqa: E501
    commit_count: Optional[StrictInt] = None
    content_base64: Optional[StrictStr] = Field(default=None, description="Page content, base64 encoded")
    footer: Optional[StrictStr] = None
    html_url: Optional[StrictStr] = None
    last_commit: Optional[WikiCommit] = None
    sidebar: Optional[StrictStr] = None
    sub_url: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["commit_count", "content_base64", "footer", "html_url", "last_commit", "sidebar", "sub_url", "title"]

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
        """Create an instance of WikiPage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of last_commit
        if self.last_commit:
            _dict['last_commit'] = self.last_commit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WikiPage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "commit_count": obj.get("commit_count"),
            "content_base64": obj.get("content_base64"),
            "footer": obj.get("footer"),
            "html_url": obj.get("html_url"),
            "last_commit": WikiCommit.from_dict(obj.get("last_commit")) if obj.get("last_commit") is not None else None,
            "sidebar": obj.get("sidebar"),
            "sub_url": obj.get("sub_url"),
            "title": obj.get("title")
        })
        return _obj



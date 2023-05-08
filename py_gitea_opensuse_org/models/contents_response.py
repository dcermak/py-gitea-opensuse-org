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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from py_gitea_opensuse_org.models.file_links_response import FileLinksResponse

class ContentsResponse(BaseModel):
    """
    ContentsResponse contains information about a repo's entry's (dir, file, symlink, submodule) metadata and content
    """
    links: Optional[FileLinksResponse] = Field(None, alias="_links")
    content: Optional[StrictStr] = Field(None, description="`content` is populated when `type` is `file`, otherwise null")
    download_url: Optional[StrictStr] = None
    encoding: Optional[StrictStr] = Field(None, description="`encoding` is populated when `type` is `file`, otherwise null")
    git_url: Optional[StrictStr] = None
    html_url: Optional[StrictStr] = None
    last_commit_sha: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    path: Optional[StrictStr] = None
    sha: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
    submodule_git_url: Optional[StrictStr] = Field(None, description="`submodule_git_url` is populated when `type` is `submodule`, otherwise null")
    target: Optional[StrictStr] = Field(None, description="`target` is populated when `type` is `symlink`, otherwise null")
    type: Optional[StrictStr] = Field(None, description="`type` will be `file`, `dir`, `symlink`, or `submodule`")
    url: Optional[StrictStr] = None
    __properties = ["_links", "content", "download_url", "encoding", "git_url", "html_url", "last_commit_sha", "name", "path", "sha", "size", "submodule_git_url", "target", "type", "url"]

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
    def from_json(cls, json_str: str) -> ContentsResponse:
        """Create an instance of ContentsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContentsResponse:
        """Create an instance of ContentsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContentsResponse.parse_obj(obj)

        _obj = ContentsResponse.parse_obj({
            "links": FileLinksResponse.from_dict(obj.get("_links")) if obj.get("_links") is not None else None,
            "content": obj.get("content"),
            "download_url": obj.get("download_url"),
            "encoding": obj.get("encoding"),
            "git_url": obj.get("git_url"),
            "html_url": obj.get("html_url"),
            "last_commit_sha": obj.get("last_commit_sha"),
            "name": obj.get("name"),
            "path": obj.get("path"),
            "sha": obj.get("sha"),
            "size": obj.get("size"),
            "submodule_git_url": obj.get("submodule_git_url"),
            "target": obj.get("target"),
            "type": obj.get("type"),
            "url": obj.get("url")
        })
        return _obj


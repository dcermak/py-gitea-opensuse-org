# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from py_gitea_opensuse_org.models.commit_date_options import CommitDateOptions
from py_gitea_opensuse_org.models.identity import Identity

class UpdateFileOptions(BaseModel):
    """
    UpdateFileOptions options for updating files Note: `author` and `committer` are optional (if only one is given, it will be used for the other, otherwise the authenticated user will be used)
    """
    author: Optional[Identity] = None
    branch: Optional[StrictStr] = Field(None, description="branch (optional) to base this file from. if not given, the default branch is used")
    committer: Optional[Identity] = None
    content: StrictStr = Field(..., description="content must be base64 encoded")
    dates: Optional[CommitDateOptions] = None
    from_path: Optional[StrictStr] = Field(None, description="from_path (optional) is the path of the original file which will be moved/renamed to the path in the URL")
    message: Optional[StrictStr] = Field(None, description="message (optional) for the commit of this file. if not supplied, a default message will be used")
    new_branch: Optional[StrictStr] = Field(None, description="new_branch (optional) will make a new branch from `branch` before creating the file")
    sha: StrictStr = Field(..., description="sha is the SHA for the file that already exists")
    signoff: Optional[StrictBool] = Field(None, description="Add a Signed-off-by trailer by the committer at the end of the commit log message.")
    __properties = ["author", "branch", "committer", "content", "dates", "from_path", "message", "new_branch", "sha", "signoff"]

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
    def from_json(cls, json_str: str) -> UpdateFileOptions:
        """Create an instance of UpdateFileOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of committer
        if self.committer:
            _dict['committer'] = self.committer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dates
        if self.dates:
            _dict['dates'] = self.dates.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateFileOptions:
        """Create an instance of UpdateFileOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateFileOptions.parse_obj(obj)

        _obj = UpdateFileOptions.parse_obj({
            "author": Identity.from_dict(obj.get("author")) if obj.get("author") is not None else None,
            "branch": obj.get("branch"),
            "committer": Identity.from_dict(obj.get("committer")) if obj.get("committer") is not None else None,
            "content": obj.get("content"),
            "dates": CommitDateOptions.from_dict(obj.get("dates")) if obj.get("dates") is not None else None,
            "from_path": obj.get("from_path"),
            "message": obj.get("message"),
            "new_branch": obj.get("new_branch"),
            "sha": obj.get("sha"),
            "signoff": obj.get("signoff")
        })
        return _obj


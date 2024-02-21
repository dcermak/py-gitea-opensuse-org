# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.21.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GenerateRepoOption(BaseModel):
    """
    GenerateRepoOption options when creating repository using a template
    """ # noqa: E501
    avatar: Optional[StrictBool] = Field(default=None, description="include avatar of the template repo")
    default_branch: Optional[StrictStr] = Field(default=None, description="Default branch of the new repository")
    description: Optional[StrictStr] = Field(default=None, description="Description of the repository to create")
    git_content: Optional[StrictBool] = Field(default=None, description="include git content of default branch in template repo")
    git_hooks: Optional[StrictBool] = Field(default=None, description="include git hooks in template repo")
    labels: Optional[StrictBool] = Field(default=None, description="include labels in template repo")
    name: StrictStr = Field(description="Name of the repository to create")
    owner: StrictStr = Field(description="The organization or person who will own the new repository")
    private: Optional[StrictBool] = Field(default=None, description="Whether the repository is private")
    protected_branch: Optional[StrictBool] = Field(default=None, description="include protected branches in template repo")
    topics: Optional[StrictBool] = Field(default=None, description="include topics in template repo")
    webhooks: Optional[StrictBool] = Field(default=None, description="include webhooks in template repo")
    __properties: ClassVar[List[str]] = ["avatar", "default_branch", "description", "git_content", "git_hooks", "labels", "name", "owner", "private", "protected_branch", "topics", "webhooks"]

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
        """Create an instance of GenerateRepoOption from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GenerateRepoOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "avatar": obj.get("avatar"),
            "default_branch": obj.get("default_branch"),
            "description": obj.get("description"),
            "git_content": obj.get("git_content"),
            "git_hooks": obj.get("git_hooks"),
            "labels": obj.get("labels"),
            "name": obj.get("name"),
            "owner": obj.get("owner"),
            "private": obj.get("private"),
            "protected_branch": obj.get("protected_branch"),
            "topics": obj.get("topics"),
            "webhooks": obj.get("webhooks")
        })
        return _obj



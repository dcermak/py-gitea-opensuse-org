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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator

class MigrateRepoOptions(BaseModel):
    """
    MigrateRepoOptions options for migrating repository's this is used to interact with api v1
    """
    auth_password: Optional[StrictStr] = None
    auth_token: Optional[StrictStr] = None
    auth_username: Optional[StrictStr] = None
    clone_addr: StrictStr = Field(...)
    description: Optional[StrictStr] = None
    issues: Optional[StrictBool] = None
    labels: Optional[StrictBool] = None
    lfs: Optional[StrictBool] = None
    lfs_endpoint: Optional[StrictStr] = None
    milestones: Optional[StrictBool] = None
    mirror: Optional[StrictBool] = None
    mirror_interval: Optional[StrictStr] = None
    private: Optional[StrictBool] = None
    pull_requests: Optional[StrictBool] = None
    releases: Optional[StrictBool] = None
    repo_name: StrictStr = Field(...)
    repo_owner: Optional[StrictStr] = Field(None, description="Name of User or Organisation who will own Repo after migration")
    service: Optional[StrictStr] = None
    uid: Optional[StrictInt] = Field(None, description="deprecated (only for backwards compatibility)")
    wiki: Optional[StrictBool] = None
    __properties = ["auth_password", "auth_token", "auth_username", "clone_addr", "description", "issues", "labels", "lfs", "lfs_endpoint", "milestones", "mirror", "mirror_interval", "private", "pull_requests", "releases", "repo_name", "repo_owner", "service", "uid", "wiki"]

    @validator('service')
    def service_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('git', 'github', 'gitea', 'gitlab'):
            raise ValueError("must be one of enum values ('git', 'github', 'gitea', 'gitlab')")
        return value

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
    def from_json(cls, json_str: str) -> MigrateRepoOptions:
        """Create an instance of MigrateRepoOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MigrateRepoOptions:
        """Create an instance of MigrateRepoOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MigrateRepoOptions.parse_obj(obj)

        _obj = MigrateRepoOptions.parse_obj({
            "auth_password": obj.get("auth_password"),
            "auth_token": obj.get("auth_token"),
            "auth_username": obj.get("auth_username"),
            "clone_addr": obj.get("clone_addr"),
            "description": obj.get("description"),
            "issues": obj.get("issues"),
            "labels": obj.get("labels"),
            "lfs": obj.get("lfs"),
            "lfs_endpoint": obj.get("lfs_endpoint"),
            "milestones": obj.get("milestones"),
            "mirror": obj.get("mirror"),
            "mirror_interval": obj.get("mirror_interval"),
            "private": obj.get("private"),
            "pull_requests": obj.get("pull_requests"),
            "releases": obj.get("releases"),
            "repo_name": obj.get("repo_name"),
            "repo_owner": obj.get("repo_owner"),
            "service": obj.get("service"),
            "uid": obj.get("uid"),
            "wiki": obj.get("wiki")
        })
        return _obj


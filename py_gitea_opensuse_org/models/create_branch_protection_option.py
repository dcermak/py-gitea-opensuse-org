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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist

class CreateBranchProtectionOption(BaseModel):
    """
    CreateBranchProtectionOption options for creating a branch protection
    """
    approvals_whitelist_teams: Optional[conlist(StrictStr)] = None
    approvals_whitelist_username: Optional[conlist(StrictStr)] = None
    block_on_official_review_requests: Optional[StrictBool] = None
    block_on_outdated_branch: Optional[StrictBool] = None
    block_on_rejected_reviews: Optional[StrictBool] = None
    branch_name: Optional[StrictStr] = Field(None, description="Deprecated: true")
    dismiss_stale_approvals: Optional[StrictBool] = None
    enable_approvals_whitelist: Optional[StrictBool] = None
    enable_merge_whitelist: Optional[StrictBool] = None
    enable_push: Optional[StrictBool] = None
    enable_push_whitelist: Optional[StrictBool] = None
    enable_status_check: Optional[StrictBool] = None
    merge_whitelist_teams: Optional[conlist(StrictStr)] = None
    merge_whitelist_usernames: Optional[conlist(StrictStr)] = None
    protected_file_patterns: Optional[StrictStr] = None
    push_whitelist_deploy_keys: Optional[StrictBool] = None
    push_whitelist_teams: Optional[conlist(StrictStr)] = None
    push_whitelist_usernames: Optional[conlist(StrictStr)] = None
    require_signed_commits: Optional[StrictBool] = None
    required_approvals: Optional[StrictInt] = None
    rule_name: Optional[StrictStr] = None
    status_check_contexts: Optional[conlist(StrictStr)] = None
    unprotected_file_patterns: Optional[StrictStr] = None
    __properties = ["approvals_whitelist_teams", "approvals_whitelist_username", "block_on_official_review_requests", "block_on_outdated_branch", "block_on_rejected_reviews", "branch_name", "dismiss_stale_approvals", "enable_approvals_whitelist", "enable_merge_whitelist", "enable_push", "enable_push_whitelist", "enable_status_check", "merge_whitelist_teams", "merge_whitelist_usernames", "protected_file_patterns", "push_whitelist_deploy_keys", "push_whitelist_teams", "push_whitelist_usernames", "require_signed_commits", "required_approvals", "rule_name", "status_check_contexts", "unprotected_file_patterns"]

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
    def from_json(cls, json_str: str) -> CreateBranchProtectionOption:
        """Create an instance of CreateBranchProtectionOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateBranchProtectionOption:
        """Create an instance of CreateBranchProtectionOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateBranchProtectionOption.parse_obj(obj)

        _obj = CreateBranchProtectionOption.parse_obj({
            "approvals_whitelist_teams": obj.get("approvals_whitelist_teams"),
            "approvals_whitelist_username": obj.get("approvals_whitelist_username"),
            "block_on_official_review_requests": obj.get("block_on_official_review_requests"),
            "block_on_outdated_branch": obj.get("block_on_outdated_branch"),
            "block_on_rejected_reviews": obj.get("block_on_rejected_reviews"),
            "branch_name": obj.get("branch_name"),
            "dismiss_stale_approvals": obj.get("dismiss_stale_approvals"),
            "enable_approvals_whitelist": obj.get("enable_approvals_whitelist"),
            "enable_merge_whitelist": obj.get("enable_merge_whitelist"),
            "enable_push": obj.get("enable_push"),
            "enable_push_whitelist": obj.get("enable_push_whitelist"),
            "enable_status_check": obj.get("enable_status_check"),
            "merge_whitelist_teams": obj.get("merge_whitelist_teams"),
            "merge_whitelist_usernames": obj.get("merge_whitelist_usernames"),
            "protected_file_patterns": obj.get("protected_file_patterns"),
            "push_whitelist_deploy_keys": obj.get("push_whitelist_deploy_keys"),
            "push_whitelist_teams": obj.get("push_whitelist_teams"),
            "push_whitelist_usernames": obj.get("push_whitelist_usernames"),
            "require_signed_commits": obj.get("require_signed_commits"),
            "required_approvals": obj.get("required_approvals"),
            "rule_name": obj.get("rule_name"),
            "status_check_contexts": obj.get("status_check_contexts"),
            "unprotected_file_patterns": obj.get("unprotected_file_patterns")
        })
        return _obj


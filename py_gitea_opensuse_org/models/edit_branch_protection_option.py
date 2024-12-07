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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class EditBranchProtectionOption(BaseModel):
    """
    EditBranchProtectionOption options for editing a branch protection
    """ # noqa: E501
    approvals_whitelist_teams: Optional[List[StrictStr]] = None
    approvals_whitelist_username: Optional[List[StrictStr]] = None
    block_on_official_review_requests: Optional[StrictBool] = None
    block_on_outdated_branch: Optional[StrictBool] = None
    block_on_rejected_reviews: Optional[StrictBool] = None
    dismiss_stale_approvals: Optional[StrictBool] = None
    enable_approvals_whitelist: Optional[StrictBool] = None
    enable_merge_whitelist: Optional[StrictBool] = None
    enable_push: Optional[StrictBool] = None
    enable_push_whitelist: Optional[StrictBool] = None
    enable_status_check: Optional[StrictBool] = None
    ignore_stale_approvals: Optional[StrictBool] = None
    merge_whitelist_teams: Optional[List[StrictStr]] = None
    merge_whitelist_usernames: Optional[List[StrictStr]] = None
    protected_file_patterns: Optional[StrictStr] = None
    push_whitelist_deploy_keys: Optional[StrictBool] = None
    push_whitelist_teams: Optional[List[StrictStr]] = None
    push_whitelist_usernames: Optional[List[StrictStr]] = None
    require_signed_commits: Optional[StrictBool] = None
    required_approvals: Optional[StrictInt] = None
    status_check_contexts: Optional[List[StrictStr]] = None
    unprotected_file_patterns: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["approvals_whitelist_teams", "approvals_whitelist_username", "block_on_official_review_requests", "block_on_outdated_branch", "block_on_rejected_reviews", "dismiss_stale_approvals", "enable_approvals_whitelist", "enable_merge_whitelist", "enable_push", "enable_push_whitelist", "enable_status_check", "ignore_stale_approvals", "merge_whitelist_teams", "merge_whitelist_usernames", "protected_file_patterns", "push_whitelist_deploy_keys", "push_whitelist_teams", "push_whitelist_usernames", "require_signed_commits", "required_approvals", "status_check_contexts", "unprotected_file_patterns"]

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
        """Create an instance of EditBranchProtectionOption from a JSON string"""
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
        """Create an instance of EditBranchProtectionOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "approvals_whitelist_teams": obj.get("approvals_whitelist_teams"),
            "approvals_whitelist_username": obj.get("approvals_whitelist_username"),
            "block_on_official_review_requests": obj.get("block_on_official_review_requests"),
            "block_on_outdated_branch": obj.get("block_on_outdated_branch"),
            "block_on_rejected_reviews": obj.get("block_on_rejected_reviews"),
            "dismiss_stale_approvals": obj.get("dismiss_stale_approvals"),
            "enable_approvals_whitelist": obj.get("enable_approvals_whitelist"),
            "enable_merge_whitelist": obj.get("enable_merge_whitelist"),
            "enable_push": obj.get("enable_push"),
            "enable_push_whitelist": obj.get("enable_push_whitelist"),
            "enable_status_check": obj.get("enable_status_check"),
            "ignore_stale_approvals": obj.get("ignore_stale_approvals"),
            "merge_whitelist_teams": obj.get("merge_whitelist_teams"),
            "merge_whitelist_usernames": obj.get("merge_whitelist_usernames"),
            "protected_file_patterns": obj.get("protected_file_patterns"),
            "push_whitelist_deploy_keys": obj.get("push_whitelist_deploy_keys"),
            "push_whitelist_teams": obj.get("push_whitelist_teams"),
            "push_whitelist_usernames": obj.get("push_whitelist_usernames"),
            "require_signed_commits": obj.get("require_signed_commits"),
            "required_approvals": obj.get("required_approvals"),
            "status_check_contexts": obj.get("status_check_contexts"),
            "unprotected_file_patterns": obj.get("unprotected_file_patterns")
        })
        return _obj



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
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MergePullRequestOption(BaseModel):
    """
    MergePullRequestForm form for merging Pull Request
    """ # noqa: E501
    do: StrictStr = Field(alias="Do")
    merge_commit_id: Optional[StrictStr] = Field(default=None, alias="MergeCommitID")
    merge_message_field: Optional[StrictStr] = Field(default=None, alias="MergeMessageField")
    merge_title_field: Optional[StrictStr] = Field(default=None, alias="MergeTitleField")
    delete_branch_after_merge: Optional[StrictBool] = None
    force_merge: Optional[StrictBool] = None
    head_commit_id: Optional[StrictStr] = None
    merge_when_checks_succeed: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["Do", "MergeCommitID", "MergeMessageField", "MergeTitleField", "delete_branch_after_merge", "force_merge", "head_commit_id", "merge_when_checks_succeed"]

    @field_validator('do')
    def do_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('merge', 'rebase', 'rebase-merge', 'squash', 'manually-merged'):
            raise ValueError("must be one of enum values ('merge', 'rebase', 'rebase-merge', 'squash', 'manually-merged')")
        return value

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
        """Create an instance of MergePullRequestOption from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MergePullRequestOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Do": obj.get("Do"),
            "MergeCommitID": obj.get("MergeCommitID"),
            "MergeMessageField": obj.get("MergeMessageField"),
            "MergeTitleField": obj.get("MergeTitleField"),
            "delete_branch_after_merge": obj.get("delete_branch_after_merge"),
            "force_merge": obj.get("force_merge"),
            "head_commit_id": obj.get("head_commit_id"),
            "merge_when_checks_succeed": obj.get("merge_when_checks_succeed")
        })
        return _obj



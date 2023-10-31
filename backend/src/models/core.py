"""Core data that exist in all Models."""

# Standard library imports
from datetime import datetime
from enum import Enum
from typing import Optional

# Third party imports
from pydantic import BaseModel, validator


class CoreModel(BaseModel):
    """Any common logic to be shared by all models."""

    pass


class IDModelMixin(BaseModel):
    """ID data."""

    id: str


class DateTimeModelMixin(BaseModel):
    """Datetime model data."""

    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    @validator("created_at", "updated_at", pre=True)
    def default_datetime(self, value: datetime) -> datetime:
        """Validate both created_at and update_at data."""
        return value or datetime.now()


class Gender(str, Enum):
    """Gender data."""

    Male = "Male"
    Female = "Female"


class GenderModelMixin(BaseModel):
    """Gender mixin data"""

    sex: Gender

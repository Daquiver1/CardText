"""Legon Student Card Models"""

from datetime import datetime
from src.models.core import CoreModel, DateTimeModelMixin, GenderModelMixin


class LegonStudentCard(CoreModel, GenderModelMixin, DateTimeModelMixin):
    """Legon Student Card Model"""

    name: str
    student_id: str
    program: str
    college: str
    date_of_issuance: datetime
    date_of_expiry: datetime

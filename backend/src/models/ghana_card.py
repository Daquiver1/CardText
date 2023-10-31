"""Ghana Card Models"""

from datetime import datetime
from src.models.core import CoreModel, DateTimeModelMixin, GenderModelMixin


class GhanaCard(CoreModel, GenderModelMixin, DateTimeModelMixin):
    """Ghana Card Model"""

    first_name: str
    surname: str
    nationality: str
    date_of_birth: datetime
    height: float
    personal_id_number: str
    document_number: str
    place_of_issuance: str
    date_of_issuance: datetime
    date_of_expiry: datetime

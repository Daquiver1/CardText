"""create main tables.

Revision ID: d8930447d2c9
Revises:
Create Date: 2023-10-31 16:37:27.204138

"""
from typing import Optional, Sequence, Tuple, Union
from sqlalchemy import Enum


from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d8930447d2c9"
down_revision: Optional[str] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


gender_enum = Enum("Male", "Female", name="gender_enum")


def create_updated_at_trigger() -> None:
    """Update timestamp trigger."""
    op.execute(
        """
        CREATE OR REPLACE FUNCTION update_updated_at_column()
            RETURNS TRIGGER AS
        $$
        BEGIN
            NEW.updated_at = now();
            RETURN NEW;
        END;
        $$ language 'plpgsql';
        """
    )


def timestamps(indexed: bool = False) -> Tuple[sa.Column, sa.Column]:
    """Create timestamp in DB."""
    return (
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
            index=indexed,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
            index=indexed,
        ),
    )


def create_ghana_card_table() -> None:
    """Create ghana card table."""
    op.create_table(
        "ghana_card",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String(50), nullable=False),
        sa.Column("surname", sa.String(50), nullable=False),
        sa.Column("nationality", sa.String(50), nullable=False),
        sa.Column("sex", gender_enum, nullable=False),
        sa.Column("height", sa.Numeric, nullable=False),
        sa.Column("date_of_birth", sa.Date, nullable=False),
        sa.Column("personal_id_number", sa.String(50), nullable=False),
        sa.Column("document_number", sa.String(50), nullable=False),
        sa.Column("place_of_issuance", sa.String(50), nullable=False),
        sa.Column("date_of_issuance", sa.Date, nullable=False),
        sa.Column("date_of_expiry", sa.Date, nullable=False),
        *timestamps(),
    )
    op.execute(
        """
        CREATE TRIGGER update_user_modtime
            BEFORE UPDATE
            ON ghana_card
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column()
        """
    )


def create_legon_student_card_table() -> None:
    """Create legon student card table."""
    op.create_table(
        "legon_student_card",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("student_id", sa.String(8), nullable=False),
        sa.Column("sex", gender_enum, nullable=False),
        sa.Column("program", sa.String(50), nullable=False),
        sa.Column("college", sa.String(50), nullable=False),
        sa.Column("date_of_issuance", sa.Date),
        sa.Column("date_of_expiry", sa.Date),
        *timestamps(),
    )
    op.execute(
        """
        CREATE TRIGGER update_user_modtime
            BEFORE UPDATE
            ON legon_student_card
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column()
        """
    )


def upgrade() -> None:
    """Upgrade database."""
    create_updated_at_trigger()
    create_ghana_card_table()
    create_legon_student_card_table()


def downgrade() -> None:
    """Downgrade database."""
    op.drop_table("ghana_card")
    op.drop_table("legon_student_card")
    op.execute("DROP FUNCTION update_updated_at_column")

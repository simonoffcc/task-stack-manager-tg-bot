import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .stack import Stack


class Task(Base):

    text: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=False
    )

    stack_rel: Mapped[list[Stack]] = relationship(
        back_populates='task_rel'
    )

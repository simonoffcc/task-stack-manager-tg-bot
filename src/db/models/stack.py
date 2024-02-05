import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .user import User
from .task import Task


class Stack(Base):
    user: Mapped[int] = mapped_column(
        sa.ForeignKey('users.id')
    )
    task: Mapped[int] = mapped_column(
        sa.ForeignKey('tasks.id')
    )

    user_rel: Mapped[User] = relationship(
        back_populates='stack_rel'
    )
    task_rel: Mapped[Task] = relationship(
        back_populates='stack_rel'
    )

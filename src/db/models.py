from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    user_name = mapped_column(String(32))
    
    stack_rel: Mapped[list['Stack']] = relationship(back_populates='user_rel')


class Task(Base):
    __tablename__ = 'tasks'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(200))

    stack_rel: Mapped[list['Stack']] = relationship(back_populates='task_rel')
    

class Stack(Base):
    __tablename__ = 'stack'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    task: Mapped[int] = mapped_column(ForeignKey('tasks.id'))
    
    user_rel: Mapped['User'] = relationship(back_populates='stack_rel')
    task_rel: Mapped['Task'] = relationship(back_populates='stack_rel')

"""Data Structures.

This file contains TypedDict structure to store data which will
transfer throw Dispatcher->Middlewares->Handlers.
"""

from typing import TypedDict

from aiogram import Bot
from sqlalchemy.ext.asyncio import AsyncEngine

from src.db.database import Database


class TransferData(TypedDict):

    engine: AsyncEngine
    db: Database
    bot: Bot

from src.db.models import User, TaskType, Task, Basket
from src.db.models import async_session

from sqlalchemy import select, update, delete


async def get_categories():
    async with async_session() as session:
        categories = await session.scalars(select(TaskType))
        return categories


async def get_items_by_category(category_id: int):
    async with async_session() as session:
        items = await session.scalars(select(Task).where(Task.category == category_id))
        return items


async def get_item_by_id(item_id: int):
    async with async_session() as session:
        item = await session.scalar(select(Task).where(Task.id == item_id))
        return item

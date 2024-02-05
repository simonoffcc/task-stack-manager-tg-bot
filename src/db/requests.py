from src.db.models import User, Task, Stack
from src.db.models import async_session

from sqlalchemy import select, update, delete


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def set_item(data):
    async with async_session() as session:
        session.add(Task(**data))
        await session.commit()


async def set_stack(tg_id, item_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        session.add(Stack(user=user.id, item=item_id))
        await session.commit()


async def get_stack(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        basket = await session.scalars(select(Stack).where(Stack.user == user.id))
        return basket


async def get_users():
    async with async_session() as session:
        users = await session.scalars(select(User))
        return users


async def get_item_by_id(item_id: int):
    async with async_session() as session:
        item = await session.scalar(select(Task).where(Task.id == item_id))
        return item


async def delete_stack(tg_id, item_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        await session.execute(delete(Stack).where(Stack.user == user.id, Stack.task == item_id))
        await session.commit()

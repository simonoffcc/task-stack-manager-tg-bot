from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.keyboards import menu_board
from src.db import User

router = Router()


@router.message(CommandStart())
@router.callback_query(F.data == "main_menu")
async def start(message: Message | CallbackQuery, session: AsyncSession) -> None:
    user = await session.scalar(select(User).where(User.tg_id == message.from_user.id))
    if not user:
        session.add(User(tg_id=message.from_user.id, user_name=message.from_user.username))
        await session.commit()

    pattern = {
        "text": "Добро пожаловать в главное меню!",
        "reply_markup": menu_board
    }

    if isinstance(message, CallbackQuery):
        await message.answer()
        await message.message.edit_text(**pattern)
    else:
        await message.answer(**pattern)


# Other commands for user...

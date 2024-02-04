from datetime import datetime
from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import User
from .abstract import Repository


class UserRepo(Repository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(type_model=User, session=session)

    async def new(
        self,
        user_id: int,
        user_name: str | None = None,
        reg_date: datetime = datetime.now(),
    ) -> None:

        await self.session.merge(
            User(
                user_id=user_id,
                user_name=user_name,
                reg_date=reg_date,
            )
        )

    async def get_institute_abbr(self, user_id: int) -> str | None:
        """Get user name by telegram id."""
        query = select(User.user_name).where(User.user_id == user_id).limit(1)
        return await self.session.scalar(query)

    async def is_user_exists(self, user_id: int) -> bool:
        """Check if a user with the given user_id exists in the database."""
        query = select(exists().where(User.user_id == user_id))
        return await self.session.scalar(query)

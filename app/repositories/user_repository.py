from app.models.user_model import UserModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: UserModel):
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_by_email(self, email: str):
        result = await self.session.execute(select(UserModel).where(UserModel.email == email))
        return result.scalar_one_or_none()

    async def get_all(self):
        result = await self.session.execute(select(UserModel))
        return result.scalars().all()

    async def get_by_id(self, user_id: int):
        result = await self.session.execute(select(UserModel).where(UserModel.id == user_id))
        return result.scalar_one_or_none()

    async def update(self, user: UserModel, data: dict):
        for key, value in data.items():
            setattr(user, key, value)
        await self.session.commit()
        return user

    async def delete(self, user: UserModel):
        await self.session.delete(user)
        await self.session.commit()

    async def get_all_logins(self):
        result = await self.session.execute(select(UserModel))
        return result.scalars().all()

    async def get_login_by_id(self, user_id: int):
        result = await self.session.execute(select(UserModel).where(UserModel.id == user_id))
        return result.scalar_one_or_none()

    async def update_login(self, user_id: int, data: dict):
        user = await self.get_by_id(user_id)
        if not user:
            return None
        for key, value in data.items():
            setattr(user, key, value)
        await self.session.commit()
        return user

    async def delete_login(self, user_id: int):
        user = await self.get_by_id(user_id)
        if not user:
            return None
        await self.session.delete(user)
        await self.session.commit()
        return user

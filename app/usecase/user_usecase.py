from passlib.hash import bcrypt
from app.models.user_model import UserModel
from app.repositories.user_repository import UserRepository
from app.core.auth import create_access_token

class UserUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def register(self, name: str, email: str, password: str):
        if await self.repo.get_by_email(email):
            raise ValueError("Email já registrado")
        hashed_pw = bcrypt.hash(password)
        user = UserModel(name=name, email=email, password=hashed_pw)
        return await self.repo.create(user)

    async def login(self, email: str, password: str):
        user = await self.repo.get_by_email(email)
        if not user or not bcrypt.verify(password, user.password):
            raise ValueError("Credenciais inválidas")
        token = create_access_token({"sub": user.email})
        return {"access_token": token}

    async def get_all_users(self):
        return await self.repo.get_all()

    async def get_user_by_id(self, user_id: int):
        return await self.repo.get_by_id(user_id)

    async def update_user(self, user_id: int, data: dict):
        user = await self.repo.get_by_id(user_id)
        if not user:
            raise ValueError("Usuário não encontrado")
        return await self.repo.update(user, data)

    async def delete_user(self, user_id: int):
        user = await self.repo.get_by_id(user_id)
        if not user:
            raise ValueError("Usuário não encontrado")
        return await self.repo.delete(user)

    async def get_all_logins(self):
        return await self.repo.get_all_logins()

    async def get_login_by_id(self, user_id):
        user = await self.repo.get_login_by_id(user_id)
        if not user:
            raise ValueError("Login não encontrado")
        return user

    async def update_login(self, user_id, data):
        user = await self.repo.update_login(user_id, data)
        if not user:
            raise ValueError("Login não encontrado")
        return user

    async def delete_login(self, user_id):
        user = await self.repo.delete_login(user_id)
        if not user:
            raise ValueError("Login não encontrado")
        return


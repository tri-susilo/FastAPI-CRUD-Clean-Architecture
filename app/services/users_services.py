from app.repositories.user_repositories import UserRepository
from app.schemas.user_schemas import UserCreate, UserUpdate
from app.models.users import User
from sqlmodel import Session
from typing import List, Optional

class UserService:

    def __init__(self, session: Session):
        self.repo = UserRepository(session)

    def get_users(self) -> List[User]:
        return self.repo.get_all()

    def get_user(self, user_id: int) -> Optional[User]:
        return self.repo.get_by_id(user_id)

    def create_user(self, user_data: UserCreate) -> User:
        return self.repo.create(user_data)

    def update_user(self, user_id: int, user_data: UserUpdate) -> Optional[User]:
        return self.repo.update(user_id, user_data)

    def delete_user(self, user_id: int) -> bool:
        return self.repo.delete(user_id)

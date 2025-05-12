from sqlmodel import Session, select
from app.models.users import User
from app.schemas.user_schemas import UserCreate, UserUpdate
from typing import List, Optional

class UserRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[User]:
        return self.session.exec(select(User)).all()

    def get_by_id(self, user_id: int) -> Optional[User]:
        statement = select(User).where(User.id == user_id)
        return self.session.exec(statement).first()

    def create(self, user_data: UserCreate) -> User:
        user = User(**user_data.dict())
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def update(self, user_id: int, user_data: UserUpdate) -> Optional[User]:
        user = self.get_by_id(user_id)
        if not user:
            return None
        user_data_dict = user_data.dict(exclude_unset=True)
        for key, value in user_data_dict.items():
            setattr(user, key, value)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete(self, user_id: int) -> bool:
        user = self.get_by_id(user_id)
        if not user:
            return False
        self.session.delete(user)
        self.session.commit()
        return True

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.core.database import get_session
from sqlmodel import Session
from app.services.users_services import UserService
from app.schemas.user_schemas import UserCreate, UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])

def get_user_service(session: Session = Depends(get_session)):
    return UserService(session)

@router.get("/", response_model=List[UserRead])
def list_users(service: UserService = Depends(get_user_service)):
    return service.get_users()

def get_user_service(session: Session = Depends(get_session)):
    return UserService(session)

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user)

@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, user: UserUpdate, service: UserService = Depends(get_user_service)):
    updated = service.update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    deleted = service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")

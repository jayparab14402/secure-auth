from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import db_session
from services.userservice import Users
from schemas.auth import UserResponse, UserCreate
from models import User


router = APIRouter()

def map_user_to_response(user: User) -> UserResponse:
    print(user, "&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print(type(user), "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(dir(user))
    return UserResponse(
        id=user.id,
        email=user.email,
        username=user.username,
        full_name=user.full_name,
        is_active=user.is_active,
        is_verified=user.is_verified,
        created_at=user.created_at
        # roles=[role.name for role in user.roles]  # <-- convert Role objects to string
    )

@router.post("/register")
def register_user(user_data: UserCreate, response_model=UserResponse,  db: Session = Depends(db_session)):
    create_user = Users.create_user(user_data, db)
    return map_user_to_response(create_user)
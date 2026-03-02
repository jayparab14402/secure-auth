from fastapi import APIRouter
from api.v1.endpoints import auth, user

app_router = APIRouter()

app_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
app_router.include_router(user.sub_router, prefix="/user", tags=["user"])

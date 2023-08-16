from fastapi import APIRouter

from .user.routers import user_router
from .auth.routers import auth_router
from .logs.routers import logs_router

api_router = APIRouter()

api_router.include_router(user_router, prefix="/users")
api_router.include_router(auth_router, prefix="/auth")
api_router.include_router(logs_router, prefix="/logs")

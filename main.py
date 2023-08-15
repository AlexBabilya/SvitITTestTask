from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer


from database import engine, Base
from modules.routers import api_router

app = FastAPI()

Base.metadata.create_all(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(api_router, prefix="/api")
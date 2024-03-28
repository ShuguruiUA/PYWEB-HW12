from fastapi import APIRouter, HTTPException, Depends, status, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm, HTTPAuthorizationCredentials, HTTPBearer


from src.database.db import get_db
from src.repository import users as rep_users
from src.schemas.user import UserSchema, TokenSchema, UserResponseSchema

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post("/signup")
async def signup(body: UserSchema, db: AsyncSession = Depends(get_db)):
    pass
    return {}

@router.post("/login")
async def login(body: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    pass
    return {} # "access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"

@router.get("/refresh_token")
async def refresh_token(credentials: HTTPAuthorizationCredentials, db: AsyncSession = Depends(get_db)):
    pass
    return {}
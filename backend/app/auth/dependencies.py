"""FastAPI dependencies for extracting/validating the current user from a JWT."""
from bson import ObjectId
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.auth.jwt_handler import decode_token
from app.database import get_db

# HTTPBearer (not OAuth2PasswordBearer) - our /api/auth/login endpoint takes
# a JSON body {email, password}, not an OAuth2 form-encoded username/password
# grant, so OAuth2PasswordBearer's built-in Swagger "Authorize" form would
# never actually work against it. HTTPBearer instead shows a simple
# paste-your-token box in /docs, which matches how this API is really used.
bearer_scheme = HTTPBearer()

CREDENTIALS_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: AsyncIOMotorDatabase = Depends(get_db),
) -> dict:
    token = credentials.credentials
    try:
        payload = decode_token(token)
        if payload.get("type") != "access":
            raise CREDENTIALS_EXCEPTION
        user_id = payload.get("sub")
        if user_id is None:
            raise CREDENTIALS_EXCEPTION
    except JWTError:
        raise CREDENTIALS_EXCEPTION

    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if user is None:
        raise CREDENTIALS_EXCEPTION
    user["_id"] = str(user["_id"])
    return user


async def get_current_admin(current_user: dict = Depends(get_current_user)) -> dict:
    if current_user.get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    return current_user

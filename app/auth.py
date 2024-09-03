from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.crud import user as user_crud
from app.database import get_db
from app.schemas.user import User

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


async def get_current_user(
    db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        email: str = payload.get('sub')
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await user_crud.get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    return user


@router.get('/users/me', response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

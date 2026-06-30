from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from bson import ObjectId
from auth_utils import SECRET_KEY, ALGORITHM

# Satpam ini otomatis memunculkan tombol "Authorize" gembok di Swagger UI
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token tidak valid atau sudah kedaluwarsa! Silakan login kembali.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Dekode token JWT menggunakan Secret Key kita
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: str = payload.get("user_id")
        
        if username is None or user_id is None:
            raise credentials_exception
            
        return {"username": username, "user_id": user_id}
        
    except jwt.PyJWTError:
        raise credentials_exception
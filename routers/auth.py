from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm  # 📌 Tambahkan impor ini
from bson import ObjectId
from database import database
from schemas import UserCreate, UserOut, Token
from auth_utils import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])
user_collection = database.get_collection("users")

# 1. Endpoint Registrasi Pengguna (Tetap menggunakan JSON biasa)
@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register_user(user_data: UserCreate):
    existing_user = await user_collection.find_one({"username": user_data.username})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username sudah digunakan oleh orang lain!"
        )
    
    hashed_pwd = hash_password(user_data.password)
    new_user = {
        "username": user_data.username,
        "password": hashed_pwd
    }
    
    result = await user_collection.insert_one(new_user)
    return {
        "id": str(result.inserted_id),
        "username": user_data.username
    }

# 2. Endpoint Login Pengguna (DIUBAH agar mendukung tombol gembok Swagger)
@router.post("/login", response_model=Token)
async def login_user(user_data: OAuth2PasswordRequestForm = Depends()):
    # OAuth2PasswordRequestForm otomatis membaca input 'username' dan 'password' dari Form Data
    user = await user_collection.find_one({"username": user_data.username})
    
    if not user or not verify_password(user_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username atau password salah!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(
        data={"sub": user["username"], "user_id": str(user["_id"])}
    )
    
    return {"access_token": access_token, "token_type": "bearer"}
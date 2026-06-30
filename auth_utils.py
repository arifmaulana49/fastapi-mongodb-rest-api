import os
from datetime import datetime, timedelta
import bcrypt
import jwt
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "SUPER_SECRET_KEY_YANG_SANGAT_RAHASIA_123")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 1. Fungsi mengacak password menggunakan bcrypt murni
def hash_password(password: str) -> str:
    # Ubah string password menjadi bytes
    password_bytes = password.encode('utf-8')
    # Generate salt dan acak password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    # Kembalikan dalam bentuk string agar bisa disimpan di MongoDB
    return hashed.decode('utf-8')

# 2. Fungsi mencocokkan password menggunakan bcrypt murni
def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_bytes = plain_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    # Cocokkan secara aman
    return bcrypt.checkpw(password_bytes, hashed_bytes)

# 3. Fungsi membuat JWT Token (Tetap sama)
def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
from pydantic import BaseModel, EmailStr
from typing import Optional

# =====================================================================
# 📌 1. SKEMA DATA UNTUK FITUR KONTAK (CONTACTS)
# =====================================================================

# Data yang dikirim oleh pengguna saat membuat kontak baru (Request Body)
class ContactCreate(BaseModel):
    name: str
    phone: str
    email: Optional[EmailStr] = None

# Format data kontak yang akan dikembalikan ke pengguna (Response Body)
class ContactOut(BaseModel):
    id: str
    name: str
    phone: str
    email: Optional[str] = ""

    # Mengizinkan Pydantic membaca data dari format objek database (seperti ORM/ODM)
    class Config:
        from_attributes = True


# =====================================================================
# 📌 2. SKEMA DATA UNTUK AUTENTIKASI & PENGGUNA (AUTH & USERS)
# =====================================================================

# Data yang dikirim oleh pengguna saat mendaftar atau login (Request Body)
class UserCreate(BaseModel):
    username: str
    password: str

# Format data pengguna yang dikembalikan setelah sukses registrasi (Response Body)
class UserOut(BaseModel):
    id: str
    username: str

    class Config:
        from_attributes = True


# =====================================================================
# 📌 3. SKEMA DATA UNTUK TOKEN DIGITAL (JWT TOKEN)
# =====================================================================

# Format respons setelah pengguna berhasil melakukan login
class Token(BaseModel):
    access_token: str
    token_type: str
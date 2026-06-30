from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class ContactCreate(BaseModel):
    nama: str = Field(..., min_length=2, max_length=50)
    telepon: str = Field(..., pattern=r"^\+?[0-9]{9,15}$")
    email: EmailStr

class ContactResponse(BaseModel):
    id: str  # Kita ubah dari int menjadi str karena MongoDB menggunakan ObjectId string
    nama: str
    telepon: str
    email: str

    class Config:
        from_attributes = True
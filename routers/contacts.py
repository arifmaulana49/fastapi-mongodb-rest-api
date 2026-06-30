from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from typing import List
import database
import schemas

router = APIRouter(
    prefix="/kontak",
    tags=["Contacts"]
)

# Helper function untuk mengubah format data MongoDB ke Schema Pydantic
def contact_helper(contact) -> dict:
    return {
        "id": str(contact["_id"]),
        "nama": contact["nama"],
        "telepon": contact["telepon"],
        "email": contact["email"]
    }

# 1. POST: Membuat Kontak Baru ke Cloud
@router.post("", response_model=schemas.ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(contact: schemas.ContactCreate):
    contact_dict = contact.model_dump()
    # Simpan ke MongoDB Atlas
    new_contact = await database.contact_collection.insert_one(contact_dict)
    # Ambil data yang baru saja dimasukkan
    created_contact = await database.contact_collection.find_one({"_id": new_contact.inserted_id})
    return contact_helper(created_contact)

# 2. GET: Mengambil Semua Kontak dari Cloud
@router.get("", response_model=List[schemas.ContactResponse])
async def get_all_contacts():
    contacts = []
    async for contact in database.contact_collection.find():
        contacts.append(contact_helper(contact))
    return contacts

# 3. DELETE: Menghapus Kontak berdasarkan ID
@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(contact_id: str):
    if not ObjectId.is_valid(contact_id):
        raise HTTPException(status_code=400, detail="Format ID tidak valid")
        
    delete_result = await database.contact_collection.delete_one({"_id": ObjectId(contact_id)})
    
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Kontak tidak ditemukan")
    return None
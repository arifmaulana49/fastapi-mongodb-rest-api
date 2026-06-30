from fastapi import APIRouter, Depends, status, Query, HTTPException
from typing import List
from bson import ObjectId
from database import database
from schemas import ContactCreate, ContactOut
from dependencies import get_current_user

router = APIRouter(prefix="/contacts", tags=["Contacts"])
contact_collection = database.get_collection("contacts")

# =====================================================================
# 1. [CREATE] MEMBUAT KONTAK BARU
# =====================================================================
@router.post("/", response_model=ContactOut, status_code=status.HTTP_201_CREATED)
async def create_contact(
    contact_data: ContactCreate, 
    current_user: dict = Depends(get_current_user)
):
    new_contact = {
        "name": contact_data.name,
        "phone": contact_data.phone,
        "email": contact_data.email,
        "user_id": current_user["user_id"]
    }
    
    result = await contact_collection.insert_one(new_contact)
    
    return {
        "id": str(result.inserted_id),
        "name": contact_data.name,
        "phone": contact_data.phone,
        "email": contact_data.email
    }

# =====================================================================
# 2. [READ] DAFTAR KONTAK + SEARCH & PAGINATION
# =====================================================================
@router.get("/", response_model=List[ContactOut])
async def get_contacts(
    current_user: dict = Depends(get_current_user),
    name: str = Query(None, description="Cari nama kontak (case-insensitive)"),
    skip: int = Query(0, ge=0, description="Jumlah data awal yang dilewati"),
    limit: int = Query(10, ge=1, le=100, description="Maksimal data yang diambil")
):
    query_filter = {"user_id": current_user["user_id"]}
    
    if name:
        query_filter["name"] = {"$regex": name, "$options": "i"}
    
    cursor = contact_collection.find(query_filter).skip(skip).limit(limit)
    
    contacts = []
    async for document in cursor:
        document["id"] = str(document["_id"])
        contacts.append(document)
        
    return contacts

# =====================================================================
# 3. [READ DETAIL] MENGAMBIL SATU KONTAK BERDASARKAN ID
# =====================================================================
@router.get("/{contact_id}", response_model=ContactOut)
async def get_contact_by_id(
    contact_id: str,
    current_user: dict = Depends(get_current_user)
):
    if not ObjectId.is_valid(contact_id):
        raise HTTPException(status_code=400, detail="Format ID kontak tidak valid!")
        
    contact = await contact_collection.find_one({
        "_id": ObjectId(contact_id),
        "user_id": current_user["user_id"]
    })
    
    if not contact:
        raise HTTPException(status_code=404, detail="Kontak tidak ditemukan!")
        
    contact["id"] = str(contact["_id"])
    return contact

# =====================================================================
# 4. [UPDATE] MEMPERBARUI DATA KONTAK
# =====================================================================
@router.put("/{contact_id}", response_model=ContactOut)
async def update_contact(
    contact_id: str,
    contact_data: ContactCreate,
    current_user: dict = Depends(get_current_user)
):
    if not ObjectId.is_valid(contact_id):
        raise HTTPException(status_code=400, detail="Format ID kontak tidak valid!")
        
    updated_fields = {
        "name": contact_data.name,
        "phone": contact_data.phone,
        "email": contact_data.email
    }
    
    result = await contact_collection.update_one(
        {"_id": ObjectId(contact_id), "user_id": current_user["user_id"]},
        {"$set": updated_fields}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Kontak tidak ditemukan atau Anda tidak memiliki akses!")
        
    return {
        "id": contact_id,
        **updated_fields
    }

# =====================================================================
# 5. [DELETE] MENGHAPUS KONTAK
# =====================================================================
@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(
    contact_id: str,
    current_user: dict = Depends(get_current_user)
):
    if not ObjectId.is_valid(contact_id):
        raise HTTPException(status_code=400, detail="Format ID kontak tidak valid!")
        
    result = await contact_collection.delete_one({
        "_id": ObjectId(contact_id),
        "user_id": current_user["user_id"]
    })
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Kontak tidak ditemukan atau Anda tidak memiliki akses!")
        
    return None
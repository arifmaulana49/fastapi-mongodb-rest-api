from fastapi import APIRouter, HTTPException, status, Depends
from bson import ObjectId
from database import database
from schemas import ContactCreate, ContactOut
from dependencies import get_current_user  # 📌 Impor satpam kita di sini

router = APIRouter(prefix="/contacts", tags=["Contacts"])
contact_collection = database.get_collection("contacts")

# Helper untuk format data MongoDB Atlas
def contact_helper(contact) -> dict:
    return {
        "id": str(contact["_id"]),
        "name": contact["name"],
        "phone": contact["phone"],
        "email": contact.get("email", ""),
    }

# 1. CREATE: Menambah kontak (Otomatis terikat ke User ID yang login)
@router.post("/", response_model=ContactOut, status_code=status.HTTP_201_CREATED)
async def create_contact(contact: ContactCreate, current_user: dict = Depends(get_current_user)):
    new_contact = contact.dict()
    # 📌 KUNCI UTAMA: Ikat kontak ini dengan User ID pemiliknya!
    new_contact["owner_id"] = current_user["user_id"]
    
    result = await contact_collection.insert_one(new_contact)
    inserted_contact = await contact_collection.find_one({"_id": result.inserted_id})
    return contact_helper(inserted_contact)

# 2. READ ALL: Mengambil semua kontak (HANYA milik user yang sedang login!)
@router.get("/", response_model=list[ContactOut])
async def get_all_contacts(current_user: dict = Depends(get_current_user)):
    contacts = []
    # 📌 KUNCI UTAMA: Cari kontak yang field 'owner_id'-nya sama dengan ID user saat ini
    async for contact in contact_collection.find({"owner_id": current_user["user_id"]}):
        contacts.append(contact_helper(contact))
    return contacts

# 3. DELETE: Menghapus kontak secara aman
@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(contact_id: str, current_user: dict = Depends(get_current_user)):
    if not ObjectId.is_valid(contact_id):
        raise HTTPException(status_code=400, detail="Format ID Kontak tidak valid!")
        
    # 📌 KUNCI UTAMA: Pastikan data yang dihapus adalah miliknya sendiri
    result = await contact_collection.delete_one({
        "_id": ObjectId(contact_id), 
        "owner_id": current_user["user_id"]
    })
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Kontak tidak ditemukan atau Anda tidak berwenang!")
    return
import os
from dotenv import load_dotenv
import motor.motor_asyncio

# Muat variabel dari file .env di lokal komputer kamu
load_dotenv()

# Ambil string koneksi dari environment variable
MONGO_DETAILS = os.getenv("MONGO_DETAILS")

# Proteksi: Jika .env gagal dimuat, beri peringatan tegas di terminal
if not MONGO_DETAILS:
    raise ValueError("CRITICAL ERROR: Variabel 'MONGO_DETAILS' tidak ditemukan di file .env lokal Anda!")

# Inisialisasi client database secara asinkron
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# Hubungkan ke database 'buku_kontak'
database = client.buku_kontak
contact_collection = database.get_collection("contacts")
user_collection = database.get_collection("users")
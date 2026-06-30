import os
from dotenv import load_dotenv
import motor.motor_asyncio

# Muat variabel dari file .env
load_dotenv()

# Ambil string koneksi dari environment variable
MONGO_DETAILS = os.getenv("MONGO_DETAILS")

# Inisialisasi client database secara asinkron
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# Hubungkan ke database 'buku_kontak'
database = client.buku_kontak
contact_collection = database.get_collection("contacts")
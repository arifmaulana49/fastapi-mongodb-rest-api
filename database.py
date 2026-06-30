from motor.motor_asyncio import AsyncIOMotorClient

# 📌 PASTE CONNECTION STRING KAMU DI SINI
# Ganti <db_password> dengan password asli dari user maulanaarif1904_db_user
MONGO_DETAILS = "mongodb+srv://maulanaarif1904_db_user:Gamers99@cluster0.oqb9qkw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = AsyncIOMotorClient(MONGO_DETAILS)

# Membuat atau menggunakan database bernama 'buku_kontak'
database = client.buku_kontak

# Membuat atau menggunakan collection (tabel) bernama 'contacts'
contact_collection = database.get_collection("contacts")
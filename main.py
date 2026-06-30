from fastapi import FastAPI
from routers import contacts

app = FastAPI(
    title="Contact API with MongoDB Atlas",
    description="API Kontak Cloud Berbasis NoSQL Async menggunakan Motor & MongoDB",
    version="2.0.0"
)

# Daftarkan router
app.include_router(contacts.router)
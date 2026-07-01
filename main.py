from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from routers import contacts
from routers import auth
import os

app = FastAPI(
    title="API Kontak Cloud Berbasis NoSQL Async",
    description="Menggunakan Motor & MongoDB Atlas dengan Sistem Keamanan JWT Token",
    version="1.0.0"
)

# Konfigurasi CORS (dipertahankan agar fleksibel jika ke depan butuh akses dari app mobile)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Menentukan path absolut folder 'templates' secara dinamis
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# 📌 Menampilkan Halaman Login (index.html) saat mengakses URL utama http://127.0.0.1:8000/
@app.get("/", response_class=FileResponse, include_in_schema=False)
async def login_page():
    file_path = os.path.join(TEMPLATES_DIR, "index.html")
    return FileResponse(file_path)

# 📌 Menampilkan Halaman Dashboard saat diakses lewat URL http://127.0.0.1:8000/app
@app.get("/app", response_class=FileResponse, include_in_schema=False)
async def dashboard_page():
    file_path = os.path.join(TEMPLATES_DIR, "dashboard.html")
    return FileResponse(file_path)

# Mendaftarkan router API backend
app.include_router(contacts.router)
app.include_router(auth.router)
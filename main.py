from fastapi import FastAPI
from fastapi.responses import HTMLResponse 
from fastapi.middleware.cors import CORSMiddleware  # 📌 Impor middleware CORS
from routers import contacts
from routers import auth

app = FastAPI(
    title="API Kontak Cloud Berbasis NoSQL Async",
    description="Menggunakan Motor & MongoDB Atlas dengan Sistem Keamanan JWT Token",
    version="1.0.0"
)

# 🌐 KUNCI UTAMA: Konfigurasi CORS agar Aplikasi Frontend (Live Server) bisa mengakses API ini
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Mengizinkan akses dari domain mana pun (termasuk localhost kamu)
    allow_credentials=True,
    allow_methods=["*"],  # Mengizinkan semua metode HTTP (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Mengizinkan semua Headers data (termasuk Authorization token)
)

# Menampilkan halaman HTML interaktif saat URL utama diakses
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def home_page():
    return """
    <html>
        <head>
            <title>Contact API Production</title>
            <style>
                body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding: 50px; background-color: #f4f6f9; color: #333; }
                .card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); display: inline-block; }
                h1 { color: #4CAF50; }
                a { display: inline-block; margin-top: 20px; padding: 10px 20px; background-color: #008CBA; color: white; text-decoration: none; border-radius: 5px; }
                a:hover { background-color: #007B9A; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🚀 Contact API Sukses Mengudara!</h1>
                <p>Selamat datang! API sistem manajemen kontak berbasis Cloud ini telah aktif dan berjalan normal.</p>
                <p>Untuk mencoba fitur CRUD (Create, Read, Delete), silakan masuk ke halaman dokumentasi.</p>
                <a href="/docs">Buka Dokumentasi API (Swagger UI) ➡️</a>
            </div>
        </body>
    </html>
    """

app.include_router(contacts.router)
app.include_router(auth.router)
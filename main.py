from fastapi import FastAPI
from fastapi.responses import HTMLResponse  # 📌 Tambahkan import ini
from routers import contacts

app = FastAPI(
    title="Contact API with MongoDB Atlas",
    description="API Kontak Cloud Berbasis NoSQL Async menggunakan Motor & MongoDB",
    version="2.0.0"
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
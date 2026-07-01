# 📇 Contact Cloud — Advanced REST API

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=MongoDB&logoColor=white)](https://www.mongodb.com/)
[![Railway](https://img.shields.io/badge/Railway-131415?style=for-the-badge&logo=Railway&logoColor=white)](https://railway.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Contact Cloud** adalah sistem manajemen kontak modern berbasis REST API yang dirancang menggunakan pendekatan **Clean Architecture**. Sistem ini mengintegrasikan framework asynchronous performa tinggi dengan database NoSQL berbasis cloud untuk menghasilkan aplikasi yang _scalable_, aman, dan siap produksi.

---

## 🛠️ Tech Stack & Ekosistem

Aplikasi ini memanfaatkan kombinasi teknologi terbaik untuk memastikan kecepatan eksekusi dan integritas data:

- **Core Framework:** [FastAPI](https://fastapi.tiangolo.com/) — Framework Python modern dengan performa setara NodeJS & Go berkat arsitektur ASGI.
- **Database Driver:** [Motor](https://motor.readthedocs.io/) — Driver MongoDB asynchronous non-blocking untuk performa konkurensi maksimal.
- **Cloud Database:** [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) — Database NoSQL berbasis cloud dengan skema dokumen yang fleksibel.
- **Data Validation:** [Pydantic v2](https://docs.pydantic.dev/) — Validasi tipe data ketat dan serialisasi data instan pada _Request/Response Body_.
- **Security & Auth:** [PyJWT](https://pyjwt.readthedocs.io/) & [Passlib](https://passlib.readthedocs.io/) — Implementasi otentikasi aman menggunakan token _JSON Web Token_ (JWT) dan enkripsi password _Bcrypt_.
- **Application Server:** [Uvicorn](https://www.uvicorn.org/) — Server ASGI berkecepatan tinggi sebagai fondasi runtime aplikasi.

---

## 📂 Arsitektur & Struktur Folder

Proyek ini mengadopsi prinsip **Separation of Concerns (SoC)** sehingga setiap komponen memiliki batasan tanggung jawab yang jelas. Hal ini memudahkan proses kolaborasi, pengujian (_unit testing_), serta skalabilitas jangka panjang.

```text
rest-api/
│
├── routers/               # Layer Presentasi / API Endpoint Controllers
│   ├── auth.py            # Endpoint Registrasi, Login, dan Token Isu
│   └── contacts.py        # Endpoint Operasi CRUD Kontak Ber-Auth
│
├── templates/             # Layer UI / Frontend Web Interface (HTML, Tailwind CSS)
│   ├── index.html         # Halaman Otentikasi Premium (Login Interface)
│   └── dashboard.html     # Aplikasi Utama (Manajemen Kontak UI)
│
├── auth_utils.py          # Utilitas Keamanan (Hashing Bcrypt & Token JWT)
├── database.py            # Konfigurasi Koneksi Database Engine (Motor Async Client)
├── dependencies.py        # Layer Dependency Injection (Verifikasi Token & Session Auth)
├── main.py                # Entry Point Aplikasi & Inisialisasi Middleware
├── schemas.py             # Layer Validasi Skema Data (Pydantic Models)
│
├── .gitignore             # Konfigurasi Pengecualian Berkas Repositori Git
├── LICENSE                # Lisensi Hak Cipta Perangkat Lunak (MIT License)
├── README.md              # Dokumentasi Utama Proyek
└── requirements.txt       # Manajer Dependensi Proyek Python
```

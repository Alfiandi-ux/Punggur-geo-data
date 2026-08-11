🌍 Punggur Geo Data

<p align="center">
  <strong>Platform Informasi Geografis Kecamatan Punggur, Lampung Tengah</strong>
</p><p align="center">
  <a href="https://alfiandi-ux.github.io/Punggur-geo-data/">
    <img src="https://img.shields.io/badge/🌐%20Live%20Website-Punggur%20Geo%20Data-2563eb?style=for-the-badge" alt="Live Website">
  </a>
  <a href="https://github.com/Alfiandi-ux/Punggur-geo-data">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub Repository">
  </a>
</p><p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black">
  <img src="https://img.shields.io/badge/Leaflet-199900?style=flat-square&logo=leaflet&logoColor=white">
  <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white">
  <img src="https://img.shields.io/badge/GitHub%20Pages-222222?style=flat-square&logo=githubpages&logoColor=white">
</p>---

📖 Tentang Project

Punggur Geo Data adalah platform informasi geografis berbasis web yang dikembangkan untuk menyajikan informasi mengenai Kecamatan Punggur, Kabupaten Lampung Tengah, Provinsi Lampung secara lebih modern, interaktif, dan mudah diakses.

Platform ini menggabungkan data geografis, informasi wilayah, peta interaktif, serta sistem administrasi berbasis web dalam satu project.

Tujuan utama project ini adalah membuat informasi wilayah yang sebelumnya tersebar menjadi lebih mudah ditemukan dan dipahami melalui sebuah aplikasi web sederhana.

---

🌐 Live Website

"🚀 Buka Punggur Geo Data" (https://alfiandi-ux.github.io/Punggur-geo-data/)

Website dapat diakses langsung melalui GitHub Pages tanpa perlu melakukan instalasi aplikasi.

---

✨ Fitur Utama

🗺️ Peta Interaktif

Menampilkan informasi geografis wilayah Punggur melalui peta interaktif.

Fitur yang dikembangkan meliputi:

- 📍 Penanda lokasi
- 🏘️ Informasi desa/kampung
- 🌐 Koordinat geografis
- 🔎 Eksplorasi lokasi
- 🗺️ Visualisasi data geografis

---

📊 Informasi Wilayah

Menyajikan informasi yang berkaitan dengan wilayah Kecamatan Punggur, seperti:

- Profil wilayah
- Desa/kampung
- Lokasi geografis
- Informasi pendukung lainnya

Data dapat dikembangkan secara bertahap sesuai kebutuhan project.

---

🌤️ Informasi Cuaca

Project juga dikembangkan dengan fitur informasi kondisi cuaca berdasarkan lokasi.

Target informasi meliputi:

- 🌡️ Suhu
- 💧 Kelembapan
- ☁️ Kondisi cuaca
- 🌬️ Informasi atmosfer
- 🕐 Waktu pembaruan data

«🚧 Status: fitur cuaca masih dalam tahap pengembangan dan integrasi API.»

---

🔐 Dashboard Admin

Tersedia halaman administrasi untuk membantu pengelolaan data.

/admin.html

Dashboard admin menggunakan Supabase sebagai backend untuk autentikasi dan pengelolaan data.

Fitur admin dapat dikembangkan untuk:

- Menambahkan data
- Mengubah data
- Menghapus data
- Mengelola informasi lokasi
- Mengelola data wilayah

---

🧩 Teknologi

Project ini dibangun menggunakan teknologi web yang ringan dan mudah dikembangkan.

Teknologi| Penggunaan
HTML5| Struktur halaman
CSS3| Tampilan dan responsive design
JavaScript| Interaksi dan logika aplikasi
Leaflet.js| Peta interaktif
Supabase| Backend & autentikasi
JSON| Penyimpanan data lokasi
GitHub Pages| Hosting website
Python| Pengolahan data tertentu

---

🏗️ Arsitektur Sederhana

                    ┌─────────────────────┐
                    │      Pengguna       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   GitHub Pages      │
                    │   Punggur Geo Data  │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
          ┌──────────┐   ┌──────────┐   ┌──────────┐
          │   Map    │   │  Data    │   │  Cuaca   │
          │ Leaflet  │   │  JSON    │   │   API    │
          └──────────┘   └──────────┘   └──────────┘
                               │
                               ▼
                       ┌──────────────┐
                       │   Supabase   │
                       │ Auth + Data  │
                       └──────────────┘

---

📁 Struktur Repository

Punggur-geo-data/
│
├── index.html
│   └── Halaman utama aplikasi
│
├── admin.html
│   └── Dashboard administrasi
│
├── locations.json
│   └── Data lokasi geografis
│
├── supabase-config.js
│   └── Konfigurasi Supabase
│
├── docs/
│   └── Dokumentasi project
│
├── scripts/
│   └── Script pengolahan data
│
├── notebooks/
│   └── Eksplorasi dan analisis data
│
├── requirements.txt
│   └── Dependensi Python
│
├── .gitignore
│   └── Konfigurasi Git
│
├── LICENSE
│   └── Lisensi project
│
└── README.md
    └── Dokumentasi utama

---

🗺️ Fokus Wilayah

Kecamatan Punggur

Kabupaten Lampung Tengah
Provinsi Lampung
Indonesia 🇮🇩

Project ini berfokus pada penyajian data geografis dan informasi wilayah Kecamatan Punggur.

Pengembangan selanjutnya dapat mencakup:

- Batas administrasi
- Desa/kampung
- Jalan
- Fasilitas pendidikan
- Fasilitas kesehatan
- Tempat ibadah
- Fasilitas umum
- Titik penting lainnya

---

📈 Roadmap

Pengembangan project dilakukan secara bertahap.

✅ Sudah tersedia

- [x] Website utama
- [x] Peta interaktif
- [x] Data lokasi
- [x] Halaman admin
- [x] Integrasi Supabase
- [x] Deployment melalui GitHub Pages

🚧 Sedang dikembangkan

- [ ] Informasi suhu
- [ ] Informasi cuaca real-time
- [ ] Kelembapan
- [ ] Informasi kondisi atmosfer
- [ ] Penyempurnaan dashboard admin
- [ ] Pengelolaan data melalui Supabase

🔮 Rencana berikutnya

- [ ] Peta batas desa
- [ ] Statistik penduduk
- [ ] Data fasilitas umum
- [ ] Data sekolah
- [ ] Data kesehatan
- [ ] Pencarian lokasi
- [ ] Filter berdasarkan kategori
- [ ] Dashboard statistik
- [ ] Grafik data wilayah
- [ ] Progressive Web App (PWA)
- [ ] Optimasi performa dan mobile

---

🚀 Menjalankan Secara Lokal

Clone repository:

git clone https://github.com/Alfiandi-ux/Punggur-geo-data.git

Masuk ke folder:

cd Punggur-geo-data

Kemudian jalankan "index.html" menggunakan browser atau local development server.

Untuk pengembangan yang lebih nyaman, gunakan extension Live Server pada Visual Studio Code.

---

🌐 Deployment

Project menggunakan GitHub Pages sebagai hosting.

Repository:

https://github.com/Alfiandi-ux/Punggur-geo-data

Website:

https://alfiandi-ux.github.io/Punggur-geo-data/

Setelah perubahan di-push ke repository, GitHub Pages akan memperbarui website sesuai konfigurasi deployment.

---

🔐 Keamanan Supabase

Project menggunakan Supabase untuk autentikasi dan pengelolaan data.

File konfigurasi:

supabase-config.js

⚠️ Penting

Jangan pernah memasukkan credential sensitif seperti:

- "service_role key"
- password database
- secret API key
- access token pribadi

ke dalam repository publik.

Untuk aplikasi frontend, gunakan credential yang memang diperuntukkan bagi client dan pastikan Row Level Security (RLS) pada Supabase telah dikonfigurasi dengan benar.

---

📚 Data & Sumber

Data geografis dan informasi wilayah dapat berasal dari berbagai sumber.

Untuk menjaga kualitas data, setiap data yang digunakan sebaiknya memiliki:

- Nama sumber
- Tanggal pengambilan
- Format data
- Keterangan penggunaan
- Lisensi atau ketentuan penggunaan

Dokumentasi tambahan dapat ditempatkan pada folder:

docs/

---

🤝 Kontribusi

Kontribusi untuk pengembangan project sangat terbuka.

1. Fork repository

Fork repository melalui GitHub.

2. Buat branch

git checkout -b fitur-baru

3. Lakukan perubahan

Kembangkan fitur atau perbaikan yang diperlukan.

4. Commit

git add .
git commit -m "Menambahkan fitur baru"

5. Push

git push origin fitur-baru

Kemudian buat Pull Request ke repository utama.

---

🧪 Status Project

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active%20Development-orange?style=for-the-badge">
</p>Project masih dalam tahap pengembangan aktif.

Beberapa fitur, terutama informasi cuaca dan pengembangan dashboard admin, masih terus disempurnakan.

---

📄 Lisensi

Project ini menggunakan lisensi MIT.

Lihat:

LICENSE

Untuk data dari pihak ketiga, pengguna tetap bertanggung jawab untuk mengikuti lisensi dan ketentuan penggunaan dari sumber data masing-masing.

---

👨‍💻 Pengembang

Alfiandi

Punggur Geo Data

GitHub:

https://github.com/Alfiandi-ux

Repository:

https://github.com/Alfiandi-ux/Punggur-geo-data

Website:

https://alfiandi-ux.github.io/Punggur-geo-data/

---

⭐ Dukungan

Jika project ini bermanfaat, kamu dapat membantu dengan:

⭐ Memberikan Star pada repository
🐛 Melaporkan bug
💡 Mengusulkan fitur
🤝 Membantu pengembangan
📢 Membagikan project

---

<p align="center">
  <strong>🌍 Punggur Geo Data</strong>
  <br>
  <sub>Data geografis untuk mengenal Punggur lebih dekat.</sub>
</p>

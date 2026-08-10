# Punggur Geo Data

Kumpulan data dan analisis geografi Kecamatan Punggur, Kabupaten Lampung Tengah.

## Tentang Project

Repository ini berisi data geografis, titik lokasi, dan dokumentasi profil wilayah
Kecamatan Punggur — mencakup 9 desa/kampung, koordinat, serta rencana pengembangan
untuk batas poligon wilayah resmi.

## Struktur Folder

```
punggur-geo-data/
├── data/
│   ├── raw/          # data mentah (shapefile, geojson, csv asli, belum diubah)
│   └── processed/    # data hasil pembersihan/olahan, siap dipakai
├── scripts/          # kode Python/R untuk pemrosesan data
├── notebooks/        # Jupyter notebooks untuk eksplorasi & visualisasi
├── docs/             # catatan, sumber data, dokumentasi tambahan
├── README.md
└── .gitignore
```

## Sumber Data

| Dataset | Sumber | Tanggal Akses | Format |
|---|---|---|---|
| Titik lokasi Kec. Punggur, Lampung Tengah | Wikipedia, kodepos.co.id | 2026-08-10 | GeoJSON (Point) |
| _tambahkan dataset lain di sini_ | | | |

Lihat detail profil di [`docs/profil_punggur.md`](docs/profil_punggur.md).

## Cara Pakai

```bash
git clone https://github.com/username/punggur-geo-data.git
cd punggur-geo-data
pip install -r requirements.txt
```

Buka notebook di folder `notebooks/` untuk mulai eksplorasi.

## Tools

- Python — `geopandas`, `shapely`, `folium`
- Jupyter Notebook

## Lisensi

Data pribadi/eksplorasi. Sesuaikan lisensi data sesuai sumber aslinya.

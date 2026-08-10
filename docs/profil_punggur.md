# Profil Kecamatan Punggur, Lampung Tengah

## Data Administratif
- **Provinsi**: Lampung
- **Kabupaten**: Lampung Tengah
- **Jumlah desa/kampung**: 9
- **Koordinat pusat**: -5.0383, 105.2762 (5°02′18″S 105°16′34″E)

## Daftar Desa/Kampung
1. Asto Mulyo
2. Badran Sari
3. Mojo Pahit
4. Ngesti Rahayu
5. Nunggal Rejo
6. Sido Mulyo
7. Sri Sawahan (kode: 18.02.06.2003, kode pos: 34152)
8. Tanggul Angin (kode: 18.02.06.2005, kode pos: 34152)
9. Toto Katon

## Batas Wilayah (arah utara)
Punggur berbatasan di sisi utara dengan wilayah Kecamatan Pekalongan (Lampung Timur).

## Sumber Data
- [Website resmi Kecamatan Punggur](https://punggur.kec.lampungtengahkab.go.id/)
- [BPS Lampung Tengah - Kecamatan Punggur Dalam Angka](https://lampungtengahkab.bps.go.id/en/publication/2024/09/26/48b48c91c7482613a38549be/kecamatan-punggur-dalam-angka-2024.html)
- [Wikipedia - Punggur, Lampung Tengah](https://p2k.stekom.ac.id/ensiklopedia/Punggur,_Lampung_Tengah)

## Catatan Batas Poligon (Belum Termasuk)
File `punggur_points.geojson` di repo ini baru berisi titik (point), **bukan poligon batas wilayah**.
Untuk mendapatkan poligon batas kecamatan resmi, unduh dari salah satu sumber berikut:

1. **Batas Administrasi Indonesia (GitHub)** — data BIG, per kecamatan, format SHP/GeoJSON/GPKG
   https://github.com/Alf-Anas/batas-administrasi-indonesia
   Download interaktif: https://batas-admin.geoit.dev/

2. **Geoservice BIG (resmi)** — Badan Informasi Geospasial
   https://geoservices.big.go.id/

3. Cari file kabupaten **Lampung Tengah** di folder `Kecamatan/` pada repo GitHub di atas, lalu filter/extract polygon dengan properti `WADMKC = "Punggur"` menggunakan geopandas:

```python
import geopandas as gpd

gdf = gpd.read_file("Lampung_Tengah_Kecamatan.geojson")
punggur = gdf[gdf["WADMKC"] == "Punggur"]
punggur.to_file("data/processed/punggur_boundary.geojson", driver="GeoJSON")
```

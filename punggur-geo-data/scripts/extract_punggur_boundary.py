"""
Script untuk mengekstrak poligon batas Kecamatan Punggur (Lampung Tengah)
dari file GeoJSON/SHP kabupaten yang diunduh dari sumber BIG.

Langkah:
1. Download file batas kecamatan Kabupaten Lampung Tengah dari:
   https://github.com/Alf-Anas/batas-administrasi-indonesia (folder Kecamatan/)
   atau https://batas-admin.geoit.dev/
2. Simpan file hasil download ke data/raw/ (misal: lampung_tengah_kecamatan.geojson)
3. Jalankan script ini untuk filter khusus Punggur

Install dulu: pip install geopandas --break-system-packages
"""

import geopandas as gpd

INPUT_PATH = "data/raw/lampung_tengah_kecamatan.geojson"  # sesuaikan nama file
OUTPUT_PATH = "data/processed/punggur_boundary.geojson"


def extract_punggur_boundary(input_path: str, output_path: str) -> None:
    gdf = gpd.read_file(input_path)

    # Kolom nama kecamatan biasanya bernama WADMKC (standar BIG)
    if "WADMKC" not in gdf.columns:
        print("Kolom WADMKC tidak ditemukan. Kolom tersedia:", list(gdf.columns))
        return

    punggur = gdf[gdf["WADMKC"].str.contains("Punggur", case=False, na=False)]

    if punggur.empty:
        print("Kecamatan Punggur tidak ditemukan di file ini.")
        return

    punggur.to_file(output_path, driver="GeoJSON")
    print(f"Berhasil disimpan ke {output_path}")
    print(punggur[["WADMKC", "WADMKK", "WADMPR"]])


if __name__ == "__main__":
    extract_punggur_boundary(INPUT_PATH, OUTPUT_PATH)

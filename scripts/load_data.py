"""
Script starter untuk load dan cek data geografi (GeoJSON/Shapefile).
Install dulu: pip install geopandas matplotlib
"""

import geopandas as gpd
import matplotlib.pyplot as plt


def load_geo_data(filepath: str) -> gpd.GeoDataFrame:
    """Load file geojson/shapefile jadi GeoDataFrame."""
    gdf = gpd.read_file(filepath)
    print(f"Jumlah baris: {len(gdf)}")
    print(f"CRS: {gdf.crs}")
    print(f"Kolom: {list(gdf.columns)}")
    return gdf


def check_validity(gdf: gpd.GeoDataFrame) -> None:
    """Cek apakah ada geometri yang tidak valid."""
    invalid = gdf[~gdf.is_valid]
    if len(invalid) > 0:
        print(f"Ada {len(invalid)} geometri tidak valid!")
    else:
        print("Semua geometri valid.")


def quick_plot(gdf: gpd.GeoDataFrame, title: str = "Peta") -> None:
    """Plot cepat untuk preview data."""
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax, edgecolor="black", linewidth=0.3)
    ax.set_title(title)
    plt.savefig("output/preview_map.png", dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    # Ganti path sesuai file data kamu
    path = "data/raw/contoh.geojson"
    gdf = load_geo_data(path)
    check_validity(gdf)
    quick_plot(gdf, title="Preview Data Geografi")

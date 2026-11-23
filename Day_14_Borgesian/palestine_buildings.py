import duckdb
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from shapely.geometry import box

con = duckdb.connect()
con.sql("INSTALL httpfs; LOAD httpfs; INSTALL spatial; LOAD spatial;")
con.sql("SET s3_region='us-west-2';")
con.sql("SET geometry_always_xy=true;")

west, south, east, north = 34.15, 29.45, 35.95, 33.40
cache_path = Path(__file__).resolve().parent / "palestine_buildings.parquet"

print("Downloading Historic Palestine boundary from Natural Earth...")
countries = gpd.read_file(
    "https://naturalearth.s3.amazonaws.com/10m_cultural/ne_10m_admin_0_countries.zip"
)

countries_filtered = countries[
    countries["ADM0_A3"].isin(["ISR", "PSE", "PSX"])
    | countries["ADMIN"].str.contains(
        "Israel|Palestine|West Bank|Gaza", case=False, na=False
    )
    | countries["NAME"].str.contains(
        "Israel|Palestine|West Bank|Gaza", case=False, na=False
    )
].copy()

print(countries_filtered[["ADMIN", "NAME", "ADM0_A3"]])

if countries_filtered.empty:
    raise RuntimeError("Natural Earth did not return the Palestine/Israel polygons.")

palestine = countries_filtered.to_crs(epsg=4326)
boundary = palestine.dissolve()

# Trim the northeastern Golan/eastern lobe and use the natural southern boundary.
cutoff = gpd.GeoDataFrame(
    geometry=[box(west, south, 35.63, north)],
    crs="EPSG:4326",
)
boundary = gpd.overlay(boundary, cutoff, how="intersection")

if cache_path.exists():
    print(f"Loading cached buildings from {cache_path.name}...")
    df = pd.read_parquet(cache_path)
else:
    print("Querying Overture Maps cloud storage for Palestine buildings (takes ~1-2 minutes)...")

    df = con.sql(f"""
        SELECT
            (bbox.xmin + bbox.xmax) / 2.0 AS lon,
            (bbox.ymin + bbox.ymax) / 2.0 AS lat,
            ST_Area_Spheroid(geometry) AS area_m2,
            sources[1].dataset AS source
        FROM read_parquet(
            's3://overturemaps-us-west-2/release/2026-10-21.0/theme=buildings/type=building/*',
            hive_partitioning=1
        )
        WHERE bbox.xmin > {west} AND bbox.xmax < {east}
          AND bbox.ymin > {south} AND bbox.ymax < {north}
    """).df()

# Always clip cached or freshly queried points to the exact final boundary.
building_points = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df["lon"], df["lat"]),
    crs="EPSG:4326",
)

clipped = gpd.sjoin(
    building_points,
    boundary,
    predicate="within",
    how="inner",
)
clipped = clipped.drop(columns=["index_right", "geometry"])
df = clipped.copy()

# Keep the top-right cutoff for points outside the precise boundary clip.
df = df[df["lon"] <= 35.63].copy()

# Refresh the cache whenever the boundary refinement changes.
df.to_parquet(cache_path, index=False)
print(f"Saved clipped buildings to {cache_path}")

print(f"Buildings inside Historic Palestine: {len(df):,}")
print(df["source"].value_counts())

# Calculate total roof area & Borgesian 1:1 A4 sheet count
total_m2 = df["area_m2"].sum()
a4_m2 = 0.210 * 0.297
print(f"All roofs together: {total_m2 / 1e6:,.1f} km²")
print(f"A 1:1 map of all roofs would need {total_m2 / a4_m2:,.0f} A4 sheets!")

# Draw the Borgesian map (no basemap, no boundaries — only buildings)
fig, ax = plt.subplots(figsize=(9, 14), facecolor="white")
ax.scatter(
    df["lon"],
    df["lat"],
    s=0.08,
    c="black",
    alpha=0.85,
    linewidths=0,
)

minx, miny, maxx, maxy = boundary.total_bounds
ax.set_xlim(minx, maxx)
ax.set_ylim(miny, maxy)
ax.set_aspect(1.17)
ax.set_axis_off()

ax.text(
    0.98,
    0.02,
    f"{len(df):,}",
    transform=ax.transAxes,
    ha="right",
    va="bottom",
    fontsize=12,
    color="#666666",
)

plt.savefig(
    r"C:\Users\Asus\Downloads\palestine_every_building.png",
    dpi=300,
    bbox_inches="tight",
)
plt.show()
print("Saved to Downloads\\palestine_every_building.png! ✅")

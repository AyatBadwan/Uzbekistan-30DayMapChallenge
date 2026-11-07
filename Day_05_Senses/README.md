# 🏔️ Day 05: Senses - Tashkent TV Tower to Big Chimgan

A terrain visibility and topographic viewshed determination study computing the precise optical line-of-sight boundaries between the **Tashkent Television Tower** and **Big Chimgan Peak** in Uzbekistan 🇺🇿✨

---

## 📊 Technical Workflow & Analytics

### 1. Data Ingestion & Metric Reprojection
* **Terrain Grid Input:** Acquired global high-resolution **Copernicus DEM (DSM-COG 30m)** spatial tiles covering the capital and surrounding mountain ranges via GDAL.
* **Coordinate Synchronization:** Executed geographic grid transformation via `gdalwarp` from angular degrees (`EPSG:4326`) into a rigid, metric-based spatial coordinate reference system **`EPSG:32642` (WGS 84 / UTM zone 42N)** to ensure distance calculation integrity across changing elevations.

### 2. Algorithmic Visibility Computation
* **Horizon Parameters:** Run via the terminal engine `gdal_viewshed` to extract geometric visibility profiles from the TV Tower observation platforms (Height: **97m**) up to the structural apex of the region.
* **Mathematical Validation:** Extracted a confirmed visibility bitmask value of **`255`** using `gdallocationinfo` right at the peak coordinates of Big Chimgan, mathematically verifying a direct, clear line-of-sight spanning an impressive **66.7 Kilometers** across the terrain layout!

### 3. Cartographic Design & Blending (QGIS Production)
* **Base Map Canvas:** Integrated a rich, immersive **Google Satellite Imagery** background stream deployed instantly via the **HCMGIS plugin** to showcase authentic real-world infrastructure and ecological features.
* **Composite Symbology:** Pairs separate visibility rasters (`view_deck`, `view_ground`, and `view_chimgan`) categorized using **Paletted/Unique values** style rules.
* **Tonal Blend Profiles:** Re-ordered vector stacks and adjusted **Layer Rendering Blending Modes** to fuse pixel matrices into smooth neon yellow-green boundary classifications, overlaid with a structural 3D **Hillshade model** to cast soft environmental shadows.

---

## 📂 Folder Directory
* 🖼️ `Dat_05_Senses_Ayat.png`: The finalized production cartographic layout asset.
* 📄 `README.md`: This project sheet.

---
*Developed independently as part of the global #30DayMapChallenge.*

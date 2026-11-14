# 🌊 Day 08: Utopia - What if the Aral Sea Came Back (Animated Filling)

An interactive elevation-based simulation visualizing the hypothetical restoration of the **Aral Sea** across Karakalpakstan, Uzbekistan, and Kazakhstan—rising progressively from today's dry seabed back to its historic **1960 water level of 53 meters** 🇺🇿✨

<p align="center">
  <img src="Aral_Sea_Utopia.gif" alt="Animated Aral Sea Restoration GIF" width="100%">
</p>

---

## 📊 Technical Workflow & Spatial Modeling

### 1. Elevation Dataset & Coordinate Architecture
* **Source DEM:** Processed a 90m resolution **Copernicus DEM (GLO-90)** mosaic spanning the entire Aral Basin (`58°E–62°E`, `43°N–47°N`).
* **Metric Reprojection:** Projected in **`EPSG:32641` (WGS 84 / UTM zone 41N)** so every pixel corresponds to exact metric dimensions (`90 m × 90 m`) for accurate surface area measurement.
* **Satellite Basemap:** Overlaid onto true-color **NASA Terra / MODIS** imagery (August 10, 2026) streamed directly via NASA GIBS XYZ tiles.

### 2. Progressive Raster Calculator Simulation (QGIS)
Using the **QGIS Raster Calculator**, conditional elevation thresholds (`"aral_dem_90m@1" <= [elevation]`) were computed across six stages to simulate gradual basin filling:
* **Stage 0 (Today):** Dry seabed baseline (2026 satellite view).
* **Stage 1 (`30 m`):** Deepest troughs of the western and eastern basins refill (~11,700 km²).
* **Stage 2 (`35 m`):** Expansion across the central basin floor.
* **Stage 3 (`42 m`):** Matches modern Small (North) Aral Sea levels; reconnects the large southern basin (~44,700 km²).
* **Stage 4 (`46 m`):** Submerges the central land bridge around Vozrozhdeniya.
* **Stage 5 (`53 m` - 1960 Utopia):** Full historic shoreline restored (~67,600 km²), matching historical 1960 records of **66,000–68,000 km²** and reconnecting Muynak as a coastal harbor town.

### 3. Cartographic Styling & Animation
* **Symbology:** Styled binary outputs using **Paletted/Unique values**, isolating water pixels (`Value = 1`) in translucent ocean blue while removing dry land (`Value = 0`) to reveal the underlying satellite terrain.
* **GIF Synthesis:** Exported locked-extent PNG frames across all elevation stages and compiled them into an optimized looping animation.

---

## 📂 Folder Directory
* 🎞️ `ezgif.com-optimize`: Animated simulation showing water rising from dry seabed to 53m.
* 📄 `README.md`: This project documentation sheet.

---

## 🙏 Credits & Attribution
* **Elevation:** Copernicus DEM GLO-90 © DLR e.V. 2010–2014 and © Airbus Defence and Space GmbH 2014–2018, provided under COPERNICUS by the European Union and ESA.
* **Satellite Image:** NASA Worldview / Global Imagery Browse Services (GIBS), part of NASA Earthdata (EOSDIS), Terra MODIS Corrected Reflectance (True Color), 10 August 2026.
* **Software:** QGIS.

*Developed independently as part of the global #30DayMapChallenge.*

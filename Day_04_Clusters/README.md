# 🗺️ Day 04: Clusters - Tashkent Café & Restaurant Hotspots

A vibrant, high-contrast neon-glowing clustering visualization showcasing the intense density and spatial patterns of **2,408 culinary establishments** across the capital city of **Tashkent, Uzbekistan** 🇺🇿✨

---

## 📊 Technical Workflow & Design Analytics

### 1. Data Querying & Sourcing
Spatial point datasets were dynamically extracted from the OpenStreetMap server using the **Overpass Turbo API** to target active food infrastructure.
* **Geometries Isolated:** Production nodes containing the tags `amenity=cafe`, `amenity=restaurant`, and `amenity=fast_food` within the Tashkent administrative boundary.

### 2. Cartographic Execution & Neon Styling (Kepler.gl)
* **Base Map Template:** Rendered over a customized **Dark Matter** canvas to enhance data readability and conceal background street label clutter.
* **Clustering Architecture:** Migrated the raw point spatial arrays into an advanced **Interactive Cluster Layer**:
  * **Color Ramp Hierarchy:** Applied a striking, sequential **Mint to Emerald Green** fluorescent scale representing density categories.
  * **Volumetric Light Optimization:** 
    * **Radius Configuration:** Calibrated at **`24.9` pixels** to capture organic localized density bounds across urban avenues.
    * **Opacity & Blending:** Set to a full structural **`1.0` opacity** and paired with **Additive Blending Mode (`Layer Blending: additive`)**. This enables overlapping boundaries to accumulate light energy, producing a stunning glowing neon effect over hot zones.
* **Interaction Layer:** Enabled dynamic **Hover Tooltips** showing real-time data metrics (`point count`) for concentrated hotspots.

---

## 📂 Folder Directory
* 📁 `export.geojson`: The comprehensive spatial vector layer compiled from the OSM dataset.
* 🖼️ `Tashkent_Cafes_Clusters.png`: The finalized high-resolution glowing cartographic asset.
* 📄 `README.md`: This documentation sheet.

---
*Developed independently as part of the global #30DayMapChallenge.*

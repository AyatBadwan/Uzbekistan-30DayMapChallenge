# 🏙️🌾 Day 09: Urban–Rural - City or Countryside? Ask the Satellite

An interactive cloud-based similarity search exploring the urban–rural gradient across **Tashkent, Uzbekistan**, powered by **Google's AlphaEarth Foundations Satellite Embedding** dataset and **Google Earth Engine** 🇺🇿✨

🔗 **[Run the Live Interactive Script in Google Earth Engine](https://code.earthengine.google.com/a81fbc0a935f83c6ecb27041b3b69c57)**

<p align="center">
  <img src="Tashkent_Urban_Rural.png" alt="Tashkent AlphaEarth Similarity Map" width="100%">
</p>

---

## 📊 Technical Workflow & AI Satellite Embeddings

### 1. Satellite Embedding Dataset (`AlphaEarth`)
* **Dataset ID:** `GOOGLE/SATELLITE_EMBEDDING/V1/ANNUAL` (2024 mosaic, 10 m spatial resolution).
* **64-Dimensional Fingerprints:** Each `10 × 10 m` pixel summarizes multi-sensor satellite observations (Sentinel-2 optical, Sentinel-1 radar, Landsat, and seasonal dynamics) into a 64-number vector embedding.
* **Cloud Processing:** Computed directly in the **Google Earth Engine Code Editor** across the Greater Tashkent bounding box (`[68.95, 40.95, 69.75, 41.55]`).

### 2. Dot-Product Similarity Search
* **Reference Points:** Sampled two anchor locations—an urban apartment block example in **Chilonzor** (`[69.2050, 41.2850]`) and an agricultural cotton/wheat field example southwest of the city (`[69.0600, 41.1800]`).
* **Mathematical Comparison:** Computed the dot product across all 64 embedding bands for every pixel (`similarityTo(point)`), producing scores approaching `1.0` for structurally similar landscapes and lower values for contrasting land uses.
* **Interactive Exploration:** Enabled `Map.onClick(...)` to dynamically sample any clicked location—for instance, sampling at `(69.2043, 41.2850)` yielded a **0.79** similarity score to the city versus **0.34** to the countryside.

### 3. Layer Visualizations
* **Similar to the City / Countryside:** Continuous heatmaps highlighting urban cores versus agricultural fields, while clearly isolating dark non-built features like the **Ankhor Canal**, city parks, and airport runways.
* **Binary Classification (`City vs. Countryside`):** Pixel-by-pixel comparison (`cityLike.gt(ruralLike)`) revealing how rural villages and gardens around Tashkent blend across the urban–rural boundary.

---

## 📂 Folder Directory
* 🖼️ `Screenshot 2026-11-15 191447`: Screenshot of the AlphaEarth similarity output in Google Earth Engine.
* 📄 `README.md`: This project documentation sheet.

---

## 🙏 Credits & Attribution
* **Satellite Embeddings:** The AlphaEarth Foundations Satellite Embedding dataset is produced by Google and Google DeepMind, licensed under **CC BY 4.0** (`GOOGLE/SATELLITE_EMBEDDING/V1/ANNUAL`, 2017–2024, 10 m).
* **Platform:** Google Earth Engine Code Editor.

*Developed independently as part of the global #30DayMapChallenge.*

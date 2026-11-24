# 🛰️🔴 Day 15: Inside Out — Uzbekistan in Colours Your Eyes Can't See

An interactive multispectral false-colour exploration of **Uzbekistan** built in **Google Earth Engine** using **Copernicus Sentinel-2** summer composites (`July–August 2025`) and **Google Cloud Score+**—turning invisible near-infrared (`NIR`) and short-wave infrared (`SWIR`) wavelengths into vivid colours that reveal living crops, water bodies, urban areas, and soil salinity 🇺🇿✨


🗺️ **[Explore the Interactive Map in Google Earth Engine]: https://code.earthengine.google.com/e6d94ae73959bcab2048019df95f82e2**

---

## 📊 Technical Workflow & Multispectral Processing

### 1. Cloud-Free Summer Composite (`Sentinel-2` & `Cloud Score+`)
* **Satellite Imagery:** Filtered **Copernicus Sentinel-2 Level-2A** surface reflectance (`COPERNICUS/S2_SR_HARMONIZED`) across Uzbekistan for **July and August 2025**, retaining scenes with `< 10%` cloud cover.
* **Pixel-Level Cloud Masking:** Linked Google's **Cloud Score+** dataset (`GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED`) and masked out cloudy pixels (`cs_cdf >= 0.6`), then computed a cloud-free summer `.median()` mosaic.

### 2. Five Interactive Spectral Recipes (`ui.Select`)
Built an interactive map interface allowing instant switching across key Uzbek landscapes (**Ferghana Valley**, **Tashkent**, **Samarkand**, **Bukhara oasis**, **Aydarkul Lake**, and the **Amu Darya near Nukus**) and five spectral band combinations:
* **1. True Colour (`B4, B3, B2`):** Natural-colour view as seen by human eyes from space.
* **2. Infrared — Plants Are Red (`B8, B4, B3`):** Classic false-colour composite assigning Near-Infrared (`B8`) to red—healthy irrigated fields in the **Ferghana Valley** glow bright crimson, cities appear grey-blue, and water turns deep black.
* **3. Agriculture (`B11, B8, B2`):** Highlights active crops in bright green versus bare/harvested soil in orange-brown.
* **4. Salt and Water (`B12, B11, B4`):** Uses SWIR bands to distinguish water, damp ground, and pale salinized soils.
* **5. Negative (`3000 - B4, B3, B2`):** Turns true colour "inside out," inverting bright roofs to dark and shadows/trees to light blue.

---

## 📂 Folder Directory
* 🖼️ `Ferghana_Valley_Infrared.png`: High-resolution false-colour infrared (`B8, B4, B3`) composite of the Ferghana Valley.
* 📄 `README.md`: Project documentation and spectral methodology.

---

## 🙏 Credits & Attribution
* **Satellite Imagery:** Contains modified Copernicus Sentinel data (`2025`), processed in Google Earth Engine (`COPERNICUS/S2_SR_HARMONIZED`, July–August 2025).
* **Cloud Masking:** Cloud Score+ by Google (`GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED`).
* **Software:** Google Earth Engine Code Editor.

*Developed independently as part of the global #30DayMapChallenge.*

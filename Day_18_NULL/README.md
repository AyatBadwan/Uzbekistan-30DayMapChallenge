# ☁️🛰️ Day 18: NULL — A Satellite Picture With No Holes (Tashkent & Chimgan Mountains)

An optical and radar satellite processing workflow in **Google Earth Engine** exploring how **NULL** values (`NoData`) appear when clouds are masked out of **Sentinel-2** imagery—and how multi-date compositing and **Sentinel-1 SAR radar** fill every gap over **Tashkent and the Chimgan Mountains** (`Spring 2025`) 🇺🇿✨

🗺️ **[Explore the Interactive 6-Layer Map in Google Earth Engine](https://code.earthengine.google.com/04941b744f4390fb3bd338cf2c28f96b)**

<p align="center">
  <img src="One%20cloudy%20day.jpg" alt="1. One Cloudy Day - 12 April 2025" width="32%">
  <img src="Clouds%20removed%20Null%20holes.jpg" alt="2. Clouds Removed - NULL Holes in Red" width="32%">
  <img src="Spring%2C%20clouds%20removed%2C%20no%20holes.jpg" alt="3. Spring Composite - Zero NULL Holes" width="32%">
</p>

---

## 📊 Technical Workflow & NULL Handling

### 1. Filtering Cloudy Scenes (`Sentinel-2` Spring 2025)
* **Initial Collection:** Queried **218** Copernicus Sentinel-2 Level-2A images (`COPERNICUS/S2_SR_HARMONIZED`) covering Tashkent and the Chimgan Mountains (`[69.0, 41.0, 70.3, 41.8]`) between **March 1 and June 1, 2025**.
* **Scene-Level Filtering:** Filtered out heavily clouded passes (`CLOUDY_PIXEL_PERCENTAGE < 20%`), narrowing the stack down to **114** clear-sky candidate images.

### 2. Pixel-Level Cloud Masking (`Cloud Score+` & `NULL` Holes)
* **Cloud Score+ Masking:** Linked Google's **Cloud Score+** dataset (`GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED`) and applied `updateMask(img.select('cs_cdf').gte(0.6))` to remove clouds and cloud shadows while preserving genuine mountain snow on the Chimgan peaks.
* **Visualizing NULLs:** Masking converts cloudy pixels into `NULL` (`NoData`), displayed in bright red over the **12 April 2025** scene.

### 3. Hole-Free Median Compositing & Quantitative Verification
* **Multi-Date Median (`clear.median()`):** Combined all 114 cloud-masked spring scenes pixel by pixel, replacing every `NULL` hole with clear observations from other dates—and verified via `.mask().not().reduceRegion(ee.Reducer.sum())` that **`0` NULL pixels** remained.
* **Orbit Coverage Asymmetry:** Mapped clear observations per pixel, revealing nearly twice as many clear passes on the western side (two overlapping Sentinel-2 orbital tracks) compared to the cloudier eastern mountains (single orbital track).

### 4. All-Weather Radar Comparison (`Sentinel-1 SAR`)
* **Seeing Through Clouds:** Added **56** Copernicus Sentinel-1 C-band radar scenes (`COPERNICUS/S1_GRD`, `VV, VH, VV-VH` false-colour composite) from Spring 2025, demonstrating how active microwave radar penetrates cloud cover with zero `NULL` gaps—highlighting urban buildings in bright yellow-green and smooth water bodies like **Charvak Reservoir** in dark blue.

---

## 📂 Folder Directory
* 🖼️ `One cloudy day.jpg`: Raw Sentinel-2 true-colour view on a cloudy spring day (`12 April 2025`).
* 🖼️ `Clouds removed Null holes.jpg`: Cloud-masked scene revealing `NULL` (`NoData`) gaps in red while retaining mountain snow.
* 🖼️ `Spring, clouds removed, no holes.jpg`: Final hole-free Spring 2025 median composite (`0` NULL pixels).
* 📄 `README.md`: Project documentation and processing workflow.

---

## 🙏 Credits & Attribution
* **Optical & Radar Satellite Data:** Contains modified Copernicus Sentinel-1 and Sentinel-2 data (`2025`), processed in Google Earth Engine.
* **Cloud Masking:** Cloud Score+ by Google (`GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED`, Pasquarella et al., 2023).
* **Software:** Google Earth Engine Code Editor.

*Developed independently as part of the global #30DayMapChallenge.*

# 📜 Day 06: Vintage - 1913 Tashkent Historical Georeferencing

A fascinating historical exploration and vintage map alignment overlaying the **1913 Plan of the City of Tashkent** (published by Vladimir Pirogovsky) precisely onto today's modern urban canvas 🇺🇿✨


---

## 📊 Technical Workflow & Geospatial Analytics

### 1. Historical Dataset & Protocol Ingestion
* **Source Cartography:** "Plan of the City of Tashkent" (as of April 1, 1913), showcasing Tashkent's historical imperial infrastructure and its first pioneering electric tram network line.
* **IIIF Image Ingestion:** Extracted high-resolution mosaic raster tiles using the International Image Interoperability Framework (IIIF) linked via a structured JSON configuration manifest.

### 2. Digital Masking & Boundary Isolation (Allmaps Editor)
* **Outline Masking:** Utilized **Allmaps Editor** to deploy a precise vector bounding mask around the map's interior black frame line boundary.
* **Result:** Successfully sliced away vintage borders, aged margins, and paper text artifacts to ensure clean registration onto contemporary map networks.

### 3. Precision Georeferencing via GCP Matrix
* **Point Extraction:** Applied a rigid metric coordinate adjustment using 6 high-precision Ground Control Points (GCPs).
* **Historical Landmarks Aligned:** Target control fields focused on immutable geometric features:
  * Center of **Amir Timur Square** (historically Konstantinovsky Square).
  * **Kukeldash Madrasa** adjacent to the ancient Chorsu Bazaar core.
  * Major arterial transit junctions radiating from the railway terminal sector.
* **Transformation Mathematics:** Computed via a robust **Polynomial fit equation**, limiting pixel drift to under 3 pixels (< 10 real-world meters) to perfectly dock the historical ring layout over today's ring road system.

---

*Developed independently as part of the global #30DayMapChallenge.*

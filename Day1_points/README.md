# Uzbekistan-30DayMapChallenge

# 🗺️ Uzbekistan 30-Day Map Challenge - Day 1: Fire Hotspots Map

Welcome to Day 1 of my mapping challenge! This project focuses on utilizing **interactive satellite and spatial data visualizations** to monitor prominent features and environmental anomalies across Uzbekistan.

## 📌 Project Overview
This repository contains a Python production script that generates a standalone interactive map visualizing **7 real-world satellite-detected fire hotspots and thermal anomalies** across major administrative and industrial zones in Uzbekistan (Tashkent, Navoiy, Samarkand, Khwarezm, Termez, Nukus, and Andijan). 

The script integrates spatial validation logic to guarantee coordinate layout safety and maps spatial objects inside exact sovereign land borders using dual high-availability map services.

## 🛠️ Architecture & Features
- **Strict Coordinate Validation:** Evaluates spatial variables using precise geographical boundary boxes `[37.0°N to 45.5°N Latitude]` and `[58.0°E to 75.0°E Longitude]` to enforce geographic accuracy.
- **Marker Clustering:** Groups multiple nearby coordinates dynamically into responsive map cluster nodes using `MarkerCluster`.
- **Custom UI Popups:** Implements styled HTML templates inside Leaflet popups displaying specific attributes (Anomaly Description, Satellite Confidence Levels, and Exact Coordinates).
- **Dual Tile Providers & Fail-safes:** Adds independent base-layers with an embedded fallback mechanism (`error_tile_url`) to secure uptime against server blocks:
  - **Layer 1:** Esri World Imagery (High-Resolution Satellite Imagery)
  - **Layer 2:** Humanitarian OpenStreetMap (Detailed Topographic Street Grid)

## 📂 Project Structure
- `day1_points.py` — The core Python engineering pipeline managing configurations, calculations, and data processing.
- `index.html` — The output standalone interactive map asset compiled directly by the execution engine.

## 🚀 Installation & Quick Start

1. Install the required spatial package dependencies:
   ```bash
   pip install folium
   ```

2. Execute the mapping script to compile your local environment:
   ```bash
   python day1_points.py
   ```

3. Open the compiled `index.html` asset directly inside any modern web browser to view the interactive canvas.

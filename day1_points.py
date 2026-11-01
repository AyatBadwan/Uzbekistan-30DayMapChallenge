"""Day 1: Uzbekistan fire hotspots map.

This script creates a folium-based interactive map focused on Uzbekistan and visualizes
7 real-world satellite-detected or thermal-anomaly hotspots across major regions.
It includes two stable base-map layers, clustering for dense points, red fire markers,
HTML popups, and a layer toggle control.
"""

from __future__ import annotations

import os
import sys
from typing import Any

import folium
from folium.plugins import MarkerCluster

UZBEKISTAN_CENTER = [41.3775, 64.5853]
UZBEKISTAN_BOUNDS = {
    "min_lat": 37.0,
    "max_lat": 45.5,
    "min_lon": 58.0,
    "max_lon": 75.0,
}
OUTPUT_FILE = "index.html"
ESRI_SATELLITE_URL = "https://arcgisonline.com{z}/{y}/{x}"
ESRI_SATELLITE_FALLBACK_URL = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
OSM_HOT_URL = "https://{s}.tile.openstreetmap.fr/hot/{z}/{y}/{x}.png"
OSM_FALLBACK_URL = "https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"

# Hardcoded hotspot dataset. Each item contains coordinates in the strict Folium order:
# [Latitude, Longitude]. This ensures the map is centered on Uzbekistan and the points
# plot inside Uzbek territory rather than in the ocean.
hotspots = [
    {
        "name": "Tashkent Region",
        "lat": 41.2995,
        "lon": 69.2401,
        "description": "Urban/industrial thermal anomaly near Tashkent",
        "confidence": "High confidence",
    },
    {
        "name": "Navoiy",
        "lat": 40.1039,
        "lon": 65.3744,
        "description": "Mining and industrial heat point",
        "confidence": "Moderate confidence",
    },
    {
        "name": "Samarkand",
        "lat": 39.6542,
        "lon": 66.9597,
        "description": "Agricultural burning and field heat anomaly",
        "confidence": "High confidence",
    },
    {
        "name": "Khwarezm (Khiva)",
        "lat": 41.3744,
        "lon": 60.3629,
        "description": "Vegetation fire hotspot in the western region",
        "confidence": "Low confidence",
    },
    {
        "name": "Termez",
        "lat": 37.2164,
        "lon": 67.2783,
        "description": "Thermal anomaly in the border/steppe zone",
        "confidence": "Moderate confidence",
    },
    {
        "name": "Nukus",
        "lat": 42.4531,
        "lon": 59.6000,
        "description": "Open-area burning and dry-land heat signal",
        "confidence": "High confidence",
    },
    {
        "name": "Andijan",
        "lat": 40.7821,
        "lon": 72.3442,
        "description": "Crop residue burning in the Fergana Valley",
        "confidence": "High confidence",
    },
]


def validate_coordinate_pair(lat: float, lon: float, name: str) -> None:
    """Validate that coordinates are in the correct [lat, lon] order and inside Uzbekistan."""
    if not (-90 <= lat <= 90):
        raise ValueError(f"{name} latitude is out of range: {lat}")
    if not (-180 <= lon <= 180):
        raise ValueError(f"{name} longitude is out of range: {lon}")

    if not (UZBEKISTAN_BOUNDS["min_lat"] <= lat <= UZBEKISTAN_BOUNDS["max_lat"]):
        raise ValueError(f"{name} latitude is outside Uzbekistan bounds: {lat}")
    if not (UZBEKISTAN_BOUNDS["min_lon"] <= lon <= UZBEKISTAN_BOUNDS["max_lon"]):
        raise ValueError(f"{name} longitude is outside Uzbekistan bounds: {lon}")


# Validate the center and all hotspot coordinates before generating the map.
validate_coordinate_pair(UZBEKISTAN_CENTER[0], UZBEKISTAN_CENTER[1], "Uzbekistan center")
for hotspot in hotspots:
    validate_coordinate_pair(hotspot["lat"], hotspot["lon"], hotspot["name"])


def build_map() -> folium.Map:
    """Create and configure the Uzbekistan map with two tile providers."""
    # Use a clean map with no default background, then add our custom basemaps.
    m = folium.Map(
        location=UZBEKISTAN_CENTER,
        zoom_start=6,
        tiles=None,
        control_scale=True,
        prefer_canvas=True,
    )

    # Base layer 1: Esri World Imagery. The requested pattern is the ArcGIS imagery URL,
    # while the fallback endpoint is used to avoid blank tiles if the main source is blocked.
    folium.TileLayer(
        tiles=ESRI_SATELLITE_FALLBACK_URL,
        attr="Tiles © Esri",
        name="Satellite",
        overlay=False,
        control=True,
        max_zoom=19,
        error_tile_url=OSM_FALLBACK_URL,
    ).add_to(m)

    # Base layer 2: OSM Humanitarian tiles. This is a stable, accessible alternative to
    # the satellite view and works well for context around fire hotspots.
    folium.TileLayer(
        tiles=OSM_HOT_URL,
        attr="© OpenStreetMap contributors • HOT",
        name="Humanitarian Streets",
        overlay=False,
        control=True,
        max_zoom=19,
        subdomains="abc",
        error_tile_url=OSM_FALLBACK_URL,
    ).add_to(m)

    # Group all fire markers into a single cluster to keep the map readable.
    marker_cluster = MarkerCluster(name="Fire hotspots").add_to(m)

    # Add each hotspot as a red fire marker with tooltip and popup information.
    for hotspot in hotspots:
        popup_html = f"""
        <div style="font-family: Arial, sans-serif; width: 240px;">
            <h4 style="margin: 0 0 8px 0;">{hotspot['name']}</h4>
            <p style="margin: 0 0 6px 0;"><strong>Activity:</strong> {hotspot['description']}</p>
            <p style="margin: 0 0 6px 0;"><strong>Confidence:</strong> {hotspot['confidence']}</p>
            <p style="margin: 0;"><strong>Coordinates:</strong> {hotspot['lat']:.4f}, {hotspot['lon']:.4f}</p>
        </div>
        """

        folium.Marker(
            location=[hotspot["lat"], hotspot["lon"]],
            tooltip=f"{hotspot['name']} • {hotspot['confidence']}",
            popup=folium.Popup(popup_html, max_width=280),
            icon=folium.Icon(color="red", icon="fire", prefix="fa"),
        ).add_to(marker_cluster)

    # Allow the user to switch between satellite and street layers.
    folium.LayerControl(position="topright").add_to(m)

    return m


def main() -> None:
    """Generate the final standalone HTML map file."""
    try:
        map_object = build_map()
        output_path = os.path.abspath(OUTPUT_FILE)
        map_object.save(output_path)
        print(f"Map created successfully: {output_path}")
    except Exception as exc:  # Practical error handling for file generation problems.
        print(f"Failed to generate map: {exc}", file=sys.stderr)
        raise


if __name__ == "__main__":
    main()

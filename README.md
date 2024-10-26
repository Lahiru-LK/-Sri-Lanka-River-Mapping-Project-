
# 🌍 Sri Lanka River Mapping Project

https://github.com/user-attachments/assets/6e464aac-d12d-444d-b670-72a4e43963ed


This project visualizes the river networks of Sri Lanka using Python and GIS data. It reads shapefiles of river systems and boundary data, processes them using geospatial libraries, and displays them with optional elevation contour lines.

![image](https://github.com/user-attachments/assets/7a06c939-e237-4455-9e87-5fb5c2f9b75c)

## 📁 Project Structure

- **`hotosm_lka_waterways_lines_shp.*`**: Shapefile and related files for the river networks in Sri Lanka.
- **`lka_admbnda_adm0_slsd_20220816.*`**: Shapefile and related files containing the administrative boundary data for Sri Lanka.
- **`sri_lanka_map.py`**: Python script that loads, processes, and visualizes the river and boundary data.
- **`.venv` folder**: Virtual environment containing project-specific Python dependencies.
- **`README.md`**: Documentation file providing an overview and usage instructions.

## 📦 Libraries and Dependencies

This project uses the following Python libraries:
- **Geopandas**: For reading and handling geospatial data (`.shp` files).
- **Matplotlib**: For plotting the maps and visualizing the data.
- **Rasterio**: For working with raster data like DEM files (if used for elevation).

> **Note**: Ensure you have a virtual environment set up with these libraries installed.

## 🔧 Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/sri_lanka_river_mapping.git
   cd sri_lanka_river_mapping
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install geopandas matplotlib rasterio
   ```

## 🚀 How to Run the Project

1. Make sure all shapefiles and the Python script (`sri_lanka_map.py`) are in the same directory.
2. Run the Python script:
   ```bash
   python sri_lanka_map.py
   ```

## 🗺️ Code Overview

The script performs the following steps:

1. **Loading Shapefiles**:
   - It loads the boundary and river shapefiles using `geopandas`.
   - Sets the CRS (Coordinate Reference System) if not already set.

2. **Processing Data**:
   - Filters river data into main rivers and tributaries based on length.
   - Transforms coordinates to a common CRS for accurate overlay.

3. **Visualization**:
   - Plots the country boundary, main rivers, and tributaries.
   - Adds optional elevation contour lines (if DEM data is provided).

## 🔍 Sample Code

```python
import geopandas as gpd
import matplotlib.pyplot as plt

# Load shapefiles
sri_lanka_map = gpd.read_file("lka_admbnda_adm0_slsd_20220816.shp")
rivers_map = gpd.read_file("hotosm_lka_waterways_lines_shp.shp")

# Set CRS and transform if needed
sri_lanka_map.set_crs(epsg=4326, inplace=True)
rivers_map.set_crs(epsg=4326, inplace=True)
sri_lanka_map = sri_lanka_map.to_crs("EPSG:3857")
rivers_map = rivers_map.to_crs("EPSG:3857")

# Plotting
fig, ax = plt.subplots(figsize=(12, 12))
sri_lanka_map.plot(ax=ax, color="none", edgecolor="black")
rivers_map.plot(ax=ax, color="blue", linewidth=0.5)
plt.show()
```

## ⚠️ Troubleshooting

- **Coordinate Transformation Issues**: Ensure that all data files are correctly projected to the same CRS (EPSG:3857).
- **Library Import Errors**: Make sure all libraries are installed in your virtual environment.
- **No Data Showing**: Verify file paths and ensure all shapefiles are correctly named and placed in the same directory.

## 🌏 Acknowledgments

This project utilizes data from:
- **Humanitarian OpenStreetMap Team** for river network data.
- **[GADM](https://gadm.org/)** for administrative boundary data.

Feel free to reach out for further assistance or enhancements to this project!

---

This template provides clear steps for setup, usage, and troubleshooting, making it easy for anyone to get started with your project. Let me know if you need further customization!

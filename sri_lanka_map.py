import os
import geopandas as gpd
import matplotlib.pyplot as plt

# File paths - Update paths as necessary
country_shapefile = r"C:\Users\PC\Desktop\sl\lka_admbnda_adm0_slsd_20220816.shp"
rivers_shapefile = r"C:\Users\PC\Desktop\sl\hotosm_lka_waterways_lines_shp.shp"

# Check if files exist
if not os.path.isfile(country_shapefile):
    print("Country shapefile not found.")
    exit(1)
else:
    print("Country shapefile found.")

if not os.path.isfile(rivers_shapefile):
    print("Rivers shapefile not found.")
    exit(1)
else:
    print("Rivers shapefile found.")

try:
    # Load shapefiles
    print("Loading Sri Lanka boundary shapefile...")
    sri_lanka_map = gpd.read_file(country_shapefile)
    print("Sri Lanka boundary shapefile loaded successfully.")

    print("Loading rivers shapefile...")
    rivers_map = gpd.read_file(rivers_shapefile)
    print("Rivers shapefile loaded successfully.")

    # Set CRS if missing, and convert to EPSG:3857
    if sri_lanka_map.crs is None:
        print("Setting CRS for Sri Lanka boundary shapefile...")
        sri_lanka_map.set_crs(epsg=4326, inplace=True)
        print("CRS set for Sri Lanka boundary shapefile.")

    if rivers_map.crs is None:
        print("Setting CRS for rivers shapefile...")
        rivers_map.set_crs(epsg=4326, inplace=True)
        print("CRS set for rivers shapefile.")

    # Convert both to EPSG:3857 for consistency
    target_crs = "EPSG:3857"
    print("Transforming Sri Lanka boundary shapefile to target CRS...")
    sri_lanka_map = sri_lanka_map.to_crs(target_crs)
    print("Sri Lanka boundary shapefile transformed to target CRS.")

    print("Transforming rivers shapefile to target CRS...")
    rivers_map = rivers_map.to_crs(target_crs)
    print("Rivers shapefile transformed to target CRS.")

    # Separate main rivers and tributaries based on length
    print("Calculating river lengths...")
    rivers_map['length'] = rivers_map.geometry.length
    length_threshold = rivers_map['length'].quantile(0.75)
    main_rivers = rivers_map[rivers_map['length'] >= length_threshold]
    tributaries = rivers_map[rivers_map['length'] < length_threshold]
    print("Rivers classified into main rivers and tributaries.")

    # Plotting
    print("Generating the plot...")
    fig, ax = plt.subplots(figsize=(12, 12))

    # Overlay country boundary and rivers
    sri_lanka_map.plot(ax=ax, color="none", edgecolor="black")
    tributaries.plot(ax=ax, color="darkblue", linewidth=0.4, label="Tributaries")
    main_rivers.plot(ax=ax, color="blue", linewidth=0.5, label="Main Rivers")

    # Title and legend in English
    ax.set_title("Sri Lanka - Rivers Map", fontsize=16, fontweight='bold')
    ax.legend(loc='upper right')

    # Show the plot
    plt.show()
    print("Plot displayed successfully.")

except Exception as e:
    print(f"Error loading data: {e}")

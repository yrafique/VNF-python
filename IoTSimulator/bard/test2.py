import geopandas as gpd

city_map_path = "ITA_roads.shp"

try:
    city_map = gpd.read_file(city_map_path)
    print("Shapefile loaded successfully!")
    print(city_map.head())
except Exception as e:
    print(f"An error occurred: {e}")

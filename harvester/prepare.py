# building a buffer shape for filtering the weather data
import geopandas
from shapely.ops import cascaded_union

guetersloh = geopandas.read_file("./assets/Guetersloh.shp")
guetersloh = guetersloh.to_crs("epsg:3857")
guetersloh_boundary = geopandas.GeoDataFrame(geopandas.GeoSeries(cascaded_union(guetersloh['geometry'])))
guetersloh_boundary = guetersloh_boundary.rename(columns={0:'geometry'}).set_geometry('geometry')

guetersloh_buffer = guetersloh_boundary.buffer(2000)
guetersloh_buffer = guetersloh_buffer.simplify(1000)

guetersloh_buffer = geopandas.GeoDataFrame(guetersloh_buffer)
guetersloh_buffer = guetersloh_buffer.rename(columns={0:'geometry'}).set_geometry('geometry')
guetersloh_buffer.crs = "epsg:3857"
guetersloh_buffer.to_file("./assets/buffer.shp")
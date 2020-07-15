import pandas as pd
import geopandas
from shapely.geometry import Point, LineString, MultiPoint
from shapely.ops import cascaded_union, transform
import shapely.wkt
import matplotlib.pyplot as plt
import datetime
import sys
import os
import os.path
import dateutil
import numpy as np
import dateutil
import fiona.transform
from functools import partial
import pyproj
from collections import OrderedDict
import itertools

def wgs2ge(gdf, fname, force_delete_previous_geojson = True):
    '''take GeoDataFrame, ## convert the coordinate system to WGS84,
    write GeoJSON and convert it via ogr2ogr to KML'''
    
    for name, values in gdf.iteritems():
        if values.dtype == 'datetime64[ns]':
            gdf[name] = values.astype(str)
        else:
            continue

    # gdf.crs = {'init': 'epsg:32648'}
    # gdf_wgs = gdf.to_crs({'init': "epsg:4326"})
    gdf_wgs = gdf

    ## something wrong with schema
    ## check with geopandas.io.file.infer_schema()
    try:
        schema = geopandas.io.file.infer_schema(gdf) 
    except TypeError:
        schema = {
            'geometry': 'LineString',
            'properties': OrderedDict([('flight_id', 'str')])}
            
    try:
        os.remove('{:}.geojson'.format(fname))
    except OSError:
        pass

        
    gdf_wgs.to_file('{:}.geojson'.format(fname), driver='GeoJSON', schema=schema)
    cmd = 'ogr2ogr -f KML {:}.kml {:}.geojson'.format(fname, fname)
    print(cmd)
    os.system(cmd)

s3over = shapely.wkt.loads('''POLYGON((103.84033333333333 1.5038888888888888,
103.9886638888889 1.5197222222222222,
104.402 1.541111111111111,
104.72901944444445 2.6186555555555557,
104.2163888889 3.1297222222,
103.7441666667 3.1191666667,
103.76833333333333 2.905,
103.55666388888889 2.8722166666666666,
103.78716388888888 2.3675,
103.8078388888889 2.0022166666666665,
103.84033333333333 1.5038888888888888))''')

s7 = shapely.wkt.loads('''POLYGON((103.7441666667 3.1191666667,
103.73333055555555 4.833333333333333,
104.24500277777778 4.87305,
105.3796611111111 4.811383333333334,
106.21299722222223 4.28805,
105.795 4.07583333333,
104.33 3.6116666667,
104.2163888889 3.1297222222,
103.7441666667 3.1191666667))''')

s6 = shapely.wkt.loads('''POLYGON((106.21299722222223 4.28805,
106.57083055555556 3.90445,
106.9261638888889 3.561383333333333,
107.6855 2.92055,
105.5 2.5,
104.84117222222223 2.6597166666666667,
104.72901944444445 2.6186555555555557,
104.2163888889 3.1297222222,
104.33 3.6116666667,
105.795 4.07583333333,
106.21299722222223 4.28805))''')

s8 = shapely.wkt.loads('''POLYGON((106.57083055555556 3.90445,
106.21299722222223 4.28805,
105.3796611111111 4.811383333333334,
104.24500277777778 4.87305,
103.73333055555555 4.833333333333333,
102.66666388888889 6.75,
103.0 7.0,
108.0 7.0,
109.19966944444444 7.699716666666666,
106.57083055555556 3.90445))''')

s2old = shapely.wkt.loads('''POLYGON((103.03466666666667 1.3672222222222221,
103.2175 1.7547166666666667,
103.28799444444445 1.7041666666666666,
103.29716388888889 1.7991666666666666,
103.32883333333334 1.8861166666666667,
103.37549722222222 1.9525,
103.49282777777778 2.0366666666666666,
103.61133611111111 2.0627833333333334,
103.72466388888888 2.049716666666667,
103.8078388888889 2.0022166666666665,
103.84033333333333 1.5038888888888888,
103.47466388888888 1.4519444444444445,
103.35783333333333 1.2566666666666666,
103.03466666666667 1.3672222222222221))''')

s7old = shapely.wkt.loads('''POLYGON((102.16666388888889 1.65,
103.03466666666667 1.3672222222222221,
103.35783333333333 1.2566666666666666,
103.78799444444445 1.1197222222222223,
103.95666388888888 -0.2927777777777778,
103.60033333333334 -0.28888888888888886,
103.14699444444445 -0.1811111111111111,
102.875 -0.03388888888888889,
102.62000277777778 0.17027777777777778,
102.40466388888889 0.4363888888888889,
102.23466388888889 0.7708333333333334,
102.14966666666666 1.1105555555555555,
102.14383055555555 1.4222222222222223,
102.16666388888889 1.65))''')

s1over = shapely.wkt.loads('''POLYGON((104.402 1.541111111111111,
103.9886638888889 1.5197222222222222,
103.84033333333333 1.5038888888888888,
103.47466388888888 1.4519444444444445,
103.35783333333333 1.2566666666666666,
103.78799444444445 1.1197222222222223,
103.95666388888888 -0.2927777777777778,
104.76666944444445 0.0,
105.16666388888889 0.0,
106.0 -0.8333333333333334,
107.99333055555556 0.0,
109.0 0.0,
108.984725 0.15791944444444445,
104.56749722222222 1.0391666666666666,
104.402 1.541111111111111))''')

s4over = shapely.wkt.loads('''POLYGON((104.402 1.541111111111111,
104.72901944444445 2.6186555555555557,
104.84117222222223 2.6597166666666667,
105.5 2.5,
107.6855 2.92055,
109.62366388888888 3.30055,
110.09216388888889 3.4758333333333336,
108.5 2.25,
108.5 1.0,
108.90000277777777 1.0,
108.984725 0.15791944444444445,
104.56749722222222 1.0391666666666666,
104.402 1.541111111111111))''')

s5 = shapely.wkt.loads('''POLYGON((106.57083055555556 3.90445,
109.19966944444444 7.699716666666666,
114.0 10.5,
116.5 8.416666666666666,
110.09216388888889 3.4758333333333336,
109.62366388888888 3.30055,
107.6855 2.92055,
106.9261638888889 3.561383333333333,
106.57083055555556 3.90445))''')

s2over = cascaded_union([s2old, s7old])

project = partial(
    pyproj.transform,
    pyproj.Proj(init='epsg:32648'), # source coordinate system
    pyproj.Proj(init='epsg:4326')) # destination coordinate system
wsss_fiona = fiona.transform.transform(
    'epsg:4326', 'epsg:32648',
    [103.989444], [1.359167])
wsss = Point(wsss_fiona[0][0], wsss_fiona[1][0])
nm40_utm = wsss.buffer(40 * 1852)
nm40 = transform(project, nm40_utm)  # apply projection

s1 = s1over - nm40
s2 = s2over - nm40
s3 = s3over - nm40
s4 = s4over - nm40

speedcontrol = cascaded_union([s6, s7, s8])
north = cascaded_union([s3, s6, s7, s8])
without5 = cascaded_union([s1over, s2over, s3over, s4over, s6, s7, s8, nm40, s1, s2, s3, s4])
allsectors = cascaded_union([without5, s5, s4over, s6, s8])



sectors = geopandas.GeoSeries([
    s1, s2, s3, s4, s5, s6, s7, s8,
    s1over, s2over, s3over, s4over,
    north, speedcontrol, without5, allsectors, nm40],
    index=[
        's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8',
        's1over', 's2over', 's3over', 's4over',
        'northac', 'speedcontrol', 'operational', 'allsectors', 'tma'])

wgs2ge(geopandas.GeoDataFrame({'geometry': sectors}), 'test') 
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("http://opendata-geohive.hub.arcgis.com/datasets/07b8a45b715d4e4eb4ad39fc44c4bd06_0.csv?outSR={%22latestWkid%22:3857,%22wkid%22:102100}")

lons = df['x'].values
lats = df['y'].values
names = df['CountyName']
cases = df['CovidCases']

fig, ax = plt.subplots()
map = Basemap(projection='merc', lat_0 = 53, lon_0 = -4,
    resolution = 'i', area_thresh = 0.05,
    llcrnrlon=-10.59, llcrnrlat=51.27,
    urcrnrlon=-5.33, urcrnrlat=55.45)
map.drawcoastlines(linewidth = 0.2, zorder = 0)
map.drawmapboundary() 
map.fillcontinents()
map.drawcountries()

x,y = map(lons, lats)

for x, y, c in zip(x, y, cases):
    # markersize is scale down by /145
    map.plot(x, y, 'ro', markersize=c/145, alpha=0.4)

plt.show()

print(cases)








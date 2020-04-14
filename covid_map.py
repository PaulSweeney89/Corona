from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Covid-19 dataset csv file from data.gov.ie
# CovidCountyStatisticsHPSCIreland
# https://data.gov.ie/dataset/covidcountystatisticshpscireland/resource/db9ee961-0ea9-4f74-b137-a625ffb0efe9

df = pd.read_csv("http://opendata-geohive.hub.arcgis.com/datasets/07b8a45b715d4e4eb4ad39fc44c4bd06_0.csv?outSR={%22latestWkid%22:3857,%22wkid%22:102100}")

lons = df['x'].values
lats = df['y'].values
names = df['CountyName']
cases = df['CovidCases']

fig, ax = plt.subplots()
map = Basemap(projection='merc',
    resolution = 'i', area_thresh = 0.05,
    llcrnrlon=-10.59, llcrnrlat=51.27,
    urcrnrlon=-5.33, urcrnrlat=55.45)
map.drawcoastlines(linewidth = 0.2, zorder = 0)
map.drawmapboundary() 
map.fillcontinents()
map.drawcountries()

xpt,ypt = map(lons, lats)

total_cases = sum(cases)
#tc = df.loc[-1, 'TotalConfirmedCovidCases']
fig.suptitle("Number of Covid 19 Cases in Ireland by County\nTotal Number of Cases = %i" %total_cases)

for x, y, c in zip(xpt,ypt, cases):
    # markersize is scale down by /125
    map.plot(x, y, 'ro', markersize=(c/125), alpha=0.4)
    plt.text(x, y, c, fontsize=7, verticalalignment='bottom', horizontalalignment='center', fontweight='bold')

for w, z, n in zip(xpt,ypt, names):
    plt.text(w, z, n, fontsize=6, verticalalignment='top', horizontalalignment='center')

plt.show()







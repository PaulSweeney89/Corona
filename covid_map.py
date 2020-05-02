from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date

# Covid-19 dataset csv file from data.gov.ie
# CovidCountyStatisticsHPSCIreland
# https://data.gov.ie/dataset/covid19countystatisticshpscirelandopendata/resource/cd796ddd-38f5-47f7-b8b3-dd2b0621cce6

df = pd.read_csv("http://opendata-geohive.hub.arcgis.com/datasets/4779c505c43c40da9101ce53f34bb923_0.csv?outSR={%22latestWkid%22:3857,%22wkid%22:102100}")

today = date.today()

lons = df['x'].values
lats = df['y'].values
names = df['CountyName'].iloc[-26:]
cases = df['ConfirmedCovidCases'].iloc[-26:]

print(cases)
print(names)

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
fig.suptitle("Number of Covid 19 Cases in Ireland by County\nTotal Number of Cases = "+str(total_cases)+"\n"+str(today))

for x, y, c in zip(xpt,ypt, cases):
    # markersize is scale down by /125
    map.plot(x, y, 'ro', markersize=(c/125), alpha=0.4)
    plt.text(x, y, c, fontsize=7, verticalalignment='bottom', horizontalalignment='center', fontweight='bold')

for w, z, n in zip(xpt,ypt, names):
    plt.text(w, z, n, fontsize=6, verticalalignment='top', horizontalalignment='center')

plt.show()

# Save dataframe as csv file 

filename = str(today) + 'Covid 19 Counties.csv'
df.to_csv(filename)

# extracting county co-ordinates
#df_counties = df[['CountyName','Lat', 'Long']] 
#df_counties.to_csv('County Coordinates.csv')





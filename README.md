# Corona #
Covid 19 in Ireland

*simple python scripts for plotting & reviewing covid 19 data in Republic of Ireland.*

- Dataset 1 from [data.gov.ie - CovidStatisticsProfileHPSCIrelandOpenData](https://data.gov.ie/dataset/covidstatisticsprofilehpscirelandopendata/resource/b8143e99-4929-41bc-ac1c-5520c0666b20)
Up to date Covid-19 Daily Statistics as well as the Profile of Covid-19 Daily Statistics for Ireland, as reported by the Health Surveillance Protection
- Dataset 2 from [data.gov.ie - CovidCountyStatisticsHPSCIreland](https://data.gov.ie/dataset/covidcountystatisticshpscireland/resource/db9ee961-0ea9-4f74-b137-a625ffb0efe9)
Covid-19 Daily Statistics for Ireland by County as reported by the Health Surveillance Protection Centre
- *covid.py* used for plotting graphs for dataset 1.
- *covid_map.py* used for plotting map for dataset 2.

**Python Libraries:**
- Pandas
- Matplotlib
- Datetime
- Matplotlib Basemap Toolkit

**Sample Outputs:**

- Bar plot showing Total Confirmed Covid 19 Cases in Ireland.

![fig1](https://github.com/PaulSweeney89/Corona/blob/master/Outputs/Figure_1.png)

- Bar plot showing Total Confirmed Deaths in Ireland.

![fig2](https://github.com/PaulSweeney89/Corona/blob/master/Outputs/Figure_2.png)

- Plot showing Daily Confirmed New Cases in Ireland.

![fig3](https://github.com/PaulSweeney89/Corona/blob/master/Outputs/Figure_3.png)

- Basemap plot showing Covid 19 cases per County.

![fig5](https://github.com/PaulSweeney89/Corona/blob/master/Outputs/Figure_5.png)

**Note:** There appears to be a discrepancy between the number of confirmed cases between datasets 1 & 2, dataset 2 is reporting lower confirmed cases.

## Dash ##

*Simple web applications built using python and dash for reviewing the Covid 19 datasets for Ireland.*

Application was developed based on [Python Programming Tutorial](https://pythonprogramming.net/data-visualization-application-dash-python-tutorial-introduction/)

- *app.py* script for plotting for dataset 1.

**Python Libraries:**
- Dash
- Pandas 

References:

[Creating Attractive and Informative Map Visualisations in Python with Basemap](https://www.datadependence.com/2016/06/creating-map-visualisations-in-python/)




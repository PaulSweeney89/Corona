import pandas as pd 
import matplotlib.pyplot as plt
import datetime

# Covid-19 dataset csv file from data.gov.ie
# CovidStatisticsProfileHPSCIrelandOpenData
# https://data.gov.ie/dataset/covidstatisticsprofilehpscirelandopendata/resource/b8143e99-4929-41bc-ac1c-5520c0666b20

df = pd.read_csv("http://opendata-geohive.hub.arcgis.com/datasets/d8eb52d56273413b84b0187a4e9117be_0.csv?outSR={%22latestWkid%22:3857,%22wkid%22:102100}")

df['Date'] = pd.to_datetime(df['Date'])
df['Datestr'] = df['Date'].dt.strftime('%d/%m')

plt.bar(x=df["Datestr"], height=df["TotalConfirmedCovidCases"], color='b')
plt.bar(x=df["Datestr"], height=df["ConfirmedCovidCases"], color='c')
plt.xticks(df["Datestr"], rotation = '90')
plt.grid(which='major', axis='y', linestyle='dotted', alpha=0.8)
plt.title("Ireland Covid 19 Total Confirmed Cases")
for i in range(len(df)):
    t = df.loc[i, "TotalConfirmedCovidCases"]
    c = df.loc[i, "ConfirmedCovidCases"]
    plt.text(df.loc[i, "Datestr"], df.loc[i, "TotalConfirmedCovidCases"] + 0.25, t, size=8, fontweight='bold')
    plt.text(df.loc[i, "Datestr"], df.loc[i, "ConfirmedCovidCases"] + 0.25, c, size=8, fontweight='bold') 
plt.show()

plt.bar(x=df["Datestr"], height=df["TotalCovidDeaths"], color='r')
plt.xticks(df["Datestr"], rotation = '90')
plt.grid(which='major', axis='y', linestyle='dotted', alpha=0.8)
plt.title("Ireland Covid 19 Total Confirmed Deaths")
for i in range(len(df)):
    t = df.loc[i, "TotalCovidDeaths"]
    plt.text(df.loc[i, "Datestr"], df.loc[i, "TotalCovidDeaths"] + 0.25, t, size=8, fontweight='bold')
plt.show()

plt.plot(df["Datestr"], df["ConfirmedCovidCases"], marker='o', markersize=3, color="blue")
plt.xticks(df["Datestr"], rotation = '90')
plt.grid(which='major', axis='y', linestyle='dotted', alpha=0.8)
plt.title("Ireland Covid 19 Daily Confirmed New Cases")
for i in range(len(df)):
    t = df.loc[i, "ConfirmedCovidCases"]
    plt.text(df.loc[i, "Datestr"], df.loc[i, "ConfirmedCovidCases"] + 0.25, t, size=8)
plt.show()





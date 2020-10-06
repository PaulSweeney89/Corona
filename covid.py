import pandas as pd 
import matplotlib.pyplot as plt
#import seaborn as sns
import datetime
from datetime import date

# Covid-19 dataset csv file from data.gov.ie
# CovidStatisticsProfileHPSCIrelandOpenData
# https://data.gov.ie/dataset/covidstatisticsprofilehpscirelandopendata

df = pd.read_csv("http://opendata-geohive.hub.arcgis.com/datasets/d8eb52d56273413b84b0187a4e9117be_0.csv?outSR={%22latestWkid%22:3857,%22wkid%22:102100}")

today = date.today()

df['Date'] = pd.to_datetime(df['Date']) #unit='ms')					# csv file date format was changed to milliseconds
df['Datestr'] = df['Date'].dt.strftime('%d/%m')

plt.bar(x=df["Date"], height=df["TotalConfirmedCovidCases"], color='b')
plt.bar(x=df["Date"], height=df["ConfirmedCovidCases"], color='c')
#plt.xticks(df["Datestr"], rotation = '90')
plt.grid(which='major', axis='y', linestyle='dotted', alpha=0.8)
plt.title("Ireland Covid 19 Total Confirmed Cases"+"\n"+str(today))
#for i in range(len(df)):
    #t = df.loc[i, "TotalConfirmedCovidCases"]
    #c = df.loc[i, "ConfirmedCovidCases"]
    #plt.text(df.loc[i, "Datestr"], df.loc[i, "TotalConfirmedCovidCases"] + 0.25, t, size=8, fontweight='bold')
    #plt.text(df.loc[i, "Datestr"], df.loc[i, "ConfirmedCovidCases"] + 0.25, c, size=8, fontweight='bold') 
plt.show()

plt.bar(x=df["Date"], height=df["TotalCovidDeaths"], color='r')
#plt.xticks(df["Datestr"], rotation = '90')
plt.grid(which='major', axis='y', linestyle='dotted', alpha=0.8)
plt.title("Ireland Covid 19 Total Confirmed Deaths"+"\n"+str(today))
#for i in range(len(df)):
    #t = df.loc[i, "TotalCovidDeaths"]
    #plt.text(df.loc[i, "Datestr"], df.loc[i, "TotalCovidDeaths"] + 0.25, t, size=8, fontweight='bold')
plt.show()

plt.plot(df["Date"], df["ConfirmedCovidCases"], marker='o', markersize=1, color="blue")
#plt.xticks(df["Datestr"], rotation = '90')
plt.grid(which='major', axis='y', linestyle='dotted', alpha=0.8)
plt.title("Ireland Covid 19 Daily Confirmed New Cases"+"\n"+str(today))
#for i in range(len(df)):
    #t = df.loc[i, "ConfirmedCovidCases"]
    #plt.text(df.loc[i, "Datestr"], df.loc[i, "ConfirmedCovidCases"] + 0.25, t, size=8)
plt.show()

plt.plot(df["Date"], df["TotalConfirmedCovidCases"], marker='o', markersize=1, color="red")
plt.plot(df["Date"], df["ConfirmedCovidRecovered"], marker='o', markersize=1, color="green")
#plt.xticks(df["Datestr"], rotation = '90')
plt.grid(which='major', axis='y', linestyle='dotted', alpha=0.8)
plt.title("Ireland Covid 19 Confirmed Cases & Confirmed Recovered"+"\n"+str(today))
#for i in range(len(df)):
    #t = df.loc[i, "TotalConfirmedCovidCases"]
    #plt.text(df.loc[i, "Datestr"], df.loc[i, "TotalConfirmedCovidCases"] + 0.25, t, size=8)
#for j in range(len(df)):
    #t = df.loc[j, "ConfirmedCovidRecovered"]
    #plt.text(df.loc[j, "Datestr"], df.loc[j, "ConfirmedCovidRecovered"] + 0.25, t, size=8, rotation = '45')
plt.show()

df["x"] = df["TotalConfirmedCovidCases"] - df["ConfirmedCovidRecovered"]
plt.bar(x=df["Date"], height=df["x"], color='b')
#plt.xticks(df["Datestr"], rotation = '90')
plt.grid(which='major', axis='y', linestyle='dotted', alpha=0.8)
plt.title("Ireland Covid 19 Total - Recovered Cases"+"\n"+str(today))
#for i in range(len(df)):
    #t = df.loc[i, "x"]
    #plt.text(df.loc[i, "Datestr"], df.loc[i, "x"] + 0.25, t, size=8)
plt.show()

plt.plot(df["TotalConfirmedCovidCases"],df["ConfirmedCovidCases"], marker='o', markersize=1, color="green")
plt.xlabel("Total Confirmed Covid Cases")
plt.ylabel("Daily New Confirmed Covid Cases")
plt.title("Ireland Covid 19"+"\n"+str(today))
plt.show()

# seaborn plot
#plt.figure(2)
#plt.title("Total Confirmed Cases vs New Daily Confirmed Cases")
#ax1 = sns.scatterplot(x=df["TotalConfirmedCovidCases"], y=df["ConfirmedCovidCases"], data=df)
#ax1 = sns.regplot(x=df["TotalConfirmedCovidCases"], y=df["ConfirmedCovidCases"], data=df, scatter=False, color='red')
#ax1.set(xlabel="", ylabel="")
#plt.show()

filename = str(today) + 'Covid 19 Ireland.csv'
df.to_csv(filename)


 




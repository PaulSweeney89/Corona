# Covid 19 Dash
# Developed using Python Programming Tutorial
# https://pythonprogramming.net/data-visualization-application-dash-python-tutorial-introduction/

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash()

# Covid-19 dataset csv file from data.gov.ie
# CovidStatisticsProfileHPSCIrelandOpenData
# https://data.gov.ie/dataset/covidstatisticsprofilehpscirelandopendata

df = pd.read_csv('http://opendata-geohive.hub.arcgis.com/datasets/d8eb52d56273413b84b0187a4e9117be_0.csv?outSR={%22latestWkid%22:3857,%22wkid%22:102100}')

app.layout = html.Div(children=[
    html.H1(children='Covid 19'),
        dcc.Graph(
        id='Total Confirmed Cases',
        figure={
            'data': [
                {'x': df['Date'], 'y': df['TotalConfirmedCovidCases'], 'type': 'bar', 'name': 'Total Confirmed Cases'},
		{'x': df['Date'], 'y': df['ConfirmedCovidCases'], 'type': 'bar', 'name': 'Confirmed Cases'}
            ],
            'layout': {
                'title': 'Total Confirmed Cases'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server()





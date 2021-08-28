from dash.dependencies import Input, Output, State

from app import app

import pandas as pd
import numpy as np
import json

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table


@app.callback(
    Output('maintable','data'),
    Output('nodatalist','children'),
    Output('paplist','children'),
    Output('npaplist','children'),
    Output('bothlist','children'),
    Input('region','value')
)
def update_tables(region):
    df = pd.read_csv('maintable.csv')
    haspap = pd.read_csv('haspap.csv')
    nodatalist=[]
    paplist=[]
    npaplist=[]
    bothlist=[]


    if region == 'all':
        j = df
        nodatalist = haspap[haspap['provider type']==0]['Country'].to_list()
        paplist = haspap[haspap['provider type']==1]['Country'].to_list()
        npaplist = haspap[haspap['provider type']==2]['Country'].to_list()
        bothlist = haspap[haspap['provider type']==3]['Country'].to_list()
    elif region == 'Region of the Americas':
        j = df[df['Region'] == region]
        nodatalist = haspap[(haspap['Region']==region) & (haspap['provider type']==0)]['Country'].to_list()
        paplist = haspap[(haspap['Region']==region) & (haspap['provider type']==1)]['Country'].to_list()
        npaplist = haspap[(haspap['Region']==region) & (haspap['provider type']==2)]['Country'].to_list()
        bothlist = haspap[(haspap['Region']==region) & (haspap['provider type']==3)]['Country'].to_list()
    elif region == 'African Region':
        j = df[df['Region'] == region]
        nodatalist = haspap[(haspap['Region']==region) & (haspap['provider type']==0)]['Country'].to_list()
        paplist = haspap[(haspap['Region']==region) & (haspap['provider type']==1)]['Country'].to_list()
        npaplist = haspap[(haspap['Region']==region) & (haspap['provider type']==2)]['Country'].to_list()
        bothlist = haspap[(haspap['Region']==region) & (haspap['provider type']==3)]['Country'].to_list()
    elif region == 'Eastern Mediterranean Region':
        j = df[df['Region'] == region]
        nodatalist = haspap[(haspap['Region']==region) & (haspap['provider type']==0)]['Country'].to_list()
        paplist = haspap[(haspap['Region']==region) & (haspap['provider type']==1)]['Country'].to_list()
        npaplist = haspap[(haspap['Region']==region) & (haspap['provider type']==2)]['Country'].to_list()
        bothlist = haspap[(haspap['Region']==region) & (haspap['provider type']==3)]['Country'].to_list()
    elif region == 'European Region':
        j = df[df['Region'] == region]
        nodatalist = haspap[(haspap['Region']==region) & (haspap['provider type']==0)]['Country'].to_list()
        paplist = haspap[(haspap['Region']==region) & (haspap['provider type']==1)]['Country'].to_list()
        npaplist = haspap[(haspap['Region']==region) & (haspap['provider type']==2)]['Country'].to_list()
        bothlist = haspap[(haspap['Region']==region) & (haspap['provider type']==3)]['Country'].to_list()
    elif region == 'South-East Asia Region':
        j = df[df['Region'] == region]
        nodatalist = haspap[(haspap['Region']==region) & (haspap['provider type']==0)]['Country'].to_list()
        paplist = haspap[(haspap['Region']==region) & (haspap['provider type']==1)]['Country'].to_list()
        npaplist = haspap[(haspap['Region']==region) & (haspap['provider type']==2)]['Country'].to_list()
        bothlist = haspap[(haspap['Region']==region) & (haspap['provider type']==3)]['Country'].to_list()
    elif region == 'Western Pacific Region':
        j = df[df['Region'] == region]
        nodatalist = haspap[(haspap['Region']==region) & (haspap['provider type']==0)]['Country'].to_list()
        paplist = haspap[(haspap['Region']==region) & (haspap['provider type']==1)]['Country'].to_list()
        npaplist = haspap[(haspap['Region']==region) & (haspap['provider type']==2)]['Country'].to_list()
        bothlist = haspap[(haspap['Region']==region) & (haspap['provider type']==3)]['Country'].to_list()
    else:
        j = df

    return j.to_dict('records'), html.Div([
        html.Table(
            [html.Tr(
                html.Th('No Data'))]+
            [html.Tr(html.Td(x)) for x in nodatalist]
        )
    ]),html.Div([
        html.Table(
            [html.Tr(
                html.Th('PAP only'))]+
            [html.Tr(html.Td(x)) for x in paplist]
        )
    ]),html.Div([
        html.Table(
            [html.Tr(
                html.Th('NPAP only'))]+
            [html.Tr(html.Td(x)) for x in npaplist]
        )
    ]),html.Div([
        html.Table(
            [html.Tr(
                html.Th('Both providers'))]+
            [html.Tr(html.Td(x)) for x in bothlist]
        )
    ])

#Output('nodatastore','children'),
#Output('npapstore','children'),
#Output('bothstore','children'),
#Output('papstore','children')],
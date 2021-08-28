import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_bootstrap_components as dbc
import datetime
from datetime import date, timedelta
import pandas as pd
import numpy as np
import plotly.express as px


df = pd.read_csv('maintable.csv')
df = df.sort_values('Country', ascending=True)
haspap = pd.read_csv('haspap.csv')

#### making completion figure
def recode(x):
    if x == 0:
        return 'None'
    elif x == 1:
        return 'PAP only'
    elif x == 2:
        return 'NPAP only'
    elif x == 3:
        return 'both'

haspap['provider2'] = haspap['provider type'].apply(recode)


cxtab_normal = pd.crosstab(haspap['Region'], haspap['provider2'], normalize='index')
cxtab_count = pd.crosstab(haspap['Region'], haspap['provider2'])
t4_normal = cxtab_normal.reset_index().melt(id_vars='Region',value_name='percent')
t4_count = cxtab_count.reset_index().melt(id_vars='Region',value_name='count')
t4_normal['count'] = t4_count['count']
completion = px.bar(t4_normal, y='Region', x='percent', color='provider2',
             orientation='h',
            color_discrete_map={"None": px.colors.qualitative.Dark2[1], "NPAP only": "cornflowerblue", "PAP only": px.colors.qualitative.Pastel[4], "both":px.colors.qualitative.Pastel[9]},
             #color_discrete_sequence=px.colors.qualitative.Pastel2,
             hover_data=['count'],
            labels={"provider2":"Provider type"},
            category_orders={"provider2":['PAP only','both','NPAP only','None']},
            title='Completion by Region',
             text='count'
            )


#############


body = dbc.Container(fluid=True, style={'padding': 40}, children=[
    html.H1('Global Anesthesia Workforce Survey'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H4('Region', className='card-title'),
                dbc.FormGroup([
                    dcc.Dropdown(id='region', options=[
                        {"label": 'All regions','value':'all'},
                        {"label": 'Americas','value':'Region of the Americas'},
                        {"label": 'Africa','value':'African Region'},
                        {"label": 'Eastern Mediterranean','value':'Eastern Mediterranean Region'},
                        {"label": 'Europe','value':'European Region'},
                        {"label": 'SE Asia','value':'South-East Asia Region'},
                        {"label": 'Western Pacific','value':'Western Pacific Region'}
                        ], value='all', className='card-body')
                ]),
            ], className="w-25", color='light')
        ]),
    ]),

    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='maintable',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                page_size=10,
                sort_action='native',
                style_table={'padding': 40}
            )
        ])
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=completion)
        ])
    ]),

    dbc.Row([
        dbc.Col([html.Div(id='nodatalist')]),
        dbc.Col([html.Div(id='paplist')]),
        dbc.Col([html.Div(id='npaplist')]),
        dbc.Col([html.Div(id='bothlist')])
    ]),
])
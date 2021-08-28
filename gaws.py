import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
import numpy as np
import requests
from io import StringIO


from app import app
server = app.server

import layout_main
import callbacks_main

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavLink("Current Table", href="#")
    ],
    color="light",
    dark=False,
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(navbar),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
         return layout_main.body
    elif pathname == '/':
         return layout_main.body
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
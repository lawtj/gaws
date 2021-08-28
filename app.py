import dash
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE])
app.title = 'Global Anesthesia Workforce Survey'

#server = app.server(debug=True)
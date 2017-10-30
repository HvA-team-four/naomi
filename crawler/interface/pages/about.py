from dash.dependencies import  Input, Output
import dash_html_components as html
import dash_core_components as dcc

from interface import app

layout = html.Div([
    html.H3('About'),
    html.P('HIVE is created as part of the Security project at the Hogeschool van Amsterdam (university of applied sciences) and is therefore not means for commercial use. View the software-license to get more information about this application and redistribution.', style={'maxWidth' : 500})
])
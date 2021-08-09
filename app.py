import pandas as pd
import statsmodels.api as sm

import dash
import dash_core_components as dcc
import dash_html_components as html

import pickle
from utils.feature_calculation import *

app = dash.Dash(__name__)

forecasted_units = 0

app.layout = html.Div(children = [
    html.Div(# header
        children = [
            html.H1(
                children = 'Rain Category - Order Volume Forecaster',
                id = 'title'
            )
        ]
    ),
    html.Div(# input year and month
        children = [
            html.H3(
                children = 'Input order year and month (ex. 2010-10)',
                className = 'subtitle'
            ),
            dcc.Input(id='year', type='number', placeholder = '', min= 2005, max = 2015),
            html.Span(children = '-', style = {'fontWeight': 'bold', 'fontSize': 20}),
            dcc.Input(id='month', type='number', placeholder = '', max = 12, min = 1)
        ]
    ),
    html.Div(# select umbrella, poncho, or hat
        children = [
            html.H3(
                children = 'Select product type:',
                className = 'subtitle'
            ),
            dcc.RadioItems(
                id='product-type',
                options = [
                    {'label': 'Umbrella', 'value': 'umbrella'},
                    {'label': 'Poncho', 'value': 'poncho'},
                    {'label': 'Hat', 'value': 'hat'}
                ],
                value='umbrella'
            )
        ]
    ),
    html.Div(# price point
        children = [
            html.H3(
                children = 'Enter price point:',
                className = 'subtitle'
            ),
            html.Span(children = '$', style = {'fontSize': 20}),
            dcc.Input(id='price', type='number', placeholder = '', min = 0.01)
        ]
    ),
    html.Div(# styling: kids, dots
        children = [
            html.H3(
                children = 'Product characteristics:',
                className = 'subtitle'
            ),
            dcc.Checklist(
                id = 'product-characteristics',
                options =[
                    {'label': 'Children', 'value': 'child'},
                    {'label': 'Dots', 'value': 'dots'}
                ]
            )
        ]
    ),
    html.Div(# umbrella styling: folding, ruffled
        children = [
            html.H3(
                children = 'Umbrella styling (if applicable):',
                className = 'subtitle'
            ),
            dcc.Checklist(
                id = 'umbrella-characteristics',
                options =[
                    {'label': 'Folding', 'value': 'folding'},
                    {'label': 'Ruffled', 'value': 'ruffle'}
                ]
            )
        ]
    ),
    html.Div(# calculate button + result
        children =[
            html.Button(
                children = 'Estimate Order Quanity'
            ),
            html.Br(),
            html.Textarea(
                children = f'{forecasted_units}',
                style = {'marginTop': 14, 'fontSize': 20, 'textAlign': 'right', 'height': '24px', 'width': '10%'}
            ),
            html.Span(
                children = 'units',
                style = {'fontSize': 20, 'marginTop': 14}
            )
        ]
    )
])

if __name__ == '__main__':
    app.run_server(port = 4000, debug = True, dev_tools_hot_reload = True)
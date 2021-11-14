# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd


## Resources
df_agri = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

df_gdp = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}


"""
HTML
"""
## HTML H1
header = html.H1(children='Hello Dash', style={'textAlign': 'center','color': colors['text']})
## HTML Div
div_description = html.Div(children='''Dash: A web application framework for Python.''', style={'textAlign': 'center','color': colors['text']})
## HTML Table
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


""" 
Dash Core Components
"""
## Dash Graph
dash_graph_data = dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 4], 'y': [4, 1, 2, 6], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3, 4], 'y': [2, 4, 5, 9], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
dash_graph_gdp = dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                dict(
                    x=df_gdp[df_gdp['continent'] == i]['gdp per capita'],
                    y=df_gdp[df_gdp['continent'] == i]['life expectancy'],
                    text=df_gdp[df_gdp['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df_gdp.continent.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
## Markdown
md = dcc.Markdown(children=markdown_text)
## Dropdown
dd = dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    )
dd_multi = dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        multi=True
    )
## RadioItems
ri = dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    )
## Checklist
cl = dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']
    )
## Text Input
ti = dcc.Input(value='MTL', type='text')
## Slider
sl = dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=5,
    )


"""
Dash App
"""
## App
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

## Layout
app.layout = html.Div(style={'backgroundColor': colors['background'], 'columnCount': 1}, children=[
    
    header,

    div_description,

    dash_graph_data,

    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df_agri),
    html.H4(children='GDP'),
    dash_graph_gdp,

    html.Label('Markdown'),
    md,
    
    html.Label('Dropdown'),
    dd,
    html.Label('Multi-Select Dropdown'),
    dd_multi,

    html.Label('Radio Items'),
    ri,

    html.Label('Checklist'),
    cl,

    html.Label('Text Input'),
    ti,

    html.Label('Slider'),
    sl,

])

if __name__ == '__main__':
    app.run_server(debug=True)
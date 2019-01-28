import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

data = pd.read_csv('mtcars.tsv', sep='\t', skiprows=4)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = {
    'background': '#ffffff',
    'text': '#000000'
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


models = []
stats = ['mpg', 'cyl', 'disp', 'hp', 'drat']

for i in range(0, 10):
    models.append(data['model'][i])


app.layout = html.Div([
    html.H1(
        children='Motor Trend Car Road Tests',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(
        children='Comparing Car Models on MPG, CYL, DISP, HP, and DRAT',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),


    html.Div([
        dcc.Dropdown(
            id="variable-column",
            options=[{'label': i, 'value': i} for i in stats],
            value='mpg'
        ),
        
        dcc.Graph(id='model-graphic')
    ])
])


@app.callback(
    dash.dependencies.Output('model-graphic', 'figure'),
    [dash.dependencies.Input('variable-column', 'value')]
     
)
def update_model(variable_column):
    
    return {
        'data': [go.Scatter(
            x= models,
            y=data[variable_column],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],

        'layout': go.Layout(
            xaxis={
                'title': 'Car Models'
                
            },
            yaxis={
                'title': variable_column
                
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )


    }


if __name__ == '__main__':
    app.run_server(debug=True)

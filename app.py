import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

data = pd.read_csv('mtcars.tsv', sep='\t', skiprows=4)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


models = []
stats = ['mpg', 'cyl', 'disp', 'hp', 'drat']

for i in range(0, 10):
    models.append(data['model'][i])


app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id="model-column",
            options=[{'label': i, 'value': i} for i in stats],
            value='mpg'
        ),
        
        dcc.Graph(id='model-graphic')
    ])
])


@app.callback(
    dash.dependencies.Output('model-graphic', 'figure'),
    [dash.dependencies.Input('model-column', 'value')]
     
)
def update_model(model_column):
    
    return {
        'data': [go.Scatter(
            x= models,
            y= data[model_column],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],

        'layout': go.Layout(
            xaxis={
                'title': model_column
                
            },
            yaxis={
                'title': 'stat'
                
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )


    }


if __name__ == '__main__':
    app.run_server(debug=True)

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

data = pd.read_csv('mtcars.tsv', sep='\t', skiprows=4)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


models = []
mpgvalues =[]
cylvalues = []
dispvalues = []
stats = ['mpg', 'cyl', 'disp' ]

for i in range(0, 10):
    models.append(data['model'][i])

for i in range(0, 10):
    mpgvalues.append(data.iloc[i][1])
  

for i in range(0, 10):
    cylvalues.append(data.iloc[i][2])
    

for i in range(0, 10):
    dispvalues.append(data.iloc[i][3])

mpg_dict = dict(zip(models, mpgvalues))
cyl_dict = dict(zip(models, cylvalues))
disp_dict = dict(zip(models, dispvalues))



app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id="model-column",
            options=[{'label': i, 'value': i} for i in models],
            value='Mazda RX4'
        ),
        dcc.Dropdown(
            id='stat-column',
            options=[
                {'label': 'MPG', 'value': stats[0]},
                {'label': 'CYL', 'value': stats[1]},
                {'label': 'DISP', 'value': stats[2]}
            ],
            value='MPG'
        ),
        dcc.Graph(id='model-graphic')
    ])
])


@app.callback(
    dash.dependencies.Output('model-graphic', 'figure'),
    [dash.dependencies.Input('stat-column', 'value'),
     dash.dependencies.Input('model-column', 'value')]
)
def update_model(model_column):

    return {
        'data': [go.Scatter(
            
        )]


    }


if __name__ == '__main__':
    app.run_server(debug=True)

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

data = pd.read_csv('mtcars.tsv', sep='\t', skiprows=4)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

models =[]

for i in data.index:
    models.append(data['model'][i])


app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id="model-column",
            options=[{'label': i, 'value': i} for i in models],
            value='Mazda RX4'

        )




    ])



])


if __name__ == '__main__':
    app.run_server(debug=True)

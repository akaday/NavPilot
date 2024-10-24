import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)

# Create a layout with graphs for each sensor data type
app.layout = html.Div([
    html.H1("Real-time Sensor Data Dashboard"),
    dcc.Graph(id='gps-graph'),
    dcc.Graph(id='imu-graph'),
    dcc.Graph(id='sonar-graph'),
    dcc.Graph(id='radar-graph'),
    dcc.Graph(id='ais-graph'),
    dcc.Graph(id='windweather-graph'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    )
])

# Add a callback to update the graphs with new sensor data
@app.callback(
    [Output('gps-graph', 'figure'),
     Output('imu-graph', 'figure'),
     Output('sonar-graph', 'figure'),
     Output('radar-graph', 'figure'),
     Output('ais-graph', 'figure'),
     Output('windweather-graph', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_graphs(n):
    # Simulate sensor data
    gps_data = {'latitude': [pd.Timestamp.now()], 'longitude': [pd.Timestamp.now()]}
    imu_data = {'acceleration': [pd.Timestamp.now()], 'rotation': [pd.Timestamp.now()]}
    sonar_data = {'distance': [pd.Timestamp.now()]}
    radar_data = {'obstacle_distance': [pd.Timestamp.now()]}
    ais_data = {'speed': [pd.Timestamp.now()], 'heading': [pd.Timestamp.now()]}
    windweather_data = {'wind_speed': [pd.Timestamp.now()], 'wind_direction': [pd.Timestamp.now()]}

    gps_fig = go.Figure(data=[go.Scatter(x=gps_data['latitude'], y=gps_data['longitude'], mode='lines+markers')])
    imu_fig = go.Figure(data=[go.Scatter(x=imu_data['acceleration'], y=imu_data['rotation'], mode='lines+markers')])
    sonar_fig = go.Figure(data=[go.Scatter(x=sonar_data['distance'], y=sonar_data['distance'], mode='lines+markers')])
    radar_fig = go.Figure(data=[go.Scatter(x=radar_data['obstacle_distance'], y=radar_data['obstacle_distance'], mode='lines+markers')])
    ais_fig = go.Figure(data=[go.Scatter(x=ais_data['speed'], y=ais_data['heading'], mode='lines+markers')])
    windweather_fig = go.Figure(data=[go.Scatter(x=windweather_data['wind_speed'], y=windweather_data['wind_direction'], mode='lines+markers')])

    return gps_fig, imu_fig, sonar_fig, radar_fig, ais_fig, windweather_fig

if __name__ == '__main__':
    app.run_server(debug=True)

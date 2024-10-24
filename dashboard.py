import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from flask import request, jsonify
import matplotlib.pyplot as plt
import time

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server

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

# Global variable to store sensor data
sensor_data = {
    "GPS": {"latitude": [], "longitude": []},
    "IMU": {"acceleration": [], "rotation": []},
    "Sonar": {"distance": []},
    "Radar": {"obstacle_distance": []},
    "AIS": {"speed": [], "heading": []},
    "WindWeather": {"wind_speed": [], "wind_direction": []}
}

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
    gps_fig = go.Figure(data=[go.Scatter(x=sensor_data['GPS']['latitude'], y=sensor_data['GPS']['longitude'], mode='lines+markers')])
    imu_fig = go.Figure(data=[go.Scatter(x=sensor_data['IMU']['acceleration'], y=sensor_data['IMU']['rotation'], mode='lines+markers')])
    sonar_fig = go.Figure(data=[go.Scatter(x=sensor_data['Sonar']['distance'], y=sensor_data['Sonar']['distance'], mode='lines+markers')])
    radar_fig = go.Figure(data=[go.Scatter(x=sensor_data['Radar']['obstacle_distance'], y=sensor_data['Radar']['obstacle_distance'], mode='lines+markers')])
    ais_fig = go.Figure(data=[go.Scatter(x=sensor_data['AIS']['speed'], y=sensor_data['AIS']['heading'], mode='lines+markers')])
    windweather_fig = go.Figure(data=[go.Scatter(x=sensor_data['WindWeather']['wind_speed'], y=sensor_data['WindWeather']['wind_direction'], mode='lines+markers')])

    return gps_fig, imu_fig, sonar_fig, radar_fig, ais_fig, windweather_fig

# New route to handle sensor data updates
@server.route('/update', methods=['POST'])
def update_sensor_data():
    global sensor_data
    data = request.get_json()
    for sensor, values in data.items():
        for key, value in values.items():
            sensor_data[sensor][key].append(value)
    return jsonify({"status": "success"})

class Dashboard:
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data

    def plot_gps_data(self):
        latitudes = [data[0] for data in self.sensor_data]
        longitudes = [data[1] for data in self.sensor_data]
        
        plt.figure(figsize=(10, 6))
        plt.plot(longitudes, latitudes, marker='o', linestyle='-')
        plt.title('GPS Data Plot')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.grid(True)
        plt.show()

    def update_live_data(self, new_data):
        self.sensor_data.append(new_data)
        self.plot_gps_data()

# Example of live update usage
if __name__ == "__main__":
    sensor_data = [(34.0, -118.0), (35.0, -119.0)]
    dashboard = Dashboard(sensor_data)

    for _ in range(5):
        new_data = (34.0 + 0.1 * _, -118.0 + 0.1 * _)
        dashboard.update_live_data(new_data)
        time.sleep(1)

if __name__ == '__main__':
    app.run_server(debug=True)

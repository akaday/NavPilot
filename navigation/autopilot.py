import pandas as pd
from .sensors import GPSSensor, IMUSensor, SonarSensor, RadarSensor, AISSensor, WindWeatherSensor
import requests
import json

class Autopilot:
    def __init__(self):
        self.gps_sensor = GPSSensor()
        self.imu_sensor = IMUSensor()
        self.sonar_sensor = SonarSensor()
        self.radar_sensor = RadarSensor()
        self.ais_sensor = AISSensor()
        self.wind_weather_sensor = WindWeatherSensor()

    def start(self):
        print("Autopilot started")
        self.print_sensor_data()

    def process_reel_data(self, file_path):
        try:
            data = pd.read_csv(file_path)
            # Process the data as needed
            print("Reel data processed successfully")
        except Exception as e:
            print(f"Error processing reel data: {e}")

    def gather_sensor_data(self):
        gps_data = self.gps_sensor.get_coordinates()
        imu_data = self.imu_sensor.get_orientation()
        sonar_data = self.sonar_sensor.get_distance()
        radar_data = self.radar_sensor.get_obstacle_distance()
        ais_data = self.ais_sensor.get_ship_data()
        wind_weather_data = self.wind_weather_sensor.get_wind_data()
        return {
            "GPS": {
                "latitude": gps_data[0],
                "longitude": gps_data[1]
            },
            "IMU": {
                "acceleration": imu_data[0],
                "rotation": imu_data[1]
            },
            "Sonar": {
                "distance": sonar_data
            },
            "Radar": {
                "obstacle_distance": radar_data
            },
            "AIS": {
                "speed": ais_data["speed"],
                "heading": ais_data["heading"]
            },
            "WindWeather": {
                "wind_speed": wind_weather_data[0],
                "wind_direction": wind_weather_data[1]
            }
        }

    def print_sensor_data(self):
        sensor_data = self.gather_sensor_data()
        for sensor, data in sensor_data.items():
            print(f"{sensor} data: {data}")

    def send_sensor_data_to_dashboard(self):
        sensor_data = self.gather_sensor_data()
        try:
            response = requests.post('http://localhost:8050/update', json=sensor_data)
            if response.status_code == 200:
                print("Sensor data sent to dashboard successfully")
            else:
                print(f"Failed to send sensor data to dashboard: {response.status_code}")
        except Exception as e:
            print(f"Error sending sensor data to dashboard: {e}")

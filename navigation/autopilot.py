import pandas as pd
from .sensors import GPSSensor, IMUSensor, SonarSensor, RadarSensor, AISSensor, WindWeatherSensor

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
            "GPS": gps_data,
            "IMU": imu_data,
            "Sonar": sonar_data,
            "Radar": radar_data,
            "AIS": ais_data,
            "WindWeather": wind_weather_data
        }

    def print_sensor_data(self):
        sensor_data = self.gather_sensor_data()
        for sensor, data in sensor_data.items():
            print(f"{sensor} data: {data}")

import random

class GPSSensor:
    def __init__(self):
        self.latitude = None
        self.longitude = None

    def get_coordinates(self):
        self.latitude = round(random.uniform(-90, 90), 6)
        self.longitude = round(random.uniform(-180, 180), 6)
        return self.latitude, self.longitude

class IMUSensor:
    def __init__(self):
        self.acceleration = None
        self.rotation = None

    def get_orientation(self):
        self.acceleration = round(random.uniform(-10, 10), 6)
        self.rotation = round(random.uniform(-180, 180), 6)
        return self.acceleration, self.rotation

class SonarSensor:
    def __init__(self):
        self.distance = None

    def get_distance(self):
        self.distance = round(random.uniform(0, 100), 2)
        return self.distance

class RadarSensor:
    def __init__(self):
        self.obstacle_distance = None

    def get_obstacle_distance(self):
        self.obstacle_distance = round(random.uniform(0, 1000), 2)
        return self.obstacle_distance

class AISSensor:
    def __init__(self):
        self.ship_data = None

    def get_ship_data(self):
        self.ship_data = {
            "speed": round(random.uniform(0, 30), 2),
            "heading": round(random.uniform(0, 360), 2)
        }
        return self.ship_data

class WindWeatherSensor:
    def __init__(self):
        self.wind_speed = None
        self.wind_direction = None

    def get_wind_data(self):
        self.wind_speed = round(random.uniform(0, 100), 2)
        self.wind_direction = round(random.uniform(0, 360), 2)
        return self.wind_speed, self.wind_direction

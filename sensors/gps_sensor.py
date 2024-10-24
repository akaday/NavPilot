import random  # This is just for simulation purposes

class GPSSensor:
    def __init__(self):
        self.latitude = None
        self.longitude = None

    def get_coordinates(self):
        # Simulating GPS data
        self.latitude = round(random.uniform(-90, 90), 6)
        self.longitude = round(random.uniform(-180, 180), 6)
        return self.latitude, self.longitude

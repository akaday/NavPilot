from navigation.autopilot import Autopilot
from src.github_api import create_github_tree

def main():
    autopilot = Autopilot()
    autopilot.start()
    autopilot.process_reel_data("path/to/reel_data.csv")
    autopilot.print_sensor_data()
    create_github_tree()

if __name__ == "__main__":
    main()

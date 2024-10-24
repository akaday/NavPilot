from navigation.autopilot import Autopilot

def main():
    autopilot = Autopilot()
    autopilot.start()
    autopilot.process_reel_data("path/to/reel_data.csv")

if __name__ == "__main__":
    main()

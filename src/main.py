from navigation.autopilot import Autopilot
import threading
import time
import dashboard

def main():
    autopilot = Autopilot()
    autopilot.start()
    autopilot.process_reel_data("path/to/reel_data.csv")
    autopilot.print_sensor_data()

    # Start the dashboard server in a separate thread
    dashboard_thread = threading.Thread(target=dashboard.app.run_server, kwargs={'debug': True})
    dashboard_thread.start()

    # Continuously send sensor data to the dashboard
    while True:
        autopilot.send_sensor_data_to_dashboard()
        time.sleep(1)

if __name__ == "__main__":
    main()

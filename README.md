# NavPilot

NavPilot is an advanced ship navigation autopilot system designed to enhance maritime safety and efficiency. Utilizing state-of-the-art technology, NavPilot integrates seamlessly with existing maritime navigation systems to provide autonomous navigation and decision-making support.

## Features

- **Autonomous Navigation**: Advanced algorithms for precise route planning and course correction.
- **Sensor Integration**: Supports various sensor types for real-time environmental monitoring.
- **Dynamic Decision Making**: Adapts to changing marine conditions for optimal performance.
- **User-Friendly Interface**: Intuitive controls and displays for easy operation.
- **Reel Data Automation**: Automates the processing of reel data for enhanced operational efficiency.

## Installation

To install NavPilot, clone the repository and install the required dependencies:

```sh
git clone https://github.com/YourUsername/NavPilot.git
cd NavPilot
pip install -r requirements.txt
```

## Usage

To start the NavPilot system and process reel data, run the following command:

```sh
python src/main.py
```

Ensure that the reel data file is located at the specified path in the `process_reel_data` method call within `src/main.py`.

## Reel Data Automation

NavPilot includes a feature for automating the processing of reel data. This feature reads and processes reel data from a specified file, enhancing the system's operational efficiency. The processed data can be used for various analytical and decision-making purposes.

## Sensor Integration

NavPilot integrates several key sensors to enhance navigation and decision-making:

- **GPS (Global Positioning System)**: Determines the precise location of the ship.
- **IMU (Inertial Measurement Unit)**: Measures acceleration and rotation, helping with orientation and stability.
- **Sonar**: Detects underwater obstacles.
- **Radar**: Detects above-water obstacles and other vessels.
- **AIS (Automatic Identification System)**: Tracks nearby ships and provides data like speed and heading.
- **Wind and Weather Sensors**: Measures wind speed, direction, and weather conditions.

## Real-time Data Visualization

NavPilot now includes a real-time data visualization dashboard using Plotly Dash. This dashboard allows you to visualize sensor data in real-time, providing a comprehensive view of the ship's environment and status.

### Running the Dashboard

To run the real-time data visualization dashboard, follow these steps:

1. Ensure that you have installed the required dependencies by running:
    ```sh
    pip install -r requirements.txt
    ```

2. Start the NavPilot system and the dashboard by running:
    ```sh
    python src/main.py
    ```

3. Open your web browser and navigate to `http://localhost:8050` to view the dashboard.

### Example Code

Here's an example of how to use the integrated sensors with the `Autopilot` class:

```python
# src/main.py

from navigation.autopilot import Autopilot

def main():
    autopilot = Autopilot()
    autopilot.start()
    autopilot.process_reel_data("path/to/reel_data.csv")
    autopilot.print_sensor_data()

if __name__ == "__main__":
    main()
```

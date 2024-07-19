# hotel-temperature

## Overview

This project involves creating an IoT temperature monitoring system that reads temperature data from a sensor, publishes it to an MQTT broker, and provides a mechanism to check and alert if the temperature exceeds a certain threshold. It also exposes this data via a simple HTTP API for easy access.

## Components

1. **Publisher Program**: Reads temperature data from a sensor and publishes it to an MQTT broker every 60 seconds.
2. **Sub Program**: Sub to the MQTT topic, checks if the temperature exceeds a threshold continuously for 5 minutes, raises an alarm if the condition is met, and saves the data locally.
3. **Server Program**: Provides an HTTP API to retrieve the most recent temperature data from local storage.

## Requirements

- Python 3.x
- `paho-mqtt` library
- `Adafruit_DHT` library (for DHT11 sensor)
- `Flask` library (for the HTTP server)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/iot-temperature-monitoring.git
   cd iot-temperature-monitoring

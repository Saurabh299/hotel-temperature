# hotel-temperature

## Overview

This extend includes making an IoT temperature checking framework that peruses temperature information from a sensor, distributes it to an MQTT broker, and gives a component to check and caution in the event that the temperature surpasses a certain limit. It moreover uncovered this information through a basic HTTP API for simple get to.

## Components

1. MQTT Program:
peruses temperature information from a sensor and distributes it to an MQTT broker each 60 seconds.
2. **Sub Program**:
Sub to the MQTT theme, it checks on the off chance that the temperature surpasses a edge persistently for 5 minutes, raises an caution in the event that the condition is met, and spares the information locally.
3. API Program:
Gives an HTTP API to recover the foremost later temperature information from neighborhood capacity.

## Requirements

Python 3.x
'paho-mqtt' library
- 'Adafruit_DHT' library (for DHT11 sensor)
- 'Flask' library (for the HTTP server)

 

import paho.mqtt.client as mqtt
import time
import Adafruit_DHT

# MQTT settings
BROKER = 'broker.hivemq.com'  # Broker address
PORT = 1883
TOPIC = 'hotelTemperature' #project name

# Sensor settings
sensor = Adafruit_DHT.DHT11
pin = 4 # define GPIO pin for connecting with the temperature sensor DHT11

# Function to read temperature from the DHT11 sensor
def readTemperature():
    temperature = Adafruit_DHT.read_retry(sensor, pin)
    if temperature is not None:
        print(f"Temp={temperature:.1f}*C")
        return temperature
    else:
        print("Failed for taking data from the temperature sensor")
        return None

# Callback function for client connected with the server
def onConnect(client, userdata, flags, rc):
    print(f"Connected and result code {rc}")

# Set up the MQTT client for connection with the server
client = mqtt.Client()
client.onConnect = onConnect

client.connect(BROKER, PORT, 60)

client.loop_start()

try:
    while True:
        temperature = readTemperature()
        if temperature is not None:
            print(f"Publishing temperature: {temperature}")
            client.publish(TOPIC, f"{temperature:.1f}")  # temperature as a formatted string
        time.sleep(60)  # Wait 60 sec for next data
except KeyboardInterrupt:
    print("Publisher stop.")
    # End the client and discoonected form server
finally:
    client.loop_stop()
    client.disconnect()

import paho.mqtt.client as mqtt
import time
import Adafruit_DHT

# MQTT settings
BROKER = 'broker.hivemq.com'  # Broker address
PORT = 1883
TOPIC = 'hotel/temperature'

# Sensor settings
sensor = Adafruit_DHT.DHT11
pin = 4

# Function to read temperature from the DHT11 sensor
def readTemperature():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if temperature is not None:
        print(f"Temp={temperature:.1f}*C")
        return temperature
    else:
        print("Failed for taking data from the temperature sensor")
        return None

# Callback function for client connected with the server
def onConnect(client, userdata, flags, rc):
    print(f"Connected and result code {rc}")

# Set up the MQTT client
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
    print("Publisher stopped.")
finally:
    client.loop_stop()
    client.disconnect()

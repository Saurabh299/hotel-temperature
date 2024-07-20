import paho.mqtt.client as mqtt # libery for MQTT setup
import time
from datetime import datetime

# MQTT settings
BROKER = 'broker.hivemq.com'  # broker address
PORT = 1883
TOPIC = 'hotel/temperature'
THRESHOLD = 25.0  # Threshold value in Celsius
DURATION = 5 * 60  # Duration to check for in seconds (5 minutes)

temperatureData = []

# Callback for when the client receives a connection response from the server.
def onConnect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC)

# Callback for when a send message is received from the server.
def onMessage(client, userdata, msg):
    global temperatureData
    try:
        temperature = float(msg.payload.decode())
        timestamp = datetime.now()
        temperatureData.append((timestamp, temperature))
        
        # Save data locally
        with open('temperatureData.txt', 'a') as f:
            f.write(f"{timestamp}, {temperature}\n")
        
        # Check for alarm condition
        check_alarm()
    except Exception as e:
        print(f"Error processing message: {e}")

# Function to check if the alarm condition is met
def check_alarm():
    global temperatureData
    now = datetime.now()
    recent_data = [temp for (time, temp) in temperatureData if (now - time).total_seconds() <= DURATION]
    
    if len(recent_data) >= 5 and all(temp > THRESHOLD for temp in recent_data):
        print("ALARM: Threshold exceed for the last 5 minutes.")

# Set up the MQTT client
client = mqtt.Client()
client.onConnect = onConnect
client.onMessage = onMessage

client.connect(BROKER, PORT, 60)

# Start the MQTT client loop
client.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Subscriber stop.")
    #End the client loop and disconnected with the server
finally:
    client.loop_stop()
    client.disconnect()

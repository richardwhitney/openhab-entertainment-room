from sense_hat import SenseHat
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
sense = SenseHat()

Broker = "127.0.0.1"


pub_topic = "testing/mqtt/"       # send messages to this topic


############### sensehat inputs ##################

def read_temp():
    t = sense.get_temperature()
    t = round(t, 2)
    return t

def read_humidity():
    h = sense.get_humidity()
    h = round(h, 2)
    return h

def read_pressure():
    p = sense.get_pressure()
    p = round(p, 2)
    return p

def display_sensehat(message):
    sense.show_message(message)
    time.sleep(10)

############### MQTT section ##################

# when connecting to mqtt do this;

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

# when receiving a mqtt message do this;

def on_message(client, userdata, msg):
    message = str(msg.payload)
    print(msg.topic+" "+message)
    display_sensehat(message)

def on_publish(client, obj, mid):
    print("Message ID: " + str(mid))


client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.connect(Broker, 1883)
client.loop_start()

while True:
    temperature = read_temp()
    humidity = read_humidity()
    pressure = read_pressure()
    client.publish(pub_topic + "temperature", str(temperature))
    client.publish(pub_topic + "humidity", str(humidity))
    client.publish(pub_topic + "pressure", str(pressure))
    time.sleep(15)
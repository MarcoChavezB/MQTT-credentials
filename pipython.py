import time
import paho.mqtt.client as mqtt
import ssl
import json
import _thread
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.tls_set(ca_certs='./rootCA.pem', certfile='./e2b8c2dc40c4e0591171f7bd988aa019a0072565f11d1e79268634f5f1b2a859-certificate.pem.crt', keyfile='./e2b8c2dc40c4e0591171f7bd988aa019a0072565f11d1e79268634f5f1b2a859-private.pem.key', tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect("a169mg5ru5h2z1-ats.iot.us-east-2.amazonaws.com", 8883, 60) #Taken from REST API endpoint - Use your own.

def intrusionDetector(Dummy):
    while (1):    
        x = GPIO.input(21)
        if (x == 0): 
            print("Just Awesome") 
            client.publish("device/data", payload="Hello from BinaryUpdates!!" , qos=0, retain=False)
        time.sleep(5)

_thread.start_new_thread(intrusionDetector,("Create intrusion Thread",))

client.loop_forever()

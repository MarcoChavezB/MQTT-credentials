import paho.mqtt.client as mqtt
import ssl
import _thread

# Configuración de MQTT   PONERLO EN TEST AWS 
topic = "device/data"

def on_connect(client, userdata, flags, rc):
    print("Conectado al broker MQTT con resultado: " + str(rc))

# Configuración del cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect

# Configuración TLS CREDENCIALES EN AWS EN EL REPOSITORIO 
client.tls_set(
    ca_certs='./AmazonRootCA1.pem', 
    certfile='./cec69141d6f3a0869a78f2331a3b6acebf6bc9ddb27a738dc3945c2ea4a99618-certificate.pem.crt', 
    keyfile='./cec69141d6f3a0869a78f2331a3b6acebf6bc9ddb27a738dc3945c2ea4a99618-private.pem.key', 
    tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)

# Conexión 
client.connect("a169mg5ru5h2z1-ats.iot.us-east-2.amazonaws.com", 8883, 60)


def send_message(key):
    client.publish(topic, payload=key, qos=0, retain=False)
    
def main():
    print("Presiona WASD para mover y Q para salir")

    while True:
        key = input(": ")
        
        if key.lower() == 'q':
            break
        elif key.lower() in ['w', 'a', 's', 'd']:
            send_message(key.lower())
        else:
            print("Tecla no válida. Presiona WASD para mover y Q para salir")


_thread.start_new_thread(main, ())

client.loop_forever()

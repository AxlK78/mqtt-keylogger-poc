import paho.mqtt.client as mqtt

# Remplace "mon_projet_12345" par un mot unique pour ne pas mélanger tes messages
TOPIC = "mon_projet_12345/texte"

def on_message(client, userdata, msg):
    print(msg.payload.decode())

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

client.connect("broker.emqx.io", 1883)
client.subscribe(TOPIC)

print("En attente de texte...")
client.loop_forever()
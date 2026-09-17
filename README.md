# MQTT Input Streamer & Logger (POC Educatif)

Ce projet est une preuve de concept (POC) demontrant la capture d'evenements clavier locaux et leur transmission asynchrone vers un courtier MQTT public via Python.

[AVERTISSEMENT LEGAL & ETHIQUE]
Ce projet est developpe a des fins strictement pedagogiques, d'apprentissage des protocoles IoT (MQTT) et de l'architecture evenementielle. L'utilisation d'outils de capture de frappe sans le consentement explicite et eclaire de l'utilisateur est illegale.

---

## Architecture du Projet

Le depot contient deux composants principaux ainsi qu'un fichier de specification PyInstaller :

* **keylog.py** : Script client qui intercepte les frappes clavier a l'aide de la bibliotheque pynput, agrege le texte en memoire de maniere thread-safe (threading.Lock), puis publie periodiquement le tampon via MQTT.
* **server.py** : Ecouteur MQTT qui s'abonne au flux de messages et affiche les donnees recues en temps reel dans la console.
* **keylog.spec** : Fichier de build PyInstaller configure pour compiler le client en executable autonome sans console (console=False).

---

## Prerequis & Installation

### 1. Cloner le depot
```bash
git clone https://github.com/votre-utilisateur/votre-repo.git
cd votre-repo
```

### 2. Installer les dependances
Assurez-vous d'avoir Python 3.8+ installe, puis executez :
```bash
pip install pynput paho-mqtt pyinstaller
```

---

## Utilisation

### Etape 1 : Demarrer le recepteur (server.py)
Dans un premier terminal :
```bash
python server.py
```

### Etape 2 : Lancer le client d'envoi (keylog.py)
Dans un second terminal :
```bash
python keylog.py
```

**Note de configuration :**
Pensez a modifier la variable TOPIC dans keylog.py et server.py pour eviter d'entrer en conflit avec d'autres utilisateurs du broker public EMQX (broker.emqx.io).

---

## Compilation en Executable (.exe)

Pour compiler le client en binaire autonome avec PyInstaller :

```bash
pyinstaller keylog.spec
```

L'executable genere sera disponible dans le dossier dist/.

---

## Licence

Ce projet est distribue sous licence MIT. Consultez le fichier LICENSE pour plus de details.

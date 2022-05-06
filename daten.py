from datetime import datetime
import json
from json import loads, dumps


def speichern(datei, key, value):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    # print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def eingabe_speichern(eingabe):
    datei_name = "eingaben_nutzer.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, eingabe)
    return zeitpunkt, eingabe


"""def eingabe_laden():
    datei_name = "eingaben_nutzer.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt
"""
import json


def speichern(frage1):
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        eintraege = []

    eintrag = ("Frage 1: " + frage1)

    eintraege.append(eintrag)

    with open("datenbank.json", "w") as datenbank:
        json.dump(eintraege, datenbank) # eintrag in datenbank
    return "Daten gespeichert"
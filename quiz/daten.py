import json


def speichern(aktivitaet, dauer):
    try:
        with open("datebank.json", "r") as datenbank:
        eintraege = json.load(datenbank)
    except:
        eintraege = []
    eintrag = {aktivitaet, dauer}

    eintraege.append(eintrag)

    with open("datebank.json", "w") as datenbank:
        json.dump(eintraege, datenbank)
    return "Daten wurden gespeichert"

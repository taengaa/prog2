import json


def speichern(frage1, frage2, frage3, frage4, frage5, frage6, frage7, frage8, frage9, frage10):

    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        eintraege = []

    eintrag = (frage1, frage2, frage3, frage4, frage5, frage6, frage7, frage8, frage9, frage10)

    eintraege.append(eintrag)

    with open("datenbank.json", "w") as datenbank:
        json.dump(eintraege, datenbank) # eintrag in datenbank
    return eintraege

def laden():
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        eintraege = []
    return eintraege

import json


def speichern(frage1, frage2, frage3, frage4, frage5, frage6, frage7, frage8, frage9, frage10):
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        eintraege = []

    eintrag = ("Frage 1: " + frage1, "Frage 2: " + frage2, "Frage 3: " + frage3, "Frage 4: " + frage4, "Frage 5: " + frage5, "Frage 6: " + frage6, "Frage 7: " + frage7, "Frage 8: " + frage8, "Frage 9: " + frage9, "Frage 10: " + frage10)

    eintraege.append(eintrag)

    with open("datenbank.json", "w") as datenbank:
        json.dump(eintraege, datenbank) # eintrag in datenbank
    return "Daten gespeichert"
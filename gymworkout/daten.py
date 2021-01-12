import json


def speichern(uebung, dauer, muskelgruppe, satz1, satz2, satz3):
    # hier wird versucht die Datei json im readmodus zu öffnen, mit try da die Datei leer oder nicht existieren könnte
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        print("Beim speichern konnte keine vorhandene Datenbank gefunden werden")
        eintraege = []

    eintrag = (uebung, dauer, muskelgruppe, satz1, satz2, satz3)

    eintraege.append(eintrag)  # neuer Eintrag wird hinzugefügt

    """
    json dump nimmt was entgegen und schreibt es als json Datei
    der write Modus überschreibt bereits vorhandene Einträge, dies ist aber okay da bereits vorhin abgespeichert wurden 
    inkl. neue Einträge
    somit muss hier nicht Eintrag gespeichert werden, sondern eintraege somit sind dann die Alten und Neuen dabei
    """
    with open("datenbank.json", "w") as datenbank:
        json.dump(eintraege, datenbank)

    return uebung, dauer, muskelgruppe, satz1, satz2, satz3


def laden():
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        print("Beim laden konnte keine vorhandene Datenbank gefunden werden")
        eintraege = []

    return eintraege


def liste_uebungen_json(neue_uebung):
    # hier wird versucht die Datei json im readmodus zu öffnen, mit try da die Datei leer oder nicht existieren könnte
    try:
        with open("liste_uebungen.json", "r", encoding="utf-8") as liste_uebungen:
            eintraege = json.load(liste_uebungen)
    except:
        print("Beim speichern konnte keine vorhandene Liste gefunden werden")
        eintraege = []

    eintraege.append(neue_uebung)  # neuer Eintrag wird hinzugefügt

    with open("liste_uebungen.json", "w",  encoding="utf-8") as liste_uebungen:
        json.dump(eintraege, liste_uebungen)


def liste_laden(datenbankdatei):
    try:
        with open(datenbankdatei, "r", encoding="utf-8") as liste_uebungen:
            eintraege = json.load(liste_uebungen)
    except:
        print("Beim laden konnte keine vorhandene Datenbank gefunden werden")
        eintraege = []

    return eintraege



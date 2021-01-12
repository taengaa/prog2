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


def liste_uebungen_json():
    # hier wird versucht die Datei json im readmodus zu öffnen, mit try da die Datei leer oder nicht existieren könnte
    try:
        with open("liste_uebungen.json", "r") as liste_uebungen:
            eintraege = json.load(liste_uebungen)
    except:
        print("Beim speichern konnte keine vorhandene Liste gefunden werden")
        eintraege = []

    eintrag = ("Bankdrücken", "Back Extension", "Bizeps Curls", "Klimmzüge", "Beinpresse", "Deadlift", "Lattzug")

    eintraege.append(eintrag)  # neuer Eintrag wird hinzugefügt


def liste_uebungen_json_laden():
    try:
        with open("liste_uebungen.json", "r") as liste_uebungen:
            eintraege = json.load(liste_uebungen)
    except:
        print("Beim laden konnte keine vorhandene Datenbank gefunden werden")
        eintraege = []

    return eintraege



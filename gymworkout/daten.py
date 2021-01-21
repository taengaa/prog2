import json

"""
Damit werden die Eingaben in einer Liste gespeichert. Die neuen Einträge werden hinzugefügt und dann 
werden alle Einträge überschrieben aber dank json dump können die alten sowohl als auch die neuen Einträge erneut 
in die Liste geladen werden.
"""
def speichern(uebung, dauer, muskelgruppe, gewicht, satz1, satz2, satz3):
    # Hier wird versucht die Datei json im readmodus zu öffnen, mit try da die Datei leer oder nicht existieren könnte.
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        print("Beim speichern konnte keine vorhandene Datenbank gefunden werden")
        eintraege = []

    eintrag = (uebung, dauer, muskelgruppe, gewicht, satz1, satz2, satz3)

    eintraege.append(eintrag)  # neuer Eintrag wird hinzugefügt

    """
    Json dump nimmt etwas entgegen und schreibt es als json Datei,
    der write Modus überschreibt bereits vorhandene Einträge, dies ist kein Problem da diese bereits vorhin abgespeichert 
    wurden inkl. der neuer Einträge.
    Somit muss hier nicht Eintrag gespeichert werden, sondern eintraege somit sind dann die Alten und Neuen dabei. Mit 
    dem schreibmododus wird der gesamte json Inhalt überschrieben, mit dump können wird aber die neuen und alten 
    Einträge wieder in die Datenbank laden.
    """
    with open("datenbank.json", "w") as datenbank:
        json.dump(eintraege, datenbank)

    return uebung, dauer, muskelgruppe, gewicht, satz1, satz2, satz3


# Hier werden die gespeicherten Daten versucht zu laden.
def laden():
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        print("Beim laden konnte keine vorhandene Datenbank gefunden werden")
        eintraege = []

    return eintraege


"""
Die Liste der möglichen Übungen wird zuerst im readmodus ausgelesen und dann wird mit append die neue Übung hinzugefügt.
Im Schreibmodus werden dann alle Übungen überschrieben, mit dump eintraege können die alten sowie neuen eintraege 
aber wieder neu in die json Datei geladen werden.
"""
def liste_uebungen_json(neue_uebung):
    # Hier wird versucht die Datei json im readmodus zu öffnen, mit try da die Datei leer oder nicht existieren könnte.
    try:
        with open("liste_uebungen.json", "r", encoding="utf-8") as liste_uebungen:
            eintraege = json.load(liste_uebungen)
    except:
        print("Beim speichern konnte keine vorhandene Liste gefunden werden")
        eintraege = []

    eintraege.append(neue_uebung)  # neuer Eintrag wird hinzugefügt

    with open("liste_uebungen.json", "w",  encoding="utf-8") as liste_uebungen:
        json.dump(eintraege, liste_uebungen)

"""
Die Möglichkeiten im Dropdown, werden durch diese Funktion geladen.Sowohl die Muskelgruppen als auch die Übungen,
können mit der gleichen Funktion geladen werden.
"""
def liste_laden(datenbankdatei):
    try:
        with open(datenbankdatei, "r", encoding="utf-8") as liste_uebungen:
            eintraege = json.load(liste_uebungen)
    except:
        print("Beim laden konnte keine vorhandene Datenbank gefunden werden")
        eintraege = []

    return eintraege


# Im Prinzip das gleiche wie neue Übung, einfach mit Gewicht.
def liste_gewichte_json(neues_gewicht):
    # hier wird versucht die Datei json im readmodus zu öffnen, mit try da die Datei leer oder nicht existieren könnte
    try:
        with open("gewichte.json", "r", encoding="utf-8") as liste_gewichte:
            eintraege = json.load(liste_gewichte)
    except:
        print("Beim speichern konnte keine vorhandene Liste gefunden werden")
        eintraege = []

    eintraege.append(neues_gewicht)  # neuer Eintrag wird hinzugefügt

    with open("gewichte.json", "w",  encoding="utf-8") as liste_gewichte:
        json.dump(eintraege, liste_gewichte)

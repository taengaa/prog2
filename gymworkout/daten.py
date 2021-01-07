import json


def speichern(dauer, workoutart):
    # hier wird versucht die Datei json im readmodus zu öffnen, mit try da die Datei leer oder nicht existieren könnte
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        print("Beim speichern konnte keine vorhandene Datenbank gefunden werden")
        eintraege = []

    eintrag = (dauer, workoutart)

    eintraege.append(eintrag)  # neuer Eintrag wird hinzugefügt

    """
    json dump nimmt was entgegen und schreibt es als json Datei
    der write Modus überschreibt bereits vorhandene Einträge, dies ist aber okay da bereits vorhin abgespeichert wurden 
    inkl. neue Einträge
    somit muss hier nicht eintrag gespeichert werden, sondern eintraege somit sind dann die alten und neuen dabei
    """
    with open("datenbank.json", "w") as datenbank:
        json.dump(eintraege, datenbank)

    return dauer, workoutart

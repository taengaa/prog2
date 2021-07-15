""""
Diese Funktion iteriert durch die gespeicherten Einträge in der Liste(datenbank.json). Wenn das erste Element(index 0)
der Liste nicht im dictionary vorhanden ist, dann wird es erstellt und zwar mit Übung und Zeit. Ist die Übung aber
bereits im Dictionary, dann wird die Zeit ((eintrag[1]) der datenbank.json Liste) im Dictionary aufaddiert.
"""
def summe_der_workouts(gespeicherten_eintraege):
    workout_dictionary = {}
    for eintrag in gespeicherten_eintraege:
        # wenn der Eintrag noch nicht vorhanden ist dann wird er erstellt
        if not workout_dictionary.get(eintrag[0]):
            workout_dictionary[eintrag[0]] = float(eintrag[1])
        # ist aber der Eintrag bereits vorhanden, dann soll die Zeit addiert werden
        else:
            workout_dictionary[eintrag[0]] += float(eintrag[1])

    # Hier werden die Zeiten im Dictionary addiert und dann dem Dictionary als neuer Eintrag hinzugefügt
    summe_zeit = sum(workout_dictionary.values())
    workout_dictionary["Gesamtzeit aller Workouts"] = summe_zeit

    # Mit len werden die Listen in datenbank.json gezählt. Dies gibt dann die Anzahl Einträge.
    anzahl_zeiten_in_dict = len(gespeicherten_eintraege)
    durchschnittszeit = summe_zeit/anzahl_zeiten_in_dict
    workout_dictionary["Durchschnittszeit/Workout"] = durchschnittszeit


    return workout_dictionary


"""
Anstatt Übung und Zeit wie oben, wird hier Übung und Gewicht einem Dictionary hinzugefügt und sobald vorhanden, werden
die Gewichte aufaddiert.
"""
def gesamtgewicht_pro_muskelgruppe(gespeicherten_eintraege):
    gesamtgewicht = {}
    for eintrag in gespeicherten_eintraege:
        # wenn der Eintrag im dict noch nicht vorhanden ist dann wird er erstellt
        if not gesamtgewicht.get(eintrag[0]):
            gesamtgewicht[eintrag[0]] = float(eintrag[3])
        # ist aber der Eintrag bereits vorhanden, dann soll das Gewicht addiert werden
        else:
            gesamtgewicht[eintrag[0]] += float(eintrag[3])

    summe_gesamtgewicht = sum(gesamtgewicht.values())
    gesamtgewicht["Gesamtgewicht aller Workouts"] = summe_gesamtgewicht

    return gesamtgewicht

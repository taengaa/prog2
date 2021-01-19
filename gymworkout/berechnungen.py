def summe_der_workouts(gespeicherten_eintraege):
    workout_dictionary = {}
    for eintrag in gespeicherten_eintraege:
        # wenn der Eintrag noch nicht vorhanden ist dann wird er erstellt
        if not workout_dictionary.get(eintrag[0]):
            workout_dictionary[eintrag[0]] = float(eintrag[1])
        # ist aber der Eintrag bereits vorhanden, dann soll die Zeit addiert werden
        else:
            workout_dictionary[eintrag[0]] += float(eintrag[1])

    summe_zeit = sum(workout_dictionary.values())
    workout_dictionary["Gesamtzeit aller Workouts"] = summe_zeit

    anzahl_zeiten_in_dict = len(workout_dictionary)
    durchschnittszeit = summe_zeit/anzahl_zeiten_in_dict
    workout_dictionary["Durchschnittszeit"] = durchschnittszeit

    return workout_dictionary


def gesamtgewicht_pro_muskelgruppe(gespeicherten_eintraege):
    gesamtgewicht = {}
    for eintrag in gespeicherten_eintraege:
        # wenn der Eintrag noch nicht vorhanden ist dann wird er erstellt
        if not gesamtgewicht.get(eintrag[0]):
            gesamtgewicht[eintrag[0]] = float(eintrag[3])
        # ist aber der Eintrag bereits vorhanden, dann soll das Gewicht addiert werden
        else:
            gesamtgewicht[eintrag[0]] += float(eintrag[3])

    summe_gesamtgewicht = sum(gesamtgewicht.values())
    gesamtgewicht["Gesamtgewicht aller Workouts"] = summe_gesamtgewicht

    return gesamtgewicht


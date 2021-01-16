def summe_der_workouts(gespeicherten_eintraege):
    workout_dictionary = {}
    for eintrag in gespeicherten_eintraege:
        # wenn der Eintrag noch nicht vorhanden ist dann wird er erstellt
        if not workout_dictionary.get(eintrag[0]):
            workout_dictionary[eintrag[0]] = float(eintrag[1])
        # ist aber der Eintrag bereits vorhanden, dann soll die Zeit addiert werden
        else:
            workout_dictionary[eintrag[0]] += float(eintrag[1])
    return workout_dictionary

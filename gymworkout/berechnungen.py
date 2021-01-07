def summe_der_zeitdauer(gespeicherten_eintraege):
    aktidict = {}
    for eintrag in gespeicherten_eintraege:
        # wenn der Eintrag noch nicht vorhanden ist dann wird er erstellt
        if not aktidict.get(eintrag[0]):
            aktidict[eintrag[0]] = float(eintrag[1])
        # ist aber der Eintrag bereits vorhanden, dann soll die Zeit addiert werden
        else:
            aktidict[eintrag[0]] += float(eintrag[1])
    return aktidict
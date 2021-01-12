from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from daten import speichern, laden, liste_uebungen_json, liste_uebungen_json_laden
from berechnungen import summe_der_zeitdauer

app = Flask("tracker")

liste_uebungen = [
        "Bankdrücken",
        "Back Extension",
        "Bizeps Curls",
        "Klimmzüge",
        "Beinpresse",
        "Deadlift",
        "Lattzug"
    ]
# uebungen.append(input)


muskelgruppen = [
        "Arme",
        "Beine",
        "Brust",
        "Rücken",
        "Bauch"
    ]

wiederholungen = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15"
    ]


@app.route('/')
def start():
    ueberschrifts_text = "Willkommen auf der Workout Tracker Website"
    einleitung_text = "Hier können Sie ihre Workouts tracken, was wollen Sie tun?"
    # der Überschrift und Einleitungstext wird in der Start html Datei gerendert
    return render_template(
        'start.html',
        app_name="Workout-Tracker!",  # wird in der Suchkonsole neben dem Favicon angezeigt, im Fenster
        ueberschrift=ueberschrifts_text,
        einleitung=einleitung_text
    )


@app.route('/eingabe', methods=['POST', 'GET'])
def eingabe_formular():

    if request.method == 'POST':
        uebung = request.form['uebung']
        dauer = request.form['dauer']
        muskelgruppe = request.form['muskelgruppe']
        satz1 = request.form['satz1']
        satz2 = request.form['satz2']
        satz3 = request.form['satz3']
        antworten = speichern(uebung, dauer, muskelgruppe, satz1, satz2, satz3)
        # hier wird die Reihenfolge der gespeicherten
        # Elemente in der Datenbank definiert
        # antworten werden durch speichern in einer Liste gespeichert, darum muss diese zuerst in einen String
        # umgewandelt werden
        return 'Gespeicherte Daten: <br>' + str(antworten)
    ueberschrifts_text = "Eingabe der Workouts"
    einleitung_text = "Hier können Sie auswählen, welches Workout sie tracken wollen:"

    return render_template(
        'eingabe.html',
        app_name="Workout-Tracker! / Eingabe",
        ueberschrift=ueberschrifts_text,
        einleitung=einleitung_text,
        uebungen=liste_uebungen,
        muskelgruppen=muskelgruppen,
        wiederholungen=wiederholungen
    )


@app.route('/alle_workouts')
def alle_workouts():
    gespeicherten_eintraege = laden()  # Funktion in daten.py definiert
    ueberschrifts_text = 'Liste von allen Workouts'
    einleitung_text = 'Hier werden alle deine Workouts dargestellt, die du gespeichert hast.'
    return render_template(
        'alle_workouts.html',
        app_name="alle_workouts",
        ueberschrift=ueberschrifts_text,
        einleitung=einleitung_text,
        daten=gespeicherten_eintraege
    )


@app.route('/analyse')
def analyse():
    gespeicherten_eintraege = laden()
    analyse_ergebnis = summe_der_zeitdauer(gespeicherten_eintraege)  # Funktion wird in Berechnungen aufgeführt
    ueberschrifts_text = 'Analyse deiner Workouts'
    einleitung_text = 'Hier werden alle Workouts aufaddiert dargestellt.'
    return render_template(
        'analyse.html',
        app_name="Tracker!",
        ueberschrift=ueberschrifts_text,
        einleitung=einleitung_text,
        daten=analyse_ergebnis
    )


@app.route('/neue_uebung', methods=['POST', 'GET'])
def neue_uebung():

    if request.method == 'POST':
        neue_uebung = request.form['neue_uebung']
        eigabe=liste_uebungen_json(neue_uebung)
        neue_liste_uebungen = liste_uebungen.append(neue_uebung)
        return neue_liste_uebungen

    ueberschrifts_text = 'Neue Übung zur Auswahl hinzufügen'
    einleitung_text = 'Hier kannst du eine neue Übung zur Auswahl im Dropdown hinzufügen.'

    return render_template(
        'neue_uebung.html',
        app_name="neue_uebung",
        ueberschrift=ueberschrifts_text,
        einleitung=einleitung_text,
        uebungen=liste_uebungen
    )


@app.route('/gespeichertes_workout', methods=['POST', 'GET'])
def gespeichertes_workout():
    gespeicherten_eintraege = laden()  # Funktion in daten.py definiert
    ueberschrifts_text = 'Dein Workout'
    einleitung_text = 'Hier wird dein hinzugefügtes Workout dargestellt: Mit einem Klick auf den Button kannst du alle Workouts anzeigen'
    return render_template(
        'gespeichertes_workout.html',
        app_name="Dein Workout",
        ueberschrift=ueberschrifts_text,
        einleitung=einleitung_text,
        daten=gespeicherten_eintraege
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)

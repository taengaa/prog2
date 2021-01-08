from flask import Flask
from flask import render_template
from flask import request

from daten import speichern, laden
from berechnungen import summe_der_zeitdauer

app = Flask("tracker")


uebungen = [
        "Bankdrücken",
        "Back Extension",
        "Bizeps Curls",
        "Klimmzüge",
        "Beinpresse",
        "Deadlift",
        "Velo",
        "Laufband",
        "Lattzug"
    ]
# uebungen.append()

muskelgruppen = [
        "Arme",
        "Beine",
        "Brust",
        "Rücken",
        "Bauch",
        "Cardio"
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


@app.route('/dropdown', methods=['POST', 'GET'])
def dropdown():
    if request.method == 'GET':
        muskelgruppen = ['Beine', 'Arme', 'Rücken', 'Bauch']
        return render_template('dropdown.html', muskelgruppen=muskelgruppen)


@app.route('/eingabe', methods=['POST', 'GET'])
def eingabe_formular():

    if request.method == 'POST':
        dauer = request.form['dauer']
        uebung = request.form['uebung']
        muskelgruppe = request.form['muskelgruppe']
        wiederholung = request.form['wiederholung']
        antworten = speichern(uebung, dauer, muskelgruppe, wiederholung)  # hier wird die Reihenfolge der gespeicherten
        # Elemente in der
        # Datenbank definiert
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
        uebungen=uebungen,
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


if __name__ == "__main__":
    app.run(debug=True, port=5000)

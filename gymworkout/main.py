from flask import Flask
from flask import render_template
from flask import request

from daten import speichern, laden

app = Flask("tracker")


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
        workoutart = request.form['workoutart']
        antworten = speichern(workoutart, dauer) # hier wird die Reihenfolge der gespeicherten Elemente in der
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
        einleitung=einleitung_text
    )


@app.route('/alle_workouts')
def alle_workouts():
    gespeicherten_eintraege = laden()  # Funktion in daten.py definiert
    ueberschrifts_text = 'Liste von allen Workouts'
    einleitung_text = 'Hier werden alle deine Workouts dargestellt, die du gespeichert hast.'
    return render_template(
        'alle_workouts.html',
        app_name="Tracker!",
        ueberschrift=ueberschrifts_text,
        einleitung=einleitung_text,
        daten=gespeicherten_eintraege,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)

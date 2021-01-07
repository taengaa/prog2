from flask import Flask
from flask import render_template
from flask import request

from daten import speichern

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
        antworten = speichern(dauer, workoutart)
        #antworten werden durch speichern in einer Liste gespeichert, darum muss diese zuerst in eine String umgewandelt werden
        return 'Gespeicherte Daten: <br>' + str(antworten)
    ueberschrifts_text = "Eingabe der Workouts"
    einleitung_text = "Hier können Sie auswählen, welches Workout sie tracken wollen:"

    return render_template(
        'eingabe.html',
        app_name="Workout-Tracker! / Eingabe",
        ueberschrift=ueberschrifts_text,
        einleitung=einleitung_text
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)

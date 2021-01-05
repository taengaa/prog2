from flask import Flask
from flask import render_template
from flask import request

app = Flask("tracker")


@app.route('/')
def start():
    ueberschrifts_text = "Willkommen auf der Workout Tracker Website"
    einleitung_text = "Hier können Sie ihre Workouts tracken, was wollen Sie tun?"
    return render_template(
        'start.html',
        app_name="Workout-Tracker!", # wird in der Suchkonsole neben dem Favicon angezeigt, im Fenster
        ueberschrift=ueberschrifts_text,
        einleitung=einleitung_text
    )

@app.route('/eingabe', methods=['POST', 'GET'])
def eingabe_formular():

    if request.method == 'POST':
        dauer = request.form['dauer']
        antworten = dauer
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
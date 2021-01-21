from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for

from daten import speichern, laden, liste_uebungen_json, liste_laden, liste_gewichte_json
from berechnungen import summe_der_workouts, gesamtgewicht_pro_muskelgruppe

app = Flask("tracker")


# Dies ist die Startseite, hier können die 3 Buttons ausgewählt werden.
@app.route('/')
def start():
    ueberschrifts_text = "Willkommen auf der Workout Tracker Website"
    einleitung_text = "Hier können Sie ihre Workouts tracken, was wollen Sie tun?"
    # Der Überschrift und Einleitungstext wird in der Start html Datei gerendert.
    return render_template(
        'start.html',
        app_name="Workout-Tracker!",  # Wird in der Suchkonsole neben dem Favicon angezeigt, im Fenster
        # da der app_name als Titel definiert wurde im header.html <title>{{ app_name }}</title>
        ueberschrift=ueberschrifts_text,
        einleitung=einleitung_text
    )


# Eingabeseite, auf welcher Dauer, workout etc. ausgewählt werden kann.
@app.route('/eingabe', methods=['POST', 'GET'])
def eingabe_formular():

    if request.method == 'POST':
        uebung = request.form['uebung']
        dauer = request.form['dauer']
        muskelgruppe = request.form['muskelgruppe']
        gewicht = request.form['gewicht']
        satz1 = request.form['satz1']
        satz2 = request.form['satz2']
        satz3 = request.form['satz3']
        speichern(uebung, dauer, muskelgruppe, gewicht, satz1, satz2, satz3)  # Speichern in daten.py definiert
        return redirect(url_for("gespeichertes_workout"))
        # Hier wird die Reihenfolge der gespeicherten
        # Elemente in der Datenbank definiert
        # Antworten werden durch speichern in einer Liste gespeichert

    ueberschrifts_text = "Eingabe der Workouts"
    einleitung_text = "Hier können Sie auswählen, welches Übung sie tracken wollen oder eine neue hinzufügen:"

    liste_uebungen = liste_laden("liste_uebungen.json")  # Können beide mit der gleichen Funktion geladen werden,
    muskelgruppen = liste_laden("muskelgruppen.json")    # da die Funktion in daten.py mit datenbankdatei dynamisch ist.
    gewichte = liste_laden("gewichte.json")
    wiederholungen = liste_laden("wiederholungen.json")
    return render_template(
        'eingabe.html',
        app_name="Workout-Tracker! / Eingabe",
        ueberschrift=ueberschrifts_text,
        einleitung=einleitung_text,
        uebungen=liste_uebungen,
        muskelgruppen=muskelgruppen,
        gewichte=gewichte,
        wiederholungen=wiederholungen
    )


@app.route('/alle_workouts/')
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
    gespeicherten_eintraege = laden()  # wird in daten.py definiert
    analyse_ergebnis = summe_der_workouts(gespeicherten_eintraege)  # Funktion wird in berechnungen.py definiert
    summe_gewichte = gesamtgewicht_pro_muskelgruppe(gespeicherten_eintraege)  # Funktion wird in berechnungen.py definiert
    ueberschrifts_text = 'Analyse deiner Workouts'
    einleitung_text = 'Hier werden alle Workouts aufaddiert dargestellt.'
    return render_template(
        'analyse.html',
        app_name="Tracker!",
        ueberschrift=ueberschrifts_text,
        einleitung=einleitung_text,
        daten=analyse_ergebnis,
        summe_gewichte=summe_gewichte
    )


@app.route('/neue_uebung', methods=['POST', 'GET'])
def neue_uebung():

    if request.method == 'POST':
        neue_uebung = request.form['neue_uebung']
        liste_uebungen_json(neue_uebung)
        return redirect(url_for("eingabe_formular"))

    ueberschrifts_text = 'Neue Übung zur Auswahl hinzufügen'
    einleitung_text = 'Hier kannst du eine neue Übung zur Auswahl im Dropdown hinzufügen.'
    liste_uebungen = liste_laden("liste_uebungen.json")

    return render_template(
        'neue_uebung.html',
        app_name="neue_uebung",
        ueberschrift=ueberschrifts_text,
        einleitung=einleitung_text,
        uebungen=liste_uebungen
    )


@app.route('/neues_gewicht', methods=['POST', 'GET'])
def neues_gewicht():

    if request.method == 'POST':
        neues_gewicht = request.form['neues_gewicht']
        liste_gewichte_json(neues_gewicht)
        return redirect(url_for("eingabe_formular"))

    ueberschrifts_text = 'Neues Gewicht zur Auswahl hinzufügen'
    einleitung_text = 'Hier kannst du ein neues Gewicht zur Auswahl im Dropdown hinzufügen.'
    gewichte = liste_laden("gewichte.json")

    return render_template(
        'neues_gewicht.html',
        app_name="neue_uebung",
        ueberschrift=ueberschrifts_text,
        einleitung=einleitung_text,
        gewichte=gewichte
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

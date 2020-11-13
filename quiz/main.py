from flask import Flask
from flask import render_template
from flask import request
from daten import speichern
from flask import redirect

app = Flask("Psychologische Gesundheit")

@app.route('/')
def start():
    ueberschrifts_text = "Willkomen, hier können sie den Corona Psycho Test durchführen."
    einleitung_text = "Die Corona Zeit verlangt nicht nur dem Körper mehr ab sondern auch dem Geist, darum wurde dieser psychologische Test entwickelt. Testen sie nun und erfahren sie, wie es ihrer Psyche geht"
    return render_template('start.html', app_name="Quiz", ueberschrift=ueberschrifts_text, einleitung=einleitung_text)


@app.route('/eingabe', methods=['POST', 'GET'])
def eingabe():

    if request.method == 'POST':
        frage1 = request.form['frage1']
        frage2 = request.form['frage2']
        frage3 = request.form['frage3']
        frage4 = request.form['frage4']
        frage5 = request.form['frage5']
        frage6 = request.form['frage6']
        frage7 = request.form['frage7']
        frage8 = request.form['frage8']
        frage9 = request.form['frage9']
        frage10 = request.form['frage10']
        antwort = speichern(frage1, frage2, frage3, frage4, frage5, frage6, frage7, frage8, frage9, frage10)
        return 'Gespeicherte Daten: <br>' + str(antwort)

    return render_template('index.html', app_name="Quiz - Eingabe")

@app.route('/about')
def about():
    ueberschrifts_text = "Über diese Webapp"
    einleitung_text = "Diese App wurde im Fach Programmierung 2 an der FHGR programmiert."
    return render_template('start.html', app_name="Quiz", ueberschrift=ueberschrifts_text, einleitung=einleitung_text)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
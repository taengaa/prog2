from flask import Flask
from flask import render_template
from flask import request
from daten import speichern
from flask import redirect

app = Flask("Psychologische Gesundheit")

@app.route('/')
def start():
    ueberschrifts_text = "Willkomen, hier können sie den Corona Psycho Test durchführen."
    einleitung_text = "hier können Sie Ihre Aktivitäten tracken. Was wollen Sie tun?"
    return render_template('start.html', app_name="Quiz", ueberschrift=ueberschrifts_text, einleitung=einleitung_text)


@app.route('/eingabe', methods=['POST', 'GET'])
def eingabe():

    if request.method == 'POST':
        frage1 = request.form['frage1']
        antwort = speichern(frage1)
        return 'Gespeicherte Daten: <br>' + str(antwort)

    return render_template('index.html', app_name="Tracker! - Eingabe")

@app.route('/about')
def about():
    ueberschrifts_text = "Über diese Webapp"
    einleitung_text = "Diese App wurde als Demo-App programmiert"
    return render_template('start.html', app_name="Quiz", ueberschrift=ueberschrifts_text, einleitung=einleitung_text)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
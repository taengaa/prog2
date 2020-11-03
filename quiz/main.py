from flask import Flask
from flask import render_template
from flask import request
from daten import speichern
from flask import redirect

app = Flask("Psychologische Gesundheit")


@app.route('/questionaire', methods=["GET", "POST"])
def index():

    if request.method == "POST":
        data = request.form
        print(data)

    return render_template('index.html', name="Simon", app_name="Psychologischer Test")

@app.route('/about')
def about():
    return render_template('about.html', app_name="about")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
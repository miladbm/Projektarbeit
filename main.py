from flask import Flask
from flask import render_template
from flask import request
import json
from json import loads, dumps
from daten import daten_laden
from datetime import datetime
from json import loads, dumps

app = Flask("Projektarbeit")


#Verlinkung auf Hauptseite
@app.route("/")
def start():
    name = "Mirjam"
    cards = [
        {"titel": "Card 0", "inhalt": "Card 1"},
        {"titel": "Card 1", "inhalt": "Card 2"},
        {"titel": "Card 2", "inhalt": "Card 3"},
        {"titel": "Card 2", "inhalt": "Card 4"}
    ]
    return render_template("index.html", name=name, cards=cards)

#Verlinkung auf Formular
@app.route("/formular/", methods=['GET', 'POST'])
def formular():
    if request.method == 'POST':
        data = request.form
        vorname = data["name"]
        gekauft = data["was"]
        ausgegeben = data["betrag"]
        zeitpunkt = datetime.now()


        daten = daten_laden()

        my_dict = {"Vorname": vorname, "Was": gekauft, "Ausgegeben": ausgegeben}
        daten.update({str(zeitpunkt): my_dict})


        with open("eingaben_nutzer.json", "w") as open_file:
            json.dump(daten, open_file, default=str)
        return render_template("formular.html")
    else:
        return render_template("formular.html")

@app.route("/ausgaben/")
def ausgaben():
    with open("eingaben_nutzer.json") as open_file:
        json_as_string = open_file.read()
        my_read_dict = loads(json_as_string)

        return render_template(my_read_dict)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

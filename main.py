from flask import Flask
from flask import render_template
from flask import request
import json
from json import loads, dumps
from daten import *
from datetime import datetime

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

        my_dict = dict()
        my_dict[str(zeitpunkt)] = {"Vorname": vorname, "Was": gekauft, "Ausgegeben": ausgegeben, "Zeitpunkt": zeitpunkt}


        with open("eingaben_nutzer.json", "w") as open_file:
            json.dump(my_dict, open_file, default=str)
        return render_template("formular.html")
    else:
        return render_template("formular.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)

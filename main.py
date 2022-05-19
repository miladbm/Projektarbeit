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
        name = data["name"]
        was = data["was"]
        betrag = data["betrag"]
        zeitpunkt = datetime.now()


        daten = daten_laden()

        my_dict = {"Name": name, "Was": was, "Betrag": betrag}
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

        return render_template("ausgaben.html", eingabe_nutzer=my_read_dict)

@app.route("/berechnung/")
def berechnung():
    with open("eingaben_nutzer.json") as open_file:
        json_as_string = open_file.read()
        my_read_dict = loads(json_as_string)

    summe_mirjam = 0
    summe_luca = 0
    summe_sarina = 0

    # namen = ['Mirjam', 'Luca', 'Sarina']
    # ausgaben = {}
    #
    # for name in namen:
    #     for key, value in my_read_dict.items():
    #         if value['Name'] == name:
    #             try:
    #                 if name in ausgaben.keys():
    #                     ausgaben[name]= ausgaben.get(name,0) + value['Betrag']
    #                 else:
    #                     ausgaben[]



    for key, value in my_read_dict.items():
        if value['Name']=='Mirjam':
            try:
                summe_mirjam += float(value['Betrag'])

            except:
                continue

        elif value['Name']=='Luca':
            try:
                summe_luca += float(value['Betrag'])
            except:
                continue

        elif value['Name']=='Sarina':
            try:
                summe_sarina += float(value['Betrag'])
            except:
                continue

    return render_template("berechnung.html", summe_mirjam=summe_mirjam, summe_luca=summe_luca, summe_sarina=summe_sarina)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

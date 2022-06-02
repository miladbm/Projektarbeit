from flask import Flask
from flask import render_template
from flask import request
import json
from daten import daten_laden
from datetime import datetime
from json import loads
import plotly.express as px
from plotly.offline import plot
import os
from os.path import exists


app = Flask("Projektarbeit")


# Verlinkung auf Hauptseite
@app.route("/")
def start():
    return render_template("index.html")


# Verlinkung auf Formular
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
    if exists("eingaben_nutzer.json"):
        with open("eingaben_nutzer.json") as open_file:
            json_as_string = open_file.read()
            my_read_dict = loads(json_as_string)

        return render_template("ausgaben.html", eingabe_nutzer=my_read_dict)
    else:
        return render_template("daten_loeschen.html")


@app.route("/ausgaben/daten_loeschen")
def daten_loeschen():
    if exists("eingaben_nutzer.json"):
        os.remove("eingaben_nutzer.json")
        return render_template("daten_loeschen.html")
    else:
        return render_template("daten_loeschen.html")


@app.route("/berechnung/")
def berechnung():
    if exists("eingaben_nutzer.json"):
        with open("eingaben_nutzer.json") as open_file:
            json_as_string = open_file.read()
            my_read_dict = loads(json_as_string)

        summe_mirjam = 0
        summe_luca = 0
        summe_sarina = 0

        for key, value in my_read_dict.items():
            if value["Name"] == 'Mirjam':
                try:
                    summe_mirjam += float(value['Betrag'])

                except:
                    continue

            elif value['Name'] == 'Luca':
                try:
                    summe_luca += float(value['Betrag'])
                except:
                    continue

            elif value['Name'] == 'Sarina':
                try:
                    summe_sarina += float(value['Betrag'])
                except:
                    continue

        fig = px.bar(x=["Luca", "Mirjam", "Sarina"], y=[summe_luca, summe_mirjam, summe_sarina])
        div = plot(fig, output_type="div")

        return render_template("berechnung.html", summe_mirjam=summe_mirjam, summe_luca=summe_luca, summe_sarina=summe_sarina, fig_div=div)
    else:
        return render_template("daten_loeschen.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

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


# Verlinkung auf Ausgaben erfassen
@app.route("/formular/", methods=['GET', 'POST'])
def formular():
    if request.method == 'POST':
        data = request.form
        name = data["name"]
        was = data["was"]
        kategorie = data["kategorie"]
        betrag = data["betrag"]
        zeitpunkt = datetime.now()

        daten = daten_laden()

        my_dict = {"Name": name, "Was": was, "Kategorie": kategorie, "Betrag": betrag}
        daten.update({str(zeitpunkt): my_dict})

        with open("eingaben_nutzer.json", "w") as open_file:
            json.dump(daten, open_file, default=str)
        return render_template("formular.html")
    else:
        return render_template("formular.html")


# Verlinkung auf Übersicht Ausgaben
@app.route("/ausgaben/")
def ausgaben():
    if exists("eingaben_nutzer.json"):
        with open("eingaben_nutzer.json") as open_file:
            json_as_string = open_file.read()
            my_read_dict = loads(json_as_string)

        return render_template("ausgaben.html", eingabe_nutzer=my_read_dict)
    else:
        return render_template("daten_loeschen.html")


# Verlinkung auf Seite die kommt, wenn Daten gelöscht wurden.
@app.route("/ausgaben/daten_loeschen")
def daten_loeschen():
    if exists("eingaben_nutzer.json"):
        os.remove("eingaben_nutzer.json")
        return render_template("daten_loeschen.html")
    else:
        return render_template("daten_loeschen.html")


# Berechnungen für Seite "Zusammenfassung"
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
                    summe_mirjam += float(value["Betrag"])

                except:
                    continue

            elif value["Name"] == 'Luca':
                try:
                    summe_luca += float(value["Betrag"])
                except:
                    continue

            elif value["Name"] == "Sarina":
                try:
                    summe_sarina += float(value["Betrag"])
                except:
                    continue

        summe_lebensmittel = 0
        summe_haushalt = 0
        summe_hygieneartikel = 0
        summe_balkon = 0
        summe_diverses = 0

        for key, value in my_read_dict.items():
            if value["Kategorie"] == "Lebensmittel":
                try:
                    summe_lebensmittel += float(value["Betrag"])
                except:
                    continue

            elif value["Kategorie"] == "Haushalt":
                try:
                    summe_haushalt += float(value["Betrag"])
                except:
                    continue

            elif value["Kategorie"] == "Hygieneartikel":
                try:
                    summe_hygieneartikel += float(value["Betrag"])
                except:
                    continue

            elif value["Kategorie"] == "Balkon":
                try:
                    summe_balkon += float(value["Betrag"])
                except:
                    continue

            elif value["Kategorie"] == "Diverses":
                try:
                    summe_diverses += float(value["Betrag"])
                except:
                    continue

        balkendiagramm = px.bar(
            x=["Luca", "Mirjam", "Sarina"],
            y=[summe_luca, summe_mirjam, summe_sarina],
            labels={"x": "Name", "y": "Betrag"}
        )
        div_balkendiagramm = plot(balkendiagramm, output_type="div")

        liste_kategorien = [summe_lebensmittel, summe_haushalt, summe_hygieneartikel, summe_balkon, summe_diverses]
        liste_namen = ["Lebensmittel", "Haushalt", "Hygieneartikel", "Balkon", "Diverses"]

        kreisdiagramm = px.pie(values=liste_kategorien, names=liste_namen)

        div_kreisdiagramm = plot(kreisdiagramm, output_type="div")

        return render_template("berechnung.html",
                               summe_mirjam=summe_mirjam, summe_luca=summe_luca, summe_sarina=summe_sarina,
                               summe_lebensmittel=summe_lebensmittel,
                               summe_haushalt=summe_haushalt,
                               summe_hygieneartikel=summe_hygieneartikel,
                               summe_balkon=summe_balkon,
                               summe_diverses=summe_diverses,
                               balkendiagramm=div_balkendiagramm,
                               kreisdiagramm=div_kreisdiagramm)
    else:
        return render_template("daten_loeschen.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

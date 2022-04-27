from flask import Flask
from flask import render_template
from flask import request
import daten

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
        #ziel_person = request.form['vorname']
        #rueckgabe_string = "Hello " + ziel_person + "!"
        #return rueckgabe_string
        return render_template("formular.html")
    else:
        return render_template("formular.html")


@app.route("/speichern/<aktivitaet>")
def speichern(aktivitaet):
    zeitpunkt, aktivitaet = daten.aktivitaet_speichern(aktivitaet)

    return "Gespeichert: " + aktivitaet + " um " + str(zeitpunkt)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

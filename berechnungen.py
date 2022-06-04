from json import loads

with open("eingaben_nutzer.json") as open_file:
    json_as_string = open_file.read()
    my_read_dict = loads(json_as_string)

def rechnen_name():

    summe_mirjam = 0
    summe_luca = 0
    summe_sarina = 0

    for key, value in my_read_dict.items():
        if value["Name"] == "Mirjam":
            try:
                summe_mirjam += float(value["Betrag"])

            except:
                continue

        elif value["Name"] == "Luca":
            try:
                summe_luca += float(value["Betrag"])
            except:
                continue

        elif value["Name"] == "Sarina":
            try:
                summe_sarina += float(value["Betrag"])
            except:
                continue

    return summe_mirjam, summe_luca, summe_sarina

def rechnen_kategorie():
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

    return summe_lebensmittel
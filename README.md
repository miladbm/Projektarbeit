# README - Dokumentation WG-Ausgabenübersicht
##  Mirjam Lang


##Problembeschreibung/Motivation
Da ich in einer WG wohne und wir viele gemeinsame Ausgaben haben, möchten wir gerne eine Übersicht aller Ausgaben generieren. Daher erstelle ich in diesem Projekt eine Seite, auf der Ausgaben eingetragen werden könnnen, eine Übersichtsseite mit allen Ausgaben, sowie eine Seite mit den Ausgaben pro Person und den Ausgaben nach Kategorie.

##Betrieb
Für den Betrieb werden die zusätzlichen Pakete Plotly und Flask benötigt. 

Die Datei Main muss zuerst ausgeführt werden. 


##Benutzung
In der Navigation oben können "Ausgaben erfassen" neue Ausgaben eingetragen werden. Bei "Übersicht Ausgaben" ist eine Liste von allen Ausgaben ersichtlich. Auf dieser Seite können zuunterst alle Daten zurückgesetzt werden. Mit diesem Button wird das JSON File, wo die Ausgaben gespeichert sind, gelöscht. Unter "Zusammenfassung" sind die Ausgaben pro Person sowie verschiedene Diagramme mit spannenden Ergänzungen ersichtlich.  


##Ungelöste/unbearbeitete Probleme
Es wurde versucht, die Berechnungen und die Diagramme aus dem Main auszulagern,dies hat zu Anzeigefehlern im HTML geführt. Daher wurden diese wieder zurück ins Main File genommen. Die Datei berechnungen.py wurde mal bestehen gelassen, obwohl diese somit nicht verwendet wird. Die Auslagerung der Berechnung könnte zu einem späteren Zeitpunkt nochmals probiert werden. 

Weiter könnten noch weitere Diagramme zu den Kategorien gemacht und dargestellt werden. 
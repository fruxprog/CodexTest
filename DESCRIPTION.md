# Beschreibung

Diese kleine Testanwendung demonstriert, wie man mit Python und `tkinter`
eine moderne, minimalistische Oberfläche zum Pingen von Hosts erstellt. Die
Applikation unterstützt IPv4- und IPv6-Adressen und zeigt die Ergebnisse in
einem Protokollfenster an.

## Features

- Eingabefeld für Hostnamen oder IP-Adresse
- Zwei Schaltflächen zum Senden von IPv4- bzw. IPv6-Pings
- Logfenster mit automatischem Scrollen für alle Ausgaben
- Plattformübergreifendes `ping`-Kommando
- Einfache Tests zum Überprüfen der Funktion

## Starten

```bash
python ping_gui.py
```

## Tests

```bash
pytest -q
```

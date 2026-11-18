
from db import UsageDB

# Verbindung zur Datenbank herstellen
db = UsageDB()

# Simulierte API-Nutzungsdaten speichern
db.log(
    model="gpt-4o-mini",
    tokens_in=150,
    tokens_out=80,
    cost_usd=0.0000705,
    note="Testaufruf Unit 03"
)

db.log(
    model="gpt-4o-mini",
    tokens_in=200,
    tokens_out=100,
    cost_usd=0.00009,
    note="Zweiter Testaufruf"
)

# Gespeicherte Daten auswerten
print("--- API-Nutzungsstatistik ---")
db.stats()

# Datenbankverbindung schließen
db.close()

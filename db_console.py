
from db import UsageDB

db = UsageDB()

while True:
    print("\n--- API-Datenbank ---")
    print("1 - Statistik anzeigen")
    print("2 - Alle API-Aufrufe anzeigen")
    print("3 - Programm beenden")

    auswahl = input("Deine Auswahl: ").strip()

    if auswahl == "1":
        print("\n--- Statistik ---")
        db.stats()

    elif auswahl == "2":
        print("\n--- Gespeicherte API-Aufrufe ---")

        cursor = db.conn.execute("""
            SELECT id, ts, model, tokens_in,
                   tokens_out, cost_usd, note
            FROM api_calls
            ORDER BY id
        """)

        for row in cursor.fetchall():
            print(
                f"ID: {row[0]} | "
                f"Zeit: {row[1]} | "
                f"Modell: {row[2]} | "
                f"Input: {row[3]} | "
                f"Output: {row[4]} | "
                f"Kosten: ${row[5]:.8f} | "
                f"Notiz: {row[6]}"
            )

    elif auswahl == "3":
        print("Programm wird beendet.")
        break

    else:
        print("Ungültige Eingabe. Bitte 1, 2 oder 3 wählen.")

db.close()

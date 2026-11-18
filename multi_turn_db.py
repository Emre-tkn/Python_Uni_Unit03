
from db import UsageDB

# Datenbank öffnen
db = UsageDB()

# Nachrichtenverlauf anlegen
messages = [
    {
        "role": "system",
        "content": "Du bist ein präziser Assistent."
    }
]

print("Multi-Turn-Chat mit SQLite gestartet!")
print("Zum Beenden 'exit' eingeben.\n")

while True:
    user_input = input("Du: ").strip()

    if user_input.lower() in ("exit", "quit"):
        break

    if not user_input:
        continue

    messages.append({
        "role": "user",
        "content": user_input
    })

    # Einfache lokale Simulation
    if "was habe ich" in user_input.lower():
        previous = [
            msg["content"]
            for msg in messages[:-1]
            if msg["role"] == "user"
        ]

        reply = (
            "Du hast zuvor geschrieben: " + previous[-1]
            if previous
            else "Du hast mir noch nichts erzählt."
        )
    else:
        reply = "Ich habe deine Nachricht gespeichert."

    messages.append({
        "role": "assistant",
        "content": reply
    })

    print(f"Assistent: {reply}\n")

    # Beispielwerte: keine echten API-Tokens
    tokens_in = 30
    tokens_out = 20

    # Beispielpreise aus Unit 02
    cost = (
        tokens_in * 0.00000015
        + tokens_out * 0.0000006
    )

    db.log(
        model="simulation",
        tokens_in=tokens_in,
        tokens_out=tokens_out,
        cost_usd=cost,
        note="multi-turn-simulation"
    )

print("\n--- Datenbankstatistik ---")
db.stats()

print("\n--- Gesprächsverlauf ---")
for msg in messages:
    print(f"{msg['role']}: {msg['content']}")

db.close()


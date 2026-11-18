
# Multi-Turn Conversation – lokale Simulation
# Es wird noch keine echte API aufgerufen.

messages = [
    {
        "role": "system",
        "content": "Du bist ein präziser Assistent."
    }
]

print("Multi-Turn Chat gestartet!")
print("Zum Beenden 'exit' eingeben.\n")

while True:
    user_input = input("Du: ").strip()

    if user_input.lower() in ("exit", "quit"):
        break

    if not user_input:
        continue

    # Neue Nutzernachricht speichern
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Simulierte Antwort anhand des Nachrichtenverlaufs
    if "was habe ich" in user_input.lower():
        vorherige_nachrichten = [
            msg["content"]
            for msg in messages[:-1]
            if msg["role"] == "user"
        ]

        if vorherige_nachrichten:
            reply = (
                "Du hast zuvor geschrieben: "
                + vorherige_nachrichten[-1]
            )
        else:
            reply = "Du hast mir noch nichts erzählt."
    else:
        reply = "Ich habe deine Nachricht gespeichert."

    # Assistentenantwort ebenfalls speichern
    messages.append({
        "role": "assistant",
        "content": reply
    })

    print(f"Assistent: {reply}\n")

print("\n--- Gespeicherter Gesprächsverlauf ---")

for msg in messages:
    print(f"{msg['role']}: {msg['content']}")

print(f"\nInsgesamt {len(messages)} Nachrichten gespeichert.")

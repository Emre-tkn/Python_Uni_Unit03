
import os
from openai import OpenAI
from dotenv import load_dotenv
from db import UsageDB

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Kein API-Schlüssel vorhanden.")
    print("Der echte API-Chat kann noch nicht gestartet werden.")
    raise SystemExit

client = OpenAI(api_key=api_key)
db = UsageDB()

messages = [
    {"role": "system", "content": "Du bist ein präziser Assistent."}
]

print("Multi-Turn-Chat mit echter API gestartet!")
print("Zum Beenden 'exit' eingeben.\n")

try:
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

        try:
            resp = client.responses.create(
                model="gpt-4o-mini",
                input=messages
            )
        except Exception as error:
            messages.pop()
            print(f"API-Fehler: {error}")
            continue

        reply = resp.output_text

        messages.append({
            "role": "assistant",
            "content": reply
        })

        print(f"Assistent: {reply}\n")

        usage = resp.usage

        # Beispielpreise aus deiner Universitätsvorlage
        cost = (
            usage.input_tokens * 0.00000015
            + usage.output_tokens * 0.0000006
        )

        db.log(
            model="gpt-4o-mini",
            tokens_in=usage.input_tokens,
            tokens_out=usage.output_tokens,
            cost_usd=cost,
            note="multi-turn-api"
        )

finally:
    print("\n--- Datenbankstatistik ---")
    db.stats()
    db.close()

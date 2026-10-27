import pandas as pd


def analys_pris_skillnaden(data, exchange_rate=11.14):
    # Samlar priser i en tabell
    df = pd.DataFrame(
        {
            "dates": data["labels"],
            "bensin": data["e95"],
            "diesel": data["diesel"],
        }
    )

    # Gör om priser från EURO till SEK
    df["bensin"] = (df["bensin"] * exchange_rate).round(2)
    df["diesel"] = (df["diesel"] * exchange_rate).round(2)

    # Räknar ut skillnaden mellan bensin och diesel
    df["prisskillnad"] = (df["diesel"] - df["bensin"]).round(2)

    # Skickar tillbaka tabellen
    return df

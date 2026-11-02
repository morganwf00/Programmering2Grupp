import pandas as pd
import plotly.express as px
from flask import render_template

from functions.analys import analys_pris_skillnaden
from functions.currency_converter import convert_to_sek


# Analyserar priset med Pandas
def visa_jamforelse(data):
    df = analys_pris_skillnaden(data)

    # Gör data frame kolumn till listor
    analys_datum = df["dates"].tolist()
    analys_bensin = df["bensin"].tolist()
    analys_diesel = df["diesel"].tolist()
    analys_skillnad = df["prisskillnad"].tolist()

    # Hämtar datum och priser från data
    dates = data["labels"]
    eBensin = data["e95"]
    diesel = data["diesel"]

    # Konvertera priserna från EURO till SEK
    bensin_sek = [convert_to_sek(pris, 11.14) for pris in eBensin]
    diesel_sek = [convert_to_sek(pris, 11.14) for pris in diesel]

    # Priser i en DataFrame för diagram
    diagram1 = pd.DataFrame(
        {
            "Datum": dates,
            "Bensin": bensin_sek,
            "Diesel": diesel_sek,
        }
    )

    # Diagram 1: prisutveckling över tid
    fig1 = px.line(
        diagram1,
        x="Datum",
        y=["Bensin", "Diesel"],
        title="Bensin och dieselpriser över tid",
        labels={"value": "Pris (kr/liter)", "variable": "Bränsle"},
    )

    diagram1 = fig1.to_html(full_html=False)

    # Skickar både diagram och analys till HTML
    return render_template(
        "jamforelse.html",
        dates=dates,
        bensin=bensin_sek,
        diesel=diesel_sek,
        analys_datum=analys_datum,
        analys_bensin=analys_bensin,
        analys_diesel=analys_diesel,
        analys_skillnad=analys_skillnad,
        diagram1=diagram1,
    )

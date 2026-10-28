# Hämtar vad vi behöver för att bygga webapplikatio från Flask
import pandas as pd
import plotly.express as px
from flask import Flask, render_template
from functions.data_fetcher import fetch_fuel_data


# Hämtar funktioner som räkner priset för diesel och bensin, samt prisskillnaden.
from functions.analys import analys_pris_skillnaden

# Hämtar funktionen som räknar om euro till kronor
from functions.currency_converter import convert_to_sek

# Hämtar funktionen som hämtar priset från API
from functions.data_fetcher import fetch_fuel_data

# Skapar Flask-appen
app = Flask(__name__)


# Startsidan
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/minmax")
def minMaxPris():
    return render_template("minMax.html")

# Sida som jämför bensin och dieselpriser
@app.route("/jamforelse_bensin_diesel", methods=["GET"])
def jamforelse_bensin_diesel():

    # Hämtar data från API
    data = fetch_fuel_data()

    # Visar fel om data inte kunde hämtas
    if data is None:
        return render_template(
            "fel.html",
            fel="Vi kunde inte hämta bränslepriser just nu. Vänligen försöka igen senare.",
        ), 503

    # Analyserar priset med Pandas
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


# Visar ett fel meddelande om felet är från clienten
@app.errorhandler(404)
def inte_hittad(fel):
    return render_template(
        "fel.html",
        fel="Sidan kunde inte hittas. Kontrollera addressen.",
    ), 404


# Visar ett felmeddelande om servern får ett fel
@app.errorhandler(500)
def serverfel(fel):
    return render_template(
        "fel.html", fel="Något gick fel på servern. Vänligen försöka igen senare."
    ), 500


# Startar appen när vi kör den här filen
if __name__ == "__main__":
    app.run(debug=True)

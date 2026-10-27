# Hämtar vad vi behöver för att bygga webapplikatio från Flask
from flask import Flask, render_template

# Hämtar funktionen som hämtar priset från API
from functions.data_fetcher import fetch_fuel_data

# Hämtar funktionen som räknar om euro till kronor
from functions.currency_converter import convert_to_sek

# Skapar Flask-appen
app = Flask(__name__)

# Startsidan
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# Sida som jämför bensin och dieselpriser
@app.route("/jamforelse_bensin_diesel" , methods=["GET"])
def jamforelse_bensin_diesel():
    
    # Hämtar data från API
    data = fetch_fuel_data()

    # Visar fel om data inte kunde hämtas
    if data is None:
        return render_template(
            "fel.html",
            fel="Vi kunde inte hämta bränslepriser just nu. Vänligen försöka igen senare."
        ), 503

    # Hämtar datum och priser från data
    dates = data["labels"]
    eBensin = data["e95"]
    diesel = data["diesel"]

    # Konvertera priserna från EURO till SEK
    bensin_sek = [convert_to_sek(pris, 11.14) for pris in eBensin]
    diesel_sek = [convert_to_sek(pris, 11.14) for pris in diesel]

    # Skickar datum och prier i kronor till HTML template
    return render_template(
        "jamforelse.html",
        dates=dates,
        bensin=bensin_sek,
        diesel=diesel_sek,
    )

# Visar ett fel meddelande om felet är från clienten
@app.errorhandler(404)
def inte_hittad(fel):
    return render_template(
        "fel.html",
        fel = "Sidan kunde inte hittas. Kontrollera addressen.",
        ), 404

# Visar ett felmeddelande om servern får ett fel
@app.errorhandler(500)
def serverfel(fel):
     return render_template(
         "fel.html",
         fel="Något gick fel på servern. Vänligen försöka igen senare."
     ), 500

# Startar appen när vi kör den här filen
if __name__ == "__main__":
    app.run(debug=True)

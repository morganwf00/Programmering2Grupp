# Hämtar vad vi behöver för att bygga webapplikatio från Flask och functions module
from flask import Flask, render_template

from functions.data_fetcher import fetch_fuel_data
from functions.e95differance import dfDiff
from functions.graf_minmax import visa_graf_minmax
from functions.jamforelse_bensin_diesel import visa_jamforelse
from functions.match_dag_pris import matchDagOchPrisDiesel, matchDagOchPrisE95
from functions.min_max_pris import *

# .................................................FLASK APPEN..................................................................#
# Skapar Flask-appen
app = Flask(__name__)


# ..................................................STARTSIDAN..................................................................#
# Startsidan
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# ..............................................MIN/MAX PRISET PÅ DIESEL OCH BENSIN.............................................#
# minsta och maxpriset på diesel och e95
@app.route("/minmax")
def minMaxPris():
    data_diesel = matchDagOchPrisDiesel()
    data_e95 = matchDagOchPrisE95()
    max_pris_diesel = hitta_max_diesel(data_diesel)
    min_pris_diesel = hitta_min_diesel(data_diesel)
    max_pris_e95 = hitta_max_e95(data_e95)
    min_pris_e95 = hitta_min_e95(data_e95)
    graf = visa_graf_minmax(
        min_pris_e95, max_pris_e95, min_pris_diesel, max_pris_diesel
    )
    return render_template(
        "minMax.html",
        graf=graf,
        min_diesel=min_pris_diesel,
        min_e95=min_pris_e95,
        max_diesel=max_pris_diesel,
        max_e95=max_pris_e95,
    )


# ......................................................PRICE DIFFERENCE.........................................................#
# Sidan som gämför denna månadens veckopris emot förra
@app.route("/priceDifferance")
def priceDiff():
    data = fetch_fuel_data()

    if data is None:
        return render_template(
            "fel.html",
            fel="Vi kunde inte hämta bränslepriser just nu. Vänligen försök igen senare.",
        ), 503

    fig = dfDiff(data)
    return render_template("priceDiff.html", graph=fig.to_html(full_html=False))


# .......................................................JÄMFÖRELSE: BENSIN OCH DIESEL.............................................................#
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
    # Anropar funktionen från functions mappen
    return visa_jamforelse(data)


# .....................................................ERROR 404...............................................................#
# Visar ett fel meddelande om felet är från clienten
@app.errorhandler(404)
def inte_hittad(fel):
    return render_template(
        "fel.html",
        fel="Sidan kunde inte hittas. Kontrollera addressen.",
    ), 404


# ......................................................ERROR 500..............................................................#
# Visar ett felmeddelande om servern får ett fel
@app.errorhandler(500)
def serverfel(fel):
    return render_template(
        "fel.html", fel="Något gick fel på servern. Vänligen försöka igen senare."
    ), 500


# .......................................................APPLIKATION STARTAR...................................................#
# Startar appen när vi kör den här filen
if __name__ == "__main__":
    app.run(debug=True)

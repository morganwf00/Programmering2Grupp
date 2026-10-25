import requests

API_URL = "https://www.fuel-prices.eu/lang/api/country-history.php?cc=SE"

# Hämtar JSON data från API endpoint
def fetch_fuel_data():
    try:
        # Skickar en förfrågan till API och vänta max 5 sekunder
        svar = requests.get(API_URL, timeout=5)

        # kolla om något gick fel och ger ett felmeddelande
        svar.raise_for_status() 

        # gör om JSON svaret till python-data (dict/lista)
        return svar.json() 

    except requests.exceptions.RequestException as fel:
        # Om något gick fel: skriv ut felet och skicka tillbaka ingenting
        print(f"Fel vid hämtning av data: {fel}")
        return None

# Den här delen körs bara när vi starter filen direkt
if __name__ == "__main__":
    # Hämtar data med fuktionen
    data = fetch_fuel_data()

    # Om vi fick data, skriver ut nycklarna
    if data is not None:
        print(data.keys())

    # Annars visar ett fel meddelande
    else:
        print("Kunde inte hämta data")

         
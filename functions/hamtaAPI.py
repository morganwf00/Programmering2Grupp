import json

import requests


def hamtaAPI():
    url ="https://www.fuel-prices.eu/lang/api/country-history.php?cc=SE"
    data = requests.get(url)
    response =  requests.get(url, timeout=5)
    response.raise_for_status()

    return json.loads(data)
# kan anropas data i eran funktion med en variabel 
# --> var = hamtaAPI() 
# och variabeln ska innehålla allt data från api i json form
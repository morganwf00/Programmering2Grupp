from functions.hamtaAPI import hamtaAPI
from data_fetcher import fetch_fuel_data

def test_hamtaAPI():
    data = fetch_fuel_data()
    assert data["cc"] == "SE"
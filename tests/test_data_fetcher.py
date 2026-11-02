from functions.data_fetcher import fetch_fuel_data


# test funktioner fär att checka API fetch funkar bra
def test_hamtaAPI():
    data = fetch_fuel_data()
    dates = data["labels"]

    assert dates[0] == "2021-11-01"


def test_hamtaAPI2():
    data = fetch_fuel_data()
    eBensin = data["e95"]
    assert eBensin[0] == 1.804


def test_hamtaAPI3():
    data = fetch_fuel_data()
    diesel = data["diesel"]

    assert diesel[0] == 1.943

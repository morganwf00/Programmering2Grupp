import pytest
from unittest.mock import Mock, patch
from app import app
from functions.match_dag_pris import matchDagOchPrisDiesel, matchDagOchPrisE95


DATA={"cc":"SE",
    "labels":["2021-11-01","2021-11-08","2021-11-15","2021-11-22","2021-11-29","2021-12-06","2021-12-13","2021-12-20"],
    "e95":[1.804,1.799,1.8,1.754,1.726,1.663,1.67,1.671, 1.413],
    "diesel":[1.943,1.908,1.904,1.864,1.833,1.829,1.836,1.829,],
        "count":259,
        "missing_weeks":[],
        "isolated":{"e95":[],"diesel":[]},
        "attribution":{"text":"Data: fuel-prices.eu, CC BY 4.0",
        "url":"https://www.fuel-prices.eu/press/#cite",
        "license":"https://creativecommons.org/licenses/by/4.0/",
        "note":"Weekly figures from the European Commission Weekly Oil Bulletin (CC BY 4.0). Show the text, linked to https://www.fuel-prices.eu/, next to the data."
        }}

@pytest.fixture
def klient():
    app.config["TESTING"] = True
    return app.test_client()

@patch("functions.data_fetcher.requests.get")
def test_data(mock_get, klient):
    mock_get.return_value= Mock(json=lambda: DATA)
    svar = klient.get("/minmax")
    assert svar.status_code == 200
    assert  "1.804" in svar.get_data(as_text=True)
    assert "2021-11-01" in mock_get.return_value.json()["labels"]

    

# testar om pris och dag för diesel och e95 matchas,
# det första index av listan från funktionen ska vara en dictionary
# med datum och pris, checkar om båda stämmer
@patch("functions.data_fetcher.requests.get")
def test_prise95(mock_get, klient): 
    mock_get.return_value= Mock(json=lambda: DATA)
    svar = klient.get("/minmax")
    data = matchDagOchPrisE95()
    assert data[0]["pris"] == 1.804
    assert data[0]["dag"] == "2021-11-01"

@patch("functions.data_fetcher.requests.get")
def test_pris_diesel(mock_get, klient):
    data = matchDagOchPrisDiesel()
    assert data[0]["pris"] == 1.943
    assert data[0]["dag"] == "2021-11-01"

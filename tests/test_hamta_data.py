from unittest.mock import Mock, patch

import pytest

from app import app
from functions.analys import analys_pris_skillnaden
from functions.match_dag_pris import matchDagOchPrisDiesel, matchDagOchPrisE95
from functions.data_fetcher import fetch_fuel_data

DATA = {
    "cc": "SE",
    "labels": [
        "2021-11-01",
        "2021-11-08",
        "2021-11-15",
        "2021-11-22",
        "2021-11-29",
        "2021-12-06",
        "2021-12-13",
        "2021-12-20",
    ],
    "e95": [1.804, 1.799, 1.8, 1.754, 1.726, 1.663, 1.67, 1.671, 1.413],
    "diesel": [
        1.943,
        1.908,
        1.904,
        1.864,
        1.833,
        1.829,
        1.836,
        1.829,
    ],
    "count": 259,
    "missing_weeks": [],
    "isolated": {"e95": [], "diesel": []},
    "attribution": {
        "text": "Data: fuel-prices.eu, CC BY 4.0",
        "url": "https://www.fuel-prices.eu/press/#cite",
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "note": "Weekly figures from the European Commission Weekly Oil Bulletin (CC BY 4.0). Show the text, linked to https://www.fuel-prices.eu/, next to the data.",
    },
}


# Fixture som rensar cache och används automatisk för varje test
# Yield låter testen börja
@pytest.fixture(autouse=True)
def clear_cache():
    fetch_fuel_data.cache_clear()
    yield
    fetch_fuel_data.cache_clear()


# ------------------------------------------------------------------------------------------------
# pytest decorator förbereder test miljön.
# klient förbereds för att simulera av en  HTTP request#
@pytest.fixture
def klient():
    app.config["TESTING"] = True  # aplikationen körs i test mode
    return app.test_client()


# ersätter en riktig API-request, kommer från unitest.mock
# mock_get ges av @patch och klient ges av @pytest.fixture
@patch("functions.data_fetcher.requests.get")
def test_data(mock_get, klient):
    # fake python object som simulerar requests.get().
    # Motsvarar response = requests.get(API_URL)
    # return response.json()
    mock_get.return_value = Mock(json=lambda: DATA)
    svar = klient.get("/minmax")
    assert svar.status_code == 200  # checkar success
    assert "SE" in mock_get.return_value.json()["cc"]
    assert "2021-11-01" in mock_get.return_value.json()["labels"]


# ------------------------------------------------------------------------------------------------
# testar om pris och dag för diesel och e95 matchas,
# det första index av listan från funktionen ska vara en dictionary
# med datum och pris, checkar om båda stämmer
@patch("functions.data_fetcher.requests.get")
def test_prise95(mock_get):
    mock_get.return_value = Mock(json=lambda: DATA)
    data = matchDagOchPrisE95()
    assert data[0]["pris"] == 1.804
    assert data[0]["dag"] == "2021-11-01"


@patch("functions.data_fetcher.requests.get")
def test_pris_diesel(mock_get):
    mock_get.return_value = Mock(json=lambda: DATA)
    data = matchDagOchPrisDiesel()
    assert data[0]["pris"] == 1.943
    assert data[0]["dag"] == "2021-11-01"


# ------------------------------------------------------------------------------------------------
def test_analys():
    data = {
        "labels": ["2021-10-25"],
        "e95": [1.787],
        "diesel": [1.926],
    }

    df = analys_pris_skillnaden(data, exchange_rate=11.14)

    assert df["bensin"].tolist() == [19.91]
    assert df["diesel"].tolist() == [21.46]
    assert df["prisskillnad"].tolist() == [1.55]

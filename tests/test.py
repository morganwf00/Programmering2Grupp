from functions.hamtaAPI import hamtaAPI

def test_hamtaAPI():
    data = hamtaAPI()
    assert data["cc"] == "SE"
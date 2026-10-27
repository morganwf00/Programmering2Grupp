from functions.analys import analys_pris_skillnaden


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

"""Alla funktioner har ett argument som ges när funktionen anropas, vilket förväntas vara data från api:et
omvandlad med match_dag_pris funktionen.
Datan tas och funktionen letar antingen för det lägsta eller högsta priset på bensinet(en dictionary)
key=lambda x: x["pris"] är en en rads funktion som returnerar key från dictionary man får som argument
till sist kommer alla funktioner returnera priset i form av float"""


def hitta_min_diesel(dieselPriser: dict):
    minPricedItem = min(dieselPriser, key=lambda x: x["pris"])
    return float(minPricedItem["pris"])


def hitta_min_e95(e95Priser: dict):
    minPricedItem = min(e95Priser, key=lambda x: x["pris"])
    return float(minPricedItem["pris"])


def hitta_max_diesel(dieselPriser: dict):
    maxPricedItem = max(dieselPriser, key=lambda x: x["pris"])
    return float(maxPricedItem["pris"])


def hitta_max_e95(e95Priser: dict):
    maxPricedItem = max(e95Priser, key=lambda x: x["pris"])
    return float(maxPricedItem["pris"])

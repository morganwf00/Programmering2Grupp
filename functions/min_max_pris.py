
def hitta_min_diesel(dieselPriser):
    minPricedItem = min(dieselPriser, key=lambda x:(x['pris']))
    return float(minPricedItem["pris"])
def hitta_min_e95(e95Priser):
    minPricedItem = min(e95Priser, key=lambda x:x['pris'])
    return float(minPricedItem["pris"])

def hitta_max_diesel(dieselPriser):
    maxPricedItem = max(dieselPriser, key=lambda x:x['pris'])
    return float(maxPricedItem["pris"])
def hitta_max_e95(e95Priser):
    maxPricedItem = max(e95Priser, key=lambda x:x['pris'])
    return float(maxPricedItem["pris"])

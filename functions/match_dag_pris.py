from functions.data_fetcher import fetch_fuel_data


def matchDagOchPrisE95():
    prisPerDage95 = []
    data = fetch_fuel_data()

    dagar = data["labels"]
    priserE95 = data["e95"]

    for dag, pris in zip(dagar, priserE95):
        prisPerDage95.append({
            "dag": dag,
            "pris": pris
        })
    return prisPerDage95
def matchDagOchPrisDiesel():
    prisPerDagDiesel = []
    
    data = fetch_fuel_data()

    dagar = data["labels"]
    priserDiesel = data["diesel"]
    
    for dag, pris in zip(dagar, priserDiesel):
        prisPerDagDiesel.append({
            "dag": dag,
            "pris": pris
        })
    return prisPerDagDiesel 
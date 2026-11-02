from functions.data_fetcher import fetch_fuel_data

"""
Båda funktioner gör det samma:
 1. skapar en tom lista och hämtar dagar och priser fär bränslen från API:et
 2. en for loop hämtar dagar och priser och blandar dem i en enda lista som i den här exempel:
 Input: a = ["Nisse", "Eva", "Dennis"], b = [10, 85, 25]
 Output: [("Nisse", 10), ("Eva", 85), ("Dennis", 25)]
 3. lägger till dagen och pris som en dictionary på tom listan som skapades i början
 4. Returnerar listan av dictionaries
 """


def matchDagOchPrisE95():
    prisPerDage95 = []
    data = fetch_fuel_data()

    dagar = data["labels"]
    priserE95 = data["e95"]

    for dag, pris in zip(dagar, priserE95):
        prisPerDage95.append({"dag": dag, "pris": pris})
    return prisPerDage95


def matchDagOchPrisDiesel():
    prisPerDagDiesel = []

    data = fetch_fuel_data()

    dagar = data["labels"]
    priserDiesel = data["diesel"]

    for dag, pris in zip(dagar, priserDiesel):
        prisPerDagDiesel.append({"dag": dag, "pris": pris})
    return prisPerDagDiesel

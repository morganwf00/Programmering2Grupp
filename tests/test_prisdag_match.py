from functions.match_dag_pris_e95 import matchDagOchPrisE95, matchDagOchPrisDiesel

#testar om pris och dag för diesel och e95 matchas, 
#det första index av listan från funktionen ska vara en dictionary
#med datum och pris, checkar om båda stämmer
def test_prise95():
    data = matchDagOchPrisE95()
    assert data[0]["pris"] == 1.804
    assert data[0]["dag"] == "2021-11-01"

def test_pris_diesel():
    data = matchDagOchPrisDiesel()
    assert data[0]["pris"] == 1.943
    assert data[0]["dag"] == "2021-11-01"
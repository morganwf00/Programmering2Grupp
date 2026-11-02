import plotly.express as px

""" fuktionen hämatar minsta och högsta priser från API:et och lagrasden i en dictionary som används till grafen
 - fig betyder figure och är själva grafen i python version som sedan omvandlas till en html element
 - update_layout anvönds för styling av själva grafen"""


def visa_graf_minmax(min_e95, max_e95, min_diesel, max_diesel):
    data = {
        "bensin": ["e95", "diesel"],
        "minpris": [min_e95, min_diesel],
        "maxpris": [max_e95, max_diesel],
    }
    fig = px.bar(
        data,
        x="bensin",
        y=["minpris", "maxpris"],
        barmode="group",
        labels={"variabel": "Pris", "bensin": "Typ av bensin", "värde": "Pris(kr/l)"},
        title="Högsta och lägsta pris på bensin",
    )

    fig.update_layout(title_font_size=20, autosize=True, paper_bgcolor="#e3e3e3")
    return fig.to_html(
        full_html=False,  # detta är för att inte skapa hela html strukturen, bara elementen till grafen
        include_plotlyjs="cdn",  # plotly använder javascript från en extern server, det behövs anslut till nätverk för grafen
        default_width="50%",
        default_height="100%",
    )

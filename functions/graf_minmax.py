import plotly.express as px

def visa_graf_minmax(min_e95, max_e95, min_diesel, max_diesel):
    data = {"bensin":["e95","diesel"],
            "minpris":[min_e95,min_diesel],
            "maxpris":[max_e95,max_diesel]}
    fig = px.bar(
        data,
        x="bensin",
        y=["minpris", "maxpris"],
        barmode="group",
        labels={
            "variabel": "Pris",
            "bensin": "Typ av bensin",
            "värde": "Pris(kr/l)"
        },
        title="Högsta och lägsta pris på bensin"
    )

    fig.update_layout(
        title_font_size=20,
        autosize=True,
        paper_bgcolor="#e3e3e3"
    )
    return fig.to_html(full_html=False, include_plotlyjs="cdn",default_width="50%",default_height="100%")

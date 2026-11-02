import pandas as pd
import plotly.express as px


def dfDiff(data):
    """ Make a data frame from jsonAPI with kr/liter and two months based on days"""
    df = pd.DataFrame({
        "time": pd.to_datetime(data["labels"]),
        "priceEUR": data["e95"]}
                      )
    #convert to SEK
    df["kr/liter"] = df["priceEUR"] * 11.14
    
    # Hitta senaste datumet ex 2026-11-26
    latestDate = df["time"].max()
    #Listar ut vilken månad som var den förra ex 2026-10-26
    previusDate = latestDate - pd.DateOffset(months=1)

    # Nuvarande månads alla dagar med rätt år
    currentMonth = df[
        # varje rad som har samma år som senaste datumet ex 2026
        (df["time"].dt.year == latestDate.year)&
        #  varje rad som har samma månad som senaste datumet ex 11
        (df["time"].dt.month == latestDate.month)
    ]

    # Förra månaden alla dagar med rätt år
    lastMonth = df[
        # varje rad som har samma år som tidigare datumet ex 2026
        (df["time"].dt.year == previusDate.year)&
        # varje rad som har samma månad som tidigare datumet ex 10
        (df["time"].dt.month == previusDate.month)
    ]

    # Lägg till månadsnamn och dag i månaden
    currentMonth = currentMonth.assign(
        #kolumnen "månad" får string värdet av nuvarnde månaden ex 11 = november = %B
        month=latestDate.strftime("%B"),
        #kolumen "dag" får alla dagar i den nuvarande månaden
        day=currentMonth["time"].dt.day,
    )
    # Lägg till månadsnamn och dag ifrån förra månaden
    lastMonth = lastMonth.assign(
        #kolumnen "month" får string värdet av den tidigare månaden ex 10 = oktober = %B
        month=previusDate.strftime("%B"),
        #kolumen "dag" får alla dagar i den nuvarande månaden
        day=lastMonth["time"].dt.day,
    )

    # Slå ihop till en dataframe
    combined = pd.concat([lastMonth, currentMonth])

    # Plotly-graf
    return px.line(
        combined,
        x="day",
        y="kr/liter",
        color="month",
        markers=True,
        title="Bensinpris (E95) i kr/liter: nuvarande vs förra månaden",
        labels={"day": "Dag i månaden", "kr/liter": "kr/liter"},
    )

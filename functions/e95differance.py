import pandas as pd
import plotly.express as px


def dfDiff(data):
    """Make a data frame from jsonAPI with kr/liter and two months based on days, and an avrage of the last 12 months."""
    
    df = pd.DataFrame({"time": pd.to_datetime(data["labels"]), "priceEUR": data["e95"]})
    # convert to SEK
    df["kr/liter"] = df["priceEUR"] * 11.14
    
    """Current month"""
    # Hitta senaste datumet ex 2026-11-26
    latestDate = df["time"].max()
    # Nuvarande månads alla dagar med rätt år
    currentMonth = df[
        # varje rad som har samma år som senaste datumet ex 2026
        (df["time"].dt.year == latestDate.year)
        &
        #  varje rad som har samma månad som senaste datumet ex 11
        (df["time"].dt.month == latestDate.month)
    ]
    # Lägg till månadsnamn och dag i månaden
    currentMonth = currentMonth.assign(
        # kolumnen "månad" får string värdet av nuvarnde månaden ex 11 = november = %B
        month=latestDate.strftime("%B"),
        # kolumen "day" får alla dagar i den nuvarande månaden
        day=currentMonth["time"].dt.day,
    )
    
    """Previous month"""
    # Listar ut vilken månad som var den förra ex 2026-10-26
    previousDate = latestDate - pd.DateOffset(months=1)    
    # Förra månaden alla dagar med rätt år
    lastMonth = df[
        # varje rad som har samma år som tidigare datumet ex 2026
        (df["time"].dt.year == previousDate.year)
        &
        # varje rad som har samma månad som tidigare datumet ex 10
        (df["time"].dt.month == previousDate.month)
    ]
    # Lägg till månadsnamn och dag ifrån förra månaden
    lastMonth = lastMonth.assign(
        # kolumnen "month" får string värdet av den tidigare månaden ex 10 = oktober = %B
        month=previousDate.strftime("%B"),
        # kolumen "day" får alla dagar i den nuvarande månaden
        day=lastMonth["time"].dt.day,
    )    

    """12 month average"""    
    # hitta datumet för 12 månader back ex 2026-11-26 - 12 month = 2025-11-26
    Back12Months = latestDate - pd.DateOffset(months=12)
    # Filter to all dates above this date
    last12 = df[df["time"] >= Back12Months].copy()
    #see how many times five fits into the day date and multiply by five to get the five day interval
    last12["day"] = last12["time"].dt.day // 5 * 5
    
    avgMonth = (
        # make a group for each day date and calculate the average price for each day        
        last12.groupby("day", as_index=False)["kr/liter"].mean()
        .assign(month="12 month average")
    )

    # Slå ihop till en dataframe
    combined = pd.concat([lastMonth, currentMonth, avgMonth])

    # Plotly-graf
    return px.line(
        combined,
        x="day",
        y="kr/liter",
        color="month",
        markers=True,
        title="Bensinpris (E95) i kr/liter: nuvarande vs förra månaden",
        labels={"day": "Dag", "kr/liter": "kronor"},
    )
